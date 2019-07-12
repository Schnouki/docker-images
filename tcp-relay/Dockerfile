FROM alpine:3.9

RUN apk add --no-cache socat

COPY entrypoint.sh /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]
