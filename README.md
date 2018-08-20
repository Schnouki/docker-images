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
