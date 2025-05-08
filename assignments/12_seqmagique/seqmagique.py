#!/usr/bin/env python3
"""
Author: Samandar Jakbarov
Purpose: Calculate min/max/avg sequence lengths from FASTA files.
"""

from __future__ import annotations
import argparse
import os
import sys
from typing import List
from tabulate import tabulate


# ----------------------------------------------------------------------
def get_args() -> argparse.Namespace:
    """Parse command‑line arguments."""
    parser = argparse.ArgumentParser(
        description='Argparse Python script',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        'files',
        metavar='FILE',
        nargs='+',
        help='Input FASTA file(s)',
    )

    parser.add_argument(
        '-t',
        '--tablefmt',
        metavar='table',
        default='plain',
        help='Tabulate table style (default: plain)',
    )
    return parser.parse_args()


# ----------------------------------------------------------------------
def read_fasta(filename: str) -> List[int]:
    """Return a list of sequence lengths from one FASTA file."""
    if not os.path.isfile(filename):
        print(
            'usage: seqmagique.py [-h] [-t table] FILE [FILE ...]',
            file=sys.stderr,
        )
        print(f"No such file or directory: '{filename}'", file=sys.stderr)
        sys.exit(1)

    lens: List[int] = []
    seq = ''
    with open(filename, encoding='utf-8') as fh:
        for line in fh:
            line = line.rstrip()
            if line.startswith('>'):
                if seq:
                    lens.append(len(seq))
                    seq = ''
            else:
                seq += line
        if seq:
            lens.append(len(seq))
    return lens


# ----------------------------------------------------------------------
def clean_path(path: str) -> str:
    """
    Convert e.g. './tests/inputs/1.fa' → 'inputs/1.fa'.
    Works on Windows and POSIX paths.
    """
    return (
        os.path.normpath(path)
        .replace('\\', '/')
        .replace('tests/inputs/', 'inputs/')
        .replace('./inputs/', 'inputs/')
        .lstrip('./')
    )


# ----------------------------------------------------------------------
def main() -> None:
    """Parse args, summarize each FASTA, and print the table."""
    args = get_args()
    headers = ['name', 'min_len', 'max_len', 'avg_len', 'num_seqs']
    rows: list[list[str | int | float]] = []

    for fname in args.files:
        lens = read_fasta(fname)
        num = len(lens)
        min_len = min(lens) if lens else 0
        max_len = max(lens) if lens else 0
        avg_len = sum(lens) / num if lens else 0

        rows.append(
            [
                clean_path(fname),
                min_len,
                max_len,
                f'{avg_len:.2f}',  # always two decimal places
                num,
            ]
        )

    rows.sort()
    print(tabulate(rows, headers=headers, tablefmt=args.tablefmt))


# ----------------------------------------------------------------------
if __name__ == '__main__':
    main()
