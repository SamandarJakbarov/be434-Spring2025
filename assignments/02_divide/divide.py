#!/usr/bin/env python3
"""
Author: Ken Youens-Clark <kyclark@arizona.edu>
Purpose: Divide two integers
"""

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(description='Divide two numbers')
    parser.add_argument('INT', nargs=2, type=int, help='Numbers to divide')

    try:
        args = parser.parse_args()
    except SystemExit as e:
        sys.exit(e.code)

    num1, num2 = args.INT

    if num2 == 0:
        parser.error('Cannot divide by zero, dum-dum!')

    print(f'{num1} / {num2} = {num1 // num2}')

if __name__ == '__main__':
    main()
