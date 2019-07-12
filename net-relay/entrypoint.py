#!/usr/bin/env python3

import argparse
import os
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(
        description="Relay network connections to another host."
    )
    parser.add_argument(
        "--tcp",
        "-t",
        action="store_const",
        const=True,
        help="use TCP connections (default)",
    )
    parser.add_argument(
        "--udp", "-u", action="store_const", const=True, help="use UDP connections"
    )
    parser.add_argument(
        "--debug", "-d", action="store_true", help="enable socket debugging"
    )
    parser.add_argument("hostname", type=str, help="target hostname")
    parser.add_argument("port", type=int, nargs="+", help="port numbers")

    args = parser.parse_args()

    protos = []
    if args.tcp or (args.tcp is None and args.udp is None):
        protos.append("tcp")
    if args.udp:
        protos.append("udp")

    debug = ""
    if args.debug:
        debug = ",debug"

    cmds = []
    for proto in protos:
        for port in args.port:
            print(f"Starting to relay {proto}/{port} to {args.hostname}...")
            cmd = ["socat",
                   f"{proto}-listen:{port},fork,reuseaddr{debug}",
                   f"{proto}:{args.hostname}:{port}{debug}",
            ]
            p = subprocess.Popen(cmd, close_fds=True, cwd="/", start_new_session=True)
            p.poll()

    # Now wait until one subprocess exit, and exit this script. This will cause
    # tini to kill the remaining processes, and the whole container will stop.
    pid, status = os.wait()
    if os.WIFEXITED(status):
        code = os.WEXITSTATUS(status)
        print(f"Process {pid} exited with code {code}")
        sys.exit(code)
    elif os.WIFSIGNALED(status):
        code = os.WTERMSIG(status)
        print(f"Process {pid} exited due to signal {code}")
        sys.exit(-code)
    elif os.WIFSTOPPED(status):
        code = os.WTERMSIG(status)
        print(f"Process {pid} stopped due to signal {code}")
        sys.exit(-code)
    else:
        print(f"Process {pid} exited with status {status}")
        sys.exit(status)

if __name__ == "__main__":
    main()
