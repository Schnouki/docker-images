FROM alpine:3.8

# Based on Wonderfall's image:
# https://github.com/Wonderfall/docker-isso
# https://hub.docker.com/r/wonderfall/isso/

ARG ISSO_VER=0.10.6

ENV GID=1000 UID=1000 ISSO_SETTINGS=/config/isso.conf

EXPOSE 8080
VOLUME /db /config

RUN apk -U upgrade \
 && apk add -t build-dependencies \
    python3-dev \
    libffi-dev \
    build-base \
 && apk add \
    python3 \
    sqlite \
    libressl \
    ca-certificates \
    su-exec \
    tini \
 && pip3 install --upgrade pip \
 && pip3 install --no-cache cffi gunicorn misaka==1.0.2 "isso==${ISSO_VER}" \
 && apk del build-dependencies \
 && rm -rf /tmp/* /var/cache/apk/*

COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]

CMD ["gunicorn", "-b", "0.0.0.0:8080", "-w", "4", "--preload", "isso.run"]
