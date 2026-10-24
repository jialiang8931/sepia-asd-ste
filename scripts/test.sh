#!/bin/sh
set -eu
if [ "$#" -ne 0 ]; then
    printf '%s\n' 'test.sh accepts no arguments.' >&2
    exit 2
fi
root="$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)"
docker build --file "$root/infra/docker/Dockerfile" --tag sepia-asd-ste-validation "$root"
exec docker run --rm --network none --read-only --cap-drop ALL --security-opt no-new-privileges --user "$(id -u):$(id -g)" --tmpfs /tmp:rw,noexec,nosuid,size=32m --mount "type=bind,src=$root,dst=/workspace,readonly" sepia-asd-ste-validation python -B -m unittest discover -s tests -v
