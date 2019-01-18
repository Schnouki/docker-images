FROM alpine:latest

ARG STAPLER_VERSION=0.4

RUN apk add -U make poppler-utils py2-pypdf2 texlive-full \
        && mkdir /opt \
        && cd /opt \
        && wget https://github.com/hellerbarde/stapler/archive/${STAPLER_VERSION}.zip \
        && unzip ${STAPLER_VERSION}.zip \
        && rm ${STAPLER_VERSION}.zip \
        && ln -s /opt/stapler-${STAPLER_VERSION}/stapler /usr/bin/stapler
