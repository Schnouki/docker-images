FROM alpine:latest

ENTRYPOINT ["tini", "--"]

ENV IMAPFILTER_HOME=/data
VOLUME /data

ARG APP_UID=1000
ARG APP_GID=1000

RUN addgroup -g ${APP_GID} -S app \
    && adduser -D -u ${APP_UID} -S -h /data app \
    && apk add --no-cache ca-certificates tini \
    && apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/testing imapfilter

USER app

CMD ["/usr/bin/imapfilter"]
