#!/usr/bin/env python3
"""
Author : Samandar Jakbarov <samandarjakbarov@arizona.edu>
Date   : 2025-02-12
Purpose: Print reeting
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description="Greetings and howdy",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )

    parser.add_argument(
        "-g",
        "--greeting",
        help="The greeting",
        metavar="str",
        type=str,
        default="Howdy",
    )

    parser.add_argument(
        "-n",
        "--name",
        help="Whom to greet",
        metavar="str",
        type=str,
        default="Stranger",
    )

    parser.add_argument(
        "-e",
        "--excited",
        help="If this flag is used, then print !",
        action="store_true",
    )

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    greeting = args.greeting
    name = args.name
    excited = args.excited

    if excited:
        print(f"{greeting}, {name}!")
    else:
        print(f"{greeting}, {name}.")


# --------------------------------------------------
if __name__ == "__main__":
    main()
