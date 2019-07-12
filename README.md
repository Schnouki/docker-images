# Docker images

Some Docker images that may be useful…


## imapfilter

A mini-image running [imapfilter](https://github.com/lefcha/imapfilter). The
configuration is in `/data`, which is a volume. So it will read its configuration from
`/data/config.lua`.


## isso

[Isso](https://posativ.org/isso/) is a commenting server similar to Disqus…
except it's free software, self-hosted, lightweight, and respects your privacy.
The configuration is in `/config`, the (SQLite) database in `/db`.


## texlive

A full Texlive distribution with some extra tools (make, stapler, and stuff from
poppler-utils like pdfinfo).


## tcp-relay

A simple TCP relay using socat. Use `TARGET_HOST PORT` as the command, and it
will relay incoming TCP traffic on port `PORT` to the same port on
`TARGET_HOST`.
