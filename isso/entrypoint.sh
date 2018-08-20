#!/bin/sh
chown -R $UID:$GID /db /config
exec su-exec $UID:$GID /sbin/tini -- "$@"
