#!/usr/bin/python3

import sys
import argparse
from calculation import Calc

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='computorv1 - solves quadratic equation')
    parser.add_argument('equation',
                        type=str,
                        metavar='',
                        help='equation to solve')
    parser.add_argument('-p', '--prec',
                        type=int,
                        metavar='',
                        required=False,
                        help='precision of a solution')
    parser.add_argument('-f', '--frac',
                        action='store_true',
                        help='irreducible fraction display')
    parser.add_argument('-v', '--verb',
                        action='store_true',
                        help='verbose display')
    args = parser.parse_args()

    if args.prec is None:
        args.prec = 6
    elif args.prec < 1:
        sys.exit('precision should be more than 0')
    elif args.prec > 40:
        sys.exit(f'precision should be less than {args.prec}')
    Calc(args.equation, args.prec, args.frac, args.verb)
