FROM python@sha256:35caba83af2fe6da9a5d922f9b0156f21d1246a48278c58a08bd253303ba42e8
WORKDIR /workspace
ENV PYTHONDONTWRITEBYTECODE=1
COPY AGENTS.md README.md .gitignore .dockerignore ./
COPY contracts ./contracts
COPY services ./services
COPY tests ./tests
COPY tools ./tools
COPY scripts ./scripts
COPY docs ./docs
COPY infra ./infra
COPY skills ./skills
USER 65532:65532
CMD ["python", "-B", "-m", "tools.validate_repository"]
