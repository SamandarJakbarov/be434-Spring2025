#!/usr/bin/env python3
"""
Author:Samandar Jakbarov
Purpose: Find common words between two files
"""

import argparse
import os
import sys


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Find common words',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('file1',
                        metavar='FILE1',
                        help='Input file 1',
                        type=arg_readable_file)

    parser.add_argument('file2',
                        metavar='FILE2',
                        help='Input file 2',
                        type=arg_readable_file)

    parser.add_argument('-o',
                        '--outfile',
                        help='Output file',
                        metavar='FILE',
                        type=argparse.FileType('wt'),
                        default=sys.stdout)

    return parser.parse_args()


def arg_readable_file(filename):
    """Check if file exists and is readable"""
    if not os.path.isfile(filename):
        raise argparse.ArgumentTypeError(
            f"can't open '{filename}': No such file or directory"
        )
    return open(filename, 'rt', encoding='utf-8')


def get_words(filehandle):
    """Read filehandle and return a set of words"""
    words = set()
    for line in filehandle:
        words.update(line.split())
    return words


def main():
    """Main program"""
    args = get_args()

    words1 = get_words(args.file1)
    words2 = get_words(args.file2)

    common = sorted(words1 & words2)

    for word in common:
        print(word, file=args.outfile)


if __name__ == '__main__':
    main()
