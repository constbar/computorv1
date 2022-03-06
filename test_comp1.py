#!/usr/bin/python3

import os
import time
from random import randint
from calculation import Calc
from termcolor import colored

equations = [
    '8.76x + 2.9x = 8.2', 'random string',
    '2 * X^1 + X^2 = 0', '5 * X^0 = 5 * X^0',
    '3x^2 - 4x + 2 = 0', '2 * X^0 = 8 * X^0',
    'X^2 + 2 + 3 * X^1 = 3', '0x^2 + 4x = 2',
    'X^-2 + 2 + 3 * X^1 = 3', '2X^2 = x + 3',
    'X^2 + 4 + 2 * X^1 = 3', '2x^2 - 3x = -1',
    '2x^2 -22x - 1 = 0', '1 + x^20= x^20 + 1',
    'X^2 + 2 * X^1 = -1', 'X^3 + 2 - X^1 = 3',
    '+ X^2 + 2 + 3 * X^1 = 3', 'X^2 - 16 = 0',
    '13x^23 + 1 = 1 + 13*x^23', '3X ^ 2 = 2x',
    '2 + X = X - 3 = X^2', '5 * X^2 = 1 * X^0',
    '2x^2 + 1x + 200 = 0', '5*X^0=4*X^0+7*X^1',
    'X^2 -6 * X^1 + 5 = 0', 'error = solution',
    'X^2 -6 * X^1 + 13 = 0', '3x^2 -3- 5x = 0',
    'Y^2 + 2 + 3 * X^1 = 0', '2x^2 - 13x = -1',
    '5 + 4 * X + X^2 = X^2', 'x^2 -6x + 9 = 0',
    '12.132888x^2 + 2x = + 1212', '8x + 2x = 8',
    'x^2 + 4x + x + 2 = 0 + x^2', '4*X^0=8*X^0',
    '2X^2 - 123x = x + 41', '3x^2 - 6x + 1 = 0',
    '42x^2 + x^2 + 1 = 1 + 42x^2', 'x - 47 = 0',
    '5 * X^0 = 4 * X^0 + 7 * X^1', '1 +- X = 3',
    '5 * x^0 + 4 * x^1 = 4 * x^0', '1 +* X = 3',
    '22x^2 + 123 -1 = 22x^2 - 1', 'X^2 + 16 = 0',
    '2.2x^2 - 3.3x^1 - 22.2 = 0',  '7*X^0=7*X^0',
    'X - X = 00000000000000000003', '^2 + X = 0',
    '1 * X  + 2 * X^1 + X - X = 3', 'x + 23 = 0',
    '5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0', '=',
    '+3x^2 + 3x^2-3x^2  - 4x + 22.21 =  ', '4x = 1',
    '22x^2 + 33.2x + 1.213 = 3x^2 + 32', '1 * X = 3',
    '+3x^2 + 3x^2-3x^2.2 - 4x + 22 = 123', '4x = 12',
    '+3x^2 + 3x^2-3x^-2 - 4x + 22.21 = 2', '10 = 10',
    '+3x^2 + 3x^2-3x^2 - 4x + 22.21 =  =', 'X^2 = 0',
    '+ 3.2x^2 - 4.3 + 1 + x^99= 2x + 4x^123 + 1x^99',
    '+3x^2 + 3x^2-3x^2 - 4x + 22.21 = 2', 'X + 1 = 0',
    '5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1',
    '5 * X^0 + 4 * X^1 - 9.443 * X^2 = 1 * X^0 - 312',
    '+3x^25 + 3x^2-3x^22 -4x + 22.21 = 3', '2 = 1', '',
    '6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1',
    '5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1',
    '6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1',
    '8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0',
    '32 + 3 + 00000001.000000000 = 04.0000000000000000\
    0000', '8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = \
    3 * X^0  - 5.6 * X^3', '8 * X^0 - 6 * X^1 + 0 * X^\
    2 + 10.6 * X^3 = 3 * X^0  - 5.6 * X^3', 'x^2 = 120\
    93494324111111155555555555555555555588888888888888\
    88888888888888888888888888888888888888888888888888\
    88888888888888884444444444444444444412344444444444\
    4444444444444444444444444444444444444444', 'input',
    '-x - 3X^20 - 3x^4 + 2x^2 + 9x^54 + 4x^1 - 32x^7 +\
    x + 2x + 2 = 0 - 4 - 13x^23', '-333.123 - 22.123x\
    ^2 + 32.x^2 - 23.X^7 + 33.5x^4 + 4X^3 + 20x^3 + 1\
    - x^5 = 4X^2'
]

if __name__ == '__main__':
    # for i in range(len(equations)):
    l = randint(0, len(equations))
    print('original equation:', colored(equations[l], 'cyan'))
    os.system(f"python3 computorv1.py '{equations[l]}' -f ")
    time.sleep(1)
