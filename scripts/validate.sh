#!/bin/sh
set -eu
if [ "$#" -ne 0 ]; then
    printf '%s\n' 'validate.sh accepts no arguments.' >&2
    exit 2
fi
root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
docker run --rm --network none --read-only --cap-drop ALL --security-opt no-new-privileges --user "$(id -u):$(id -g)" --tmpfs /tmp:rw,noexec,nosuid,size=32m --mount "type=bind,src=$root,dst=/workspace,readonly" ghcr.io/gitleaks/gitleaks@sha256:c00b6bd0aeb3071cbcb79009cb16a60dd9e0a7c60e2be9ab65d25e6bc8abbb7f dir /workspace --redact --no-banner
docker build --file "$root/infra/docker/Dockerfile" --tag sepia-asd-ste-validation "$root"
exec docker run --rm --network none --read-only --cap-drop ALL --security-opt no-new-privileges --user "$(id -u):$(id -g)" --tmpfs /tmp:rw,noexec,nosuid,size=32m --mount "type=bind,src=$root,dst=/workspace,readonly" sepia-asd-ste-validation python -B -m tools.validate_repository
