#!/usr/bin/env python3

import argparse
import os


def main():
    parser = argparse.ArgumentParser(
        description="Relay network connections to another host."
    )
    parser.add_argument("hostname", type=str, help="target hostname")
    parser.add_argument("ports", type=int, nargs="+", help="port numbers")
    parser.add_argument(
        "-t",
        "--tcp",
        action="store_const",
        const=True,
        help="use TCP connections (default)",
    )
    parser.add_argument(
        "-u", "--udp", action="store_const", const=True, help="use UDP connections"
    )

    args = parser.parse_args()

    protos = []
    if args.tcp or (args.tcp is None and args.udp is None):
        protos.append("tcp")
    if args.udp:
        protos.append("udp")

    cmd = ["socat"]
    for proto in protos:
        for port in args.ports:
            cmd += [
                f"{proto}-listen:{port},fork,reuseaddr",
                f"{proto}:{args.hostname}:{port}",
            ]
    print(
        "Relaying {protos} traffic to host {host} for port{s} {ports}".format(
            protos=" and ".join(proto.upper() for proto in protos),
            host=args.hostname,
            s="" if len(args.ports) == 1 else "s",
            ports=", ".join(str(port) for port in args.ports),
        )
    )
    os.execvp(cmd[0], cmd)


if __name__ == "__main__":
    main()
