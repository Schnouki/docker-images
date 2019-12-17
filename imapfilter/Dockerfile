FROM alpine:latest

ENTRYPOINT ["tini", "--"]

ENV IMAPFILTER_HOME=/data
VOLUME /data

ARG APP_UID=1000
ARG APP_GID=1000
ARG IMAPFILTER_VERSION=2.6.11

RUN addgroup -g ${APP_GID} -S app \
    && adduser -D -u ${APP_UID} -S -h /data app \
    && apk add --no-cache ca-certificates lua5.3 openssl pcre tini \
    && apk add --no-cache --virtual _build_stuff \
       build-base git lua5.3-dev openssl-dev pcre-dev \
    && git clone -b v${IMAPFILTER_VERSION} --depth=1 https://github.com/lefcha/imapfilter /imapfilter \
    && cd /imapfilter \
    && make INCDIRS="-I/usr/include/lua5.3" LIBDIRS="-L/usr/lib/lua5.3" all install \
    && cd / \
    && rm -rf /imapfilter \
    && apk del --no-cache _build_stuff

USER app

CMD ["/usr/local/bin/imapfilter"]
