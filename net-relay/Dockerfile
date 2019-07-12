FROM alpine:3.9

RUN apk add --no-cache python3 socat tini

COPY entrypoint.py /entrypoint.py
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.py"]
