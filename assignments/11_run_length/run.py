#!/usr/bin/env python3
"""
Run-length encoding of DNA sequences
"""

import argparse
import os


def get_args():
    """Get command-line arguments"""
    parser = argparse.ArgumentParser(
        description='Run-length encoding/data compression')
    parser.add_argument('text', help='DNA text or file')
    args = parser.parse_args()

    if os.path.isfile(args.text):
        with open(args.text, encoding='utf-8') as f:
            args.text = f.read().rstrip()
    return args


def rle(seq):
    """Run-length encode a sequence"""
    if not seq:
        return ''
    result = []
    count = 1
    for i in range(1, len(seq)):
        if seq[i] == seq[i - 1]:
            count += 1
        else:
            result.append(seq[i - 1] + (str(count) if count > 1 else ''))
            count = 1
    result.append(seq[-1] + (str(count) if count > 1 else ''))
    return ''.join(result)


def main():
    """Main function"""
    args = get_args()
    for seq in args.text.splitlines():
        print(rle(seq))


def test_rle():
    """Test the rle function"""
    assert rle('A') == 'A'
    assert rle('ACGT') == 'ACGT'
    assert rle('AA') == 'A2'
    assert rle('AAAAA') == 'A5'
    assert rle('ACCGGGTTTT') == 'AC2G3T4'


if __name__ == '__main__':
    main()
