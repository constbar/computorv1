#!/usr/bin/python3

import re
import sys

from equation import Eq


class Calc:
    ERR_DICT = {
        1: 'equation should have only one equal sign',
        2: 'both sides of the equation must be',
        3: 'expression must have an integer exponent',
        4: 'expression must have a non-negative exponent',
        5: 'expression can only have allowed syntax',
        6: 'it\'s just a numerical equation. no solution',
        7: 'it\'s an incorrect numerical equation. no solution',
        8: 'each real number is a solution',
    }

    REG_AFTER_X = r'([xX][^\^\-\+\=])'
    REG_NEG_EXP = r'[xX]\^(?:(?:-\d))'
    REG_FLT_EXP = r'[xX]\^(?:(?:\d*\.))'
    REG_WRG_INP = r'[^xX\d*\d*\.\d*\^\=\*\-\+]'
    REG_HGH_EXP = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^(?:(?:\d{2,})|(?:[3-9]))'

    REG_00_POL = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^0'
    REG_01_POL = r'[-+]?(?:(?:\d*\.\d*)|(?:\d+))'
    REG_1_POLY = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX](?:\^1)?'
    REG_2_POLY = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^2'

    def __init__(self, equation: str, prec: int, frac: bool = False, verb: bool = False):
        self.orig = equation
        self.check_errors()
        self.eq = Eq(self.sort_variables(), prec, frac, verb)

    @property
    def cut_input(self) -> str:
        cut_inp = self.orig
        cut_inp = cut_inp.replace('\t', '').replace(' ', '')
        return cut_inp

    def sort_variables(self) -> dict:
        """
        1. distribution of all raw data by powers
        2. cleaning, leaving only vals by degrees
        """
        left_part, right_part = self.cut_input.split('=')
        left_dict = dict()
        right_dict = dict()
        pos_exps = list(set(int(i.split('^')[-1]) for i in
                            re.findall(self.REG_HGH_EXP, self.cut_input)))

        def handle_exps(left_input: str, right_input: str) -> tuple:
            for i in pos_exps:
                reg_pos = rf'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^{i}'
                left_dict[i] = re.findall(reg_pos, left_input)
                left_input = re.sub(reg_pos, '', left_input)
                right_dict[i] = re.findall(reg_pos, right_input)
                right_input = re.sub(reg_pos, '', right_input)

            reg_list = [(2, self.REG_2_POLY), (0, self.REG_00_POL),
                        (1, self.REG_1_POLY), (0, self.REG_01_POL)]
            for e, r in reg_list:
                if e in left_dict:
                    left_dict[e].extend(re.findall(r, left_input))
                else:
                    left_dict[e] = re.findall(r, left_input)
                if e in right_dict:
                    right_dict[e].extend(re.findall(r, right_input))
                else:
                    right_dict[e] = re.findall(r, right_input)
                left_input = re.sub(r, '', left_input)
                right_input = re.sub(r, '', right_input)
            return left_input, right_input

        left_part, right_part = handle_exps(left_part, right_part)
        if len(left_part + right_part):
            sys.exit(self.ERR_DICT[5])

        def clear_vars(l_part: dict, r_part: dict) -> None:
            for k in {**l_part, **r_part}.keys():
                l_part[k] = [i.split('^')[0].lower() if '^' in i else i for i in l_part[k]]
                l_part[k] = [i.lower().replace('+', '') for i in l_part[k]]
                l_part[k] = ['1' if i == 'x' else '-1' if i == '-x' else i for i in l_part[k]]
                l_part[k] = sum(float(i.replace('*', '').replace('x', '')) for i in l_part[k])

                r_part[k] = [i.split('^')[0].lower() if '^' in i else i for i in r_part[k]]
                r_part[k] = [i.lower().replace('+', '') for i in r_part[k]]
                r_part[k] = ['1' if i == 'x' else '-1' if i == '-x' else i for i in r_part[k]]
                r_part[k] = sum(float(i.replace('*', '').replace('x', '')) for i in r_part[k])

        try:
            clear_vars(left_dict, right_dict)
        except ValueError:
            sys.exit(self.ERR_DICT[5])
        equal_sides = left_dict == right_dict
        if equal_sides and 'x' not in self.cut_input.lower():
            sys.exit(self.ERR_DICT[6])
        elif 'x' not in self.cut_input.lower():
            sys.exit(self.ERR_DICT[7])
        elif equal_sides:
            sys.exit(self.ERR_DICT[8])
        return {key: left_dict.get(key, 0) - right_dict.get(key, 0)
                for key in set(left_dict) | set(right_dict)}

    def check_errors(self) -> None:
        if self.cut_input.count('=') != 1:
            sys.exit(self.ERR_DICT[1])
        elif not all(self.cut_input.split('=')):
            sys.exit(self.ERR_DICT[2])
        elif re.findall(self.REG_FLT_EXP, self.cut_input):
            sys.exit(self.ERR_DICT[3])
        elif re.findall(self.REG_NEG_EXP, self.cut_input):
            sys.exit(self.ERR_DICT[4])
        elif re.findall(self.REG_WRG_INP, self.cut_input):
            sys.exit(self.ERR_DICT[5])
        elif re.findall(self.REG_AFTER_X, self.cut_input):
            sys.exit(self.ERR_DICT[5])
        elif re.findall(r'\^\D', self.cut_input):
            sys.exit(self.ERR_DICT[5])
        elif 'xx' in self.cut_input.lower():
            sys.exit(self.ERR_DICT[5])
