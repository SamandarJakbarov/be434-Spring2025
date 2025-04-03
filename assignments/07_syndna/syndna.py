#!/usr/bin/env python3
"""
Create synthetic DNA or RNA sequences
"""

import argparse
import random


def get_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Create synthetic sequences')

    parser.add_argument('-o', '--outfile',
                        type=argparse.FileType('wt'),
                        default='out.fa',
                        help='Output filename (default: out.fa)')
    parser.add_argument('-t', '--seqtype',
                        type=str,
                        choices=['dna', 'rna'],
                        default='dna',
                        help='DNA or RNA (default: dna)')
    parser.add_argument('-n', '--numseqs',
                        type=int,
                        default=10,
                        help='Number of sequences to create (default: 10)')
    parser.add_argument('-m', '--minlen',
                        type=int,
                        default=50,
                        help='Minimum length (default: 50)')
    parser.add_argument('-x', '--maxlen',
                        type=int,
                        default=75,
                        help='Maximum length (default: 75)')
    parser.add_argument('-p', '--pctgc',
                        type=float,
                        default=0.5,
                        help='Percent GC (default: 0.5)')
    parser.add_argument('-s', '--seed',
                        type=int,
                        default=None,
                        help='Random seed (default: None)')

    args = parser.parse_args()

    if not 0 < args.pctgc < 1:
        parser.error(f'--pctgc "{args.pctgc}" must be between 0 and 1')

    return args


def create_pool(pctgc, max_len, seq_type):
    """Create the pool of bases"""
    t_or_u = 'T' if seq_type == 'dna' else 'U'
    num_gc = int((pctgc / 2) * max_len)
    num_at = int(((1 - pctgc) / 2) * max_len)

    pool = 'A' * num_at + 'C' * num_gc + 'G' * num_gc + t_or_u * num_at

    for _ in range(max_len - len(pool)):
        pool += random.choice(pool)

    return ''.join(sorted(pool))


def main():
    args = get_args()
    random.seed(args.seed)

    pool = create_pool(args.pctgc, args.maxlen, args.seqtype)

    for i in range(1, args.numseqs + 1):
        seq_len = random.randint(args.minlen, args.maxlen)
        seq = ''.join(random.sample(pool, seq_len))
        args.outfile.write(f'>{i}\n{seq}\n')

    args.outfile.close()
    print(f'Done, wrote {args.numseqs} {args.seqtype.upper()} sequences '
      f'to "{args.outfile.name}".')


if __name__ == '__main__':
    main()
