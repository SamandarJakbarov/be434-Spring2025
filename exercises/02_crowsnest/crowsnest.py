#!/usr/bin/env python3
"""
Author : Samandar Jakbarov
Date   : 2025-02-17
Purpose: Finish it  
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Add Your Purpose',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
                        metavar='object',
                        help='the thing we see')
                    
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    word = args.word 
    article = 'an' if word[0].lower() in 'aeiou' else 'a'
                        
    print(f"Ahoy, Captain, {article} {word} off the larboard bow!")

# --------------------------------------------------
if __name__ == '__main__':
    main()
