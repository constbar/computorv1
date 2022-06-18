#!/usr/bin/python3

import argparse
import sys

from calculation import Calc

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='computorv1 - solves quadratic equation')
    parser.add_argument('equation', type=str,
                        help='polynom to process')
    parser.add_argument('-p', '--prec',
                        type=int, required=False,
                        help='set the accuracy of the solution')
    parser.add_argument('-f', '--frac', action='store_true',
                        help='show irreducible fraction')
    parser.add_argument('-v', '--verb', action='store_true',
                        help='show detail operations')
    args = parser.parse_args()

    if args.prec is None:
        args.prec = 6
    elif args.prec < 1:
        sys.exit('precision should be more than 0')
    elif args.prec > 40:
        sys.exit(f'precision should be less than {args.prec}')
    Calc(args.equation, args.prec, args.frac, args.verb)
