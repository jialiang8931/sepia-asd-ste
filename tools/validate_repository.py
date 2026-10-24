import ast
import json
from pathlib import Path
import re
import subprocess
import sys


SECRET_PATTERNS = (
    re.compile(r"(?:AK" + r"IA|AS" + r"IA)[A-Z0-9]{16}"),
    re.compile(r"gh" + r"[opusr]_[A-Za-z0-9]{20,}"),
    re.compile(r"github" + r"_pat_[A-Za-z0-9_]{20,}"),
    re.compile(r"-----BEGIN " + r"(?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    re.compile(r"(?i)(?:aws_secret_access_key|password|api_key|access_token)\s*[:=]\s*[\"']?[A-Za-z0-9/+_=.-]{20,}"),
)


def scan_text(name: str, content: str) -> tuple[str, ...]:
    return tuple(
        f"{name}: possible secret pattern {index + 1}"
        for index, pattern in enumerate(SECRET_PATTERNS)
        if pattern.search(content)
    )


def check_path(name: str) -> tuple[str, ...]:
    path = Path(name)
    forbidden = (
        ".aws" in path.parts
        or ".terraform" in path.parts
        or path.name in {"credentials", ".env"}
        or (path.name.startswith(".env.") and path.name != ".env.example")
        or ".tfstate" in path.name
        or path.suffix in {".pem", ".key", ".tfplan", ".log", ".sqlite", ".db"}
    )
    return (f"{name}: prohibited sensitive/generated path",) if forbidden else ()


def check_script(name: str, content: str) -> tuple[str, ...]:
    findings = []
    guard = 'if [ "$#" -ne 0 ]; then'
    build = "docker build "
    if not content.startswith("#!/bin/sh\nset -eu\n" + guard):
        findings.append(f"{name}: reject arguments before side effects")
    if not re.search(r'if \[ "\$#" -ne 0 \]; then\n.*\n    exit 2\nfi', content):
        findings.append(f"{name}: argument guard must exit with status 2")
    for forbidden in ("$@", "${@}", "$*", "${*}", "getopts", "eval ", "case ", "MODE=", "ENV=", "RUN_TESTS="):
        if forbidden in content:
            findings.append(f"{name}: unsupported dispatch syntax")
    if build not in content or '--file "$root/infra/docker/Dockerfile"' not in content:
        findings.append(f"{name}: explicit Dockerfile and build required")
    if not content.rstrip().endswith(("tools.validate_repository", "tests -v")):
        findings.append(f"{name}: unexpected final action")
    return tuple(findings)


def check_core(name: str, content: str, allowed_imports: frozenset[str]) -> tuple[str, ...]:
    try:
        module = ast.parse(content)
    except SyntaxError:
        return (f"{name}: invalid Python syntax",)
    imports = tuple(
        alias.name if isinstance(node, ast.Import) else node.module or ""
        for node in ast.walk(module)
        if isinstance(node, (ast.Import, ast.ImportFrom))
        for alias in (node.names if isinstance(node, ast.Import) else (None,))
    )
    return tuple(
        f"{name}: core import is not approved: {module_name}"
        for module_name in imports
        if module_name not in allowed_imports
    )


def inspect_repository(root: Path) -> tuple[str, ...]:
    architecture = json.loads((root / "contracts/architecture.json").read_text())
    scripts = json.loads((root / "contracts/scripts.json").read_text())
    findings = []
    for directory in architecture["required_directories"]:
        if not (root / directory).is_dir():
            findings.append(f"{directory}: required directory missing")
    for filename in architecture["required_files"]:
        if not (root / filename).is_file():
            findings.append(f"{filename}: required file missing")
    actual_scripts = {path.name for path in (root / "scripts").iterdir() if path.is_file()}
    if actual_scripts != set(scripts["entrypoints"]):
        findings.append("scripts: actual entrypoints differ from approved contract")
    allowed_imports = frozenset(architecture["sample_core_allowed_imports"])
    for path in sorted(root.rglob("*")):
        relative = path.relative_to(root)
        if ".git" in relative.parts:
            continue
        if path.is_symlink():
            findings.append(f"{relative}: symlinks are not allowed in this template")
            continue
        findings.extend(check_path(relative.as_posix()))
        if not path.is_file():
            continue
        try:
            content = path.read_text()
        except UnicodeDecodeError:
            findings.append(f"{relative}: binary file requires explicit review")
            continue
        findings.extend(scan_text(relative.as_posix(), content))
        if relative.parts[0] == "scripts":
            findings.extend(check_script(relative.as_posix(), content))
            if not path.stat().st_mode & 0o111:
                findings.append(f"{relative}: script must be executable")
        if relative.parts[:2] == ("services", "sample") and "core" in relative.parts and path.suffix == ".py":
            findings.extend(check_core(relative.as_posix(), content, allowed_imports))
    for filename in (".gitignore", ".dockerignore"):
        content = (root / filename).read_text()
        for required in (".aws", ".env", "*.pem", "*.key", "*.tfstate", "*.tfplan"):
            if required not in content:
                findings.append(f"{filename}: missing protection for {required}")
    if not re.search(r"^FROM python@sha256:[a-f0-9]{64}$", (root / "infra/docker/Dockerfile").read_text(), re.MULTILINE):
        findings.append("Dockerfile: base image must be pinned by digest")
    return tuple(findings)


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    try:
        findings = inspect_repository(root)
    except (OSError, ValueError, KeyError, TypeError):
        print("Repository contract could not be inspected.", file=sys.stderr)
        return 1
    if findings:
        print("\n".join(findings), file=sys.stderr)
        return 1
    print("Repository checks passed. Secret checks are heuristic, not a complete security audit.", flush=True)
    return subprocess.run(
        [sys.executable, "-B", "-m", "unittest", "discover", "-s", "tests", "-v"],
        cwd=root,
        check=False,
    ).returncode


if __name__ == "__main__":
    raise SystemExit(main())
