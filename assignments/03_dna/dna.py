#!/usr/bin/env python3
"""
Author : Samandar Jakbarov
Date   : 2025-03-03
Purpose: Add You
"""

import argparse
import sys


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Tetranucleotide frequency',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('DNA',
                        metavar='DNA',
                        nargs='?',
                        help='Input DNA sequence')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Compute tetranucleotide frequency"""

    args = get_args()
    dna_seq = args.DNA
    if dna_seq is None:
        dna_seq = sys.stdin.read().strip()

    if not dna_seq:
        print('usage: dna.py [-h] DNA', file=sys.stderr)
        sys.exit(1)

    a_count = dna_seq.count('A')
    c_count = dna_seq.count('C')
    g_count = dna_seq.count('G')
    t_count = dna_seq.count('T')

    print(a_count, c_count, g_count, t_count)


# --------------------------------------------------
if __name__ == '__main__':
    main()
