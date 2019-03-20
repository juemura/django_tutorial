#!/usr/bin/env python3
from argparse import ArgumentParser
import logging

def hello1():
    ap = ArgumentParser()
    ap.add_argument('name', nargs='?')
    args = ap.parse_args()
    name = (args.name or 'World')
    print("Hello, ", name, "!")

def hello2():
    ap = ArgumentParser()
    ap.add_argument('name', nargs='?')
    args = ap.parse_args()
    name = (args.name or 'World')
    return "Hello, ", name, "!"

def hello3():
    ap = ArgumentParser()
    ap.add_argument('-v', '--verbose',
        default=False, action='store_true',
        help='Increase verbosity')
    ap.add_argument('-n', '--number',
        type=int, default=1,
        help="The number of times to greet NAME")
    ap.add_argument('name', help="The person to greet", nargs='?')
    args = ap.parse_args()
    name = (args.name or 'World')
    for _ in range(args.number):
        print("Hello,", name, "!")
    if args.verbose:
        print("I've finished now.")


def hello4():
    ap = ArgumentParser()
    ap.add_argument('-v', '--verbose',
        default=False, action='store_true',
        help='Increase verbosity')
    ap.add_argument('-n', '--number',
        type=int, default=1,
        help="The number of times to greet NAME")
    ap.add_argument('name', help="The person to greet", nargs='*')
    logging.basicConfig(level=logging.WARNING, format="%(msg)s")
    args = ap.parse_args()
    name = (args.name or 'World')
    for _ in range(args.number):
        print("Hello,", *name, "!")
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

if __name__ == '__main__':
    hello4()