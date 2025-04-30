#!/usr/bin/env python3
"""
Author: Samandar Jakbarov
Purpose: Annotate BLAST output by merging with metadata
"""

import argparse
import os
import sys
import pandas as pd


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(description='Annotate BLAST output')
    parser.add_argument(
        '-b', '--blasthits', metavar='FILE', required=True,
        help='BLAST -outfmt 6')
    parser.add_argument(
        '-a', '--annotations', metavar='FILE', required=True,
        help='Annotations file')
    parser.add_argument(
        '-o', '--outfile', metavar='FILE', default='out.csv',
        help='Output file')
    parser.add_argument(
        '-d', '--delimiter', metavar='DELIM', default=None,
        help='Output field delimiter')
    parser.add_argument(
        '-p', '--pctid', metavar='PCTID', type=float, default=0.0,
        help='Minimum percent identity')
    return parser.parse_args()


def guess_delimiter(filename):
    """Guess delimiter based on file extension"""
    ext = os.path.splitext(filename)[1].lower()
    return '\t' if ext in ['.tsv', '.tab', '.txt'] else ','


def main():
    """Main function to parse, filter, and merge BLAST with annotations"""
    args = get_args()
    blast_file = args.blasthits
    ann_file = args.annotations
    outfile = args.outfile
    pctid = args.pctid

    if not os.path.isfile(blast_file):
        print(f"No such file or directory: '{blast_file}'")
        sys.exit(1)

    if not os.path.isfile(ann_file):
        print(f"No such file or directory: '{ann_file}'")
        sys.exit(1)

    if args.delimiter in [',', '\t']:
        delim = args.delimiter
    else:
        if args.delimiter:
            print(
                f'Warning: Invalid delimiter "{args.delimiter}", '
                'using guessed value'
            )
        delim = guess_delimiter(blast_file)

    blast_cols = ['qseqid', 'sseqid', 'pident', 'length', 'mismatch',
                  'gapopen', 'qstart', 'qend', 'sstart', 'send',
                  'evalue', 'bitscore']
    blast_df = pd.read_csv(blast_file, sep=delim, names=blast_cols)
    ann_df = pd.read_csv(ann_file)

    filtered = blast_df[blast_df['pident'] >= pctid]
    merged = filtered.merge(ann_df, left_on='qseqid', right_on='seq_id')

    if args.delimiter in [',', '\t']:
        output_delim = args.delimiter
    else:
        output_delim = guess_delimiter(outfile)

    merged[['qseqid', 'pident', 'depth', 'lat_lon']].to_csv(
        outfile, index=False, sep=output_delim)

    print(f'Exported {len(merged)} to "{outfile}".')


if __name__ == '__main__':
    main()
