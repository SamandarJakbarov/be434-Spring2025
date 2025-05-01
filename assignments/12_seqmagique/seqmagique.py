#!/usr/bin/env python3
"""
Author: Samandar Jakbarov
Purpose: Calculate min/max/avg seq lengths from FASTA files
"""

import argparse
import os
import sys
from typing import List
from tabulate import tabulate


def get_args() -> argparse.Namespace:
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('files',
                        metavar='FILE',
                        type=str,
                        nargs='+',
                        help='Input FASTA file(s)')
    parser.add_argument('-t',
                        '--tablefmt',
                        metavar='table',
                        default='plain',
                        help='Tabulate table style')
    return parser.parse_args()


def read_fasta(filename: str) -> List[int]:
    """Return list of sequence lengths in a FASTA file"""

    if not os.path.isfile(filename):
        print("usage: seqmagique.py [-h] [-t table] FILE [FILE ...]", file=sys.stderr)
        print(f"No such file or directory: '{filename}'", file=sys.stderr)
        sys.exit(1)

    lens = []
    seq = ''

    with open(filename, encoding='utf-8') as fh:
        for line in fh:
            line = line.strip()
            if line.startswith('>'):
                if seq:
                    lens.append(len(seq))
                    seq = ''
            else:
                seq += line
        if seq:
            lens.append(len(seq))

    # Ensure it returns an empty list if no sequences found (e.g., empty file)
    return lens



def main():
    """Main logic"""

    args = get_args()
    headers = ['name', 'min_len', 'max_len', 'avg_len', 'num_seqs']
    rows = []

    for file in args.files:
        lengths = read_fasta(file)
        num_seqs = len(lengths)
        min_len = min(lengths) if lengths else 0
        max_len = max(lengths) if lengths else 0
        avg_len = sum(lengths) / num_seqs if lengths else 0

        # Exactly this line:
        rows.append([file, min_len, max_len, f'{avg_len:.2f}', num_seqs])


    print(tabulate(rows, headers=headers, tablefmt=args.tablefmt))


if __name__ == '__main__':
    main()
