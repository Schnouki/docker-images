#!/usr/bin/env sh

if [ "$#" -ne 2 ]; then
    echo "Usage: $(basename $0) host port"
    exit 1
fi

HOST="$1"
PORT="$2"

echo "Relaying TCP connections on port ${PORT} to ${HOST}:${PORT}"
exec socat tcp-listen:${PORT},fork,reuseaddr tcp:${HOST}:${PORT}
