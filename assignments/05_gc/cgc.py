#!/usr/bin/env python3
"""
Author: Samandar Jakbarov
Purpose: Reverse Complement DNA Assignment
"""

import argparse
import sys


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description="Compute GC content",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file',
                        metavar='FILE',
                        help='Input sequence file',
                        type=argparse.FileType('rt'),
                        nargs='?',
                        default=sys.stdin)

    return parser.parse_args()


def read_fasta(fh):
    """Parse a FASTA file and return a dict of {ID: sequence}"""
    sequences = {}
    seq_id = ''
    seq_lines = []

    for line in fh:
        line = line.strip()
        if line.startswith('>'):
            if seq_id:
                sequences[seq_id] = ''.join(seq_lines)
            seq_id = line[1:]
            seq_lines = []
        else:
            seq_lines.append(line)

    if seq_id:
        sequences[seq_id] = ''.join(seq_lines)

    return sequences


def gc_content(seq):
    """Return GC content percentage"""
    gc = sum(1 for base in seq if base in 'GCgc')
    return 100 * gc / len(seq)


def main():
    """Main function"""
    args = get_args()
    sequences = read_fasta(args.file)

    if not sequences:
        sys.exit('No sequences found')

    best_id, best_gc = max(
        ((id_, gc_content(seq)) for id_, seq in sequences.items()),
        key=lambda x: x[1])

    print(f'{best_id} {best_gc:.6f}')


if __name__ == '__main__':
    main()
