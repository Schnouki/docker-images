FROM alpine:3.9

RUN apk add --no-cache python3 socat

COPY entrypoint.py /entrypoint.py
ENTRYPOINT ["/entrypoint.py"]
