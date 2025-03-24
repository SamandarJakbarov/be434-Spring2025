#!/usr/bin/env python3
"""
Author: Samandar Jakbarov
Purpose: Reverse Complement DNA Assignment
"""

import argparse
import os


def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Print the reverse complement of DNA')
    parser.add_argument('DNA',
                        metavar='DNA',
                        help='Input sequence or file')

    return parser.parse_args()


def reverse_complement(seq):
    """Return reverse complement of a DNA sequence"""

    complement = {
        'A': 'T', 'T': 'A',
        'C': 'G', 'G': 'C',
        'a': 't', 't': 'a',
        'c': 'g', 'g': 'c'
    }

    rev_comp = ''.join(complement.get(base, base) for base in reversed(seq))
    return rev_comp


def main():
    """Main program logic"""
    args = get_args()
    dna_input = args.DNA

    # Check if input is a file
    if os.path.isfile(dna_input):
        with open(dna_input, 'rt', encoding='utf-8') as fh:
            dna_seq = fh.read().strip()
    else:
        dna_seq = dna_input.strip()

    print(reverse_complement(dna_seq))


if __name__ == '__main__':
    main()
