#!/usr/bin/env python3
"""
Author: Ken Youens-Clark <kyclark@gmail.com>
Purpose: Find conserved bases
"""

import argparse
import os
import sys


def get_args():
    parser = argparse.ArgumentParser(description='Find conserved bases')
    parser.add_argument('FILE', help='Input file')

    args = parser.parse_args()

    if not os.path.isfile(args.FILE):
        parser.error(f"No such file or directory: '{args.FILE}'")

    return args


def main():
    args = get_args()

    with open(args.FILE) as f:
        seqs = [line.strip() for line in f if line.strip()]

    for seq in seqs:
        print(seq)

    consensus = ''
    for chars in zip(*seqs):
        if all(base == chars[0] for base in chars):
            consensus += '|'
        else:
            consensus += 'X'

    print(consensus)


if __name__ == '__main__':
    main()
