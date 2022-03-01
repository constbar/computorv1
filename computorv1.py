#!/usr/bin/python3

# if empty input -> can arg parse work with it
# make my_sum function
# можно по параметру сделать точность по заяпятой - если хочешь округление до 6 - пиши 6 или 7
# прокомментить все функции
# change chmod here
# ubrat' vse prints
# 3x^+4 - postavit' reg ex na esli ne chislo posle ^

import re
import sys
from equation import Eq
from termcolor import colored


class Comp:
    ERR_DICT = {
        1: 'equation should have only one equal sign',
        2: 'both sides of the equation must be',
        3: 'expression must have an integer exponent',
        4: 'expression must have a non-negative exponent',
        5: 'expression can only have allowed syntax',
        6: 'its just a numerical equation. no solution',
        7: 'its an incorrect numerical equation. no solution',
        8: 'each real number is a solution',
        9: 'the polynomial degree is strictly greater than 2'
    }

    REG_NEG_EXP = r'[xX]\^(?:(?:-\d))'
    REG_FLT_EXP = r'[xX]\^(?:(?:\d*\.))'
    REG_WRG_INP = r'[^xX\d*\d*\.\d*\^\=\*\-\+]'
    # REG_HGH_EXP = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^(?:[3-9]|\d{2,})'
    REG_HGH_EXP = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^(?:(?:\d{2,})|(?:[3-9]))'

    REG_00_POL = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^0'
    REG_01_POL = r'[-+]?(?:(?:\d*\.\d*)|(?:\d+))'
    REG_1_POLY = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX](?:\^1)?'
    REG_2_POLY = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^2'

    def __init__(self, equation: str, extend_param=None):
        self.orig = equation
        self.cin = self.cutted_input
        self.check_input()
        # print(self.cin)

        self.raw_lists = self.sort_variables
        # print(f'raw list: {self.raw_lists}')

        # here we should send clear vars
        self.eq = Eq(self.convert_variables(self.raw_lists))

        # and send teur or false for extend flag
        self.eq.print_result(self.raw_lists)

    @property
    def cutted_input(self) -> str:
        cut_inp = self.orig
        cut_inp = cut_inp.replace('\t', '').replace(' ', '')
        return cut_inp

    @property
    def sort_variables(self) -> tuple:
        '''
        1. 
        '''
        left_part, right_part = self.cin.split('=')
        left_dict = dict()
        right_dict = dict()
        pos_exps = [int(i.split('^')[-1]) for i in
                    re.findall(self.REG_HGH_EXP, self.cin)]
        print(pos_exps)
        def handle_exps(left_input: str, right_input: str):  # -> #
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
        print(left_part, right_part)
        print(colored(left_dict, 'cyan'))
        print(colored(right_dict, 'red'))

        if len(left_part) != 0 or len(right_part) != 0:
            self.end_eq(5)

        def clear_vars(l_part: dict, r_part: dict) -> None:
            for k in {**l_part, **r_part}.keys():
                l_part[k] = [i.split('^')[0].lower() if '^' in i else i for i in l_part[k]]
                l_part[k] = [i.strip('+') for i in l_part[k]]
                l_part[k] = ['1' if i == 'x' else '-1' if i == '-x' else i for i in l_part[k]]
                l_part[k] = sum(float(i.strip('x')) for i in l_part[k])

                r_part[k] = [i.split('^')[0].lower() if '^' in i else i for i in r_part[k]]
                r_part[k] = [i.strip('+') for i in r_part[k]]
                r_part[k] = ['1' if i == 'x' else '-1' if i == '-x' else i for i in r_part[k]]
                r_part[k] = -1 * sum(float(i.strip('x')) for i in r_part[k])


        # Sravnenie dictov
        # esli tol'ko ^0 -> else sfjskadfjsdklfj
        # left_part, right_part = handle_exps(left_part, right_part) # check if equals
        clear_vars(left_dict, right_dict)
        print(left_dict)
        print(right_dict)

        sys.exit(3)
        # check here
        if equal_sides and not 'x' in self.cin.lower():
            self.end_eq(6) # просто поставить сис эксит
        elif 'x' not in self.cin.lower():
            self.end_eq(7)
        elif equal_sides:
            self.end_eq(8)
        # return dict
        return (list_x0, list_x1, list_x2) + tuple(list_high)


    # need i this method?
    @staticmethod
    def convert_variables(conv_list: tuple) -> tuple:
        def get_sum(exp_list: list, exponent: int) -> float:
            # make lower()
            fin_list = [i.replace('X', 'x').replace(f'^{exponent}', '') for i in exp_list]
            fin_list = ['1' if i == 'x' else '-1' if i == '-x' else i for i in fin_list]
            return sum(map(float, (i.replace('*x', '').replace('x', '') for i in fin_list)))

        total = tuple(get_sum(conv_list[i], i) for i in range(len(conv_list)))
        return total

    def check_input(self) -> None: # rename check errors
        if self.cin.count('=') != 1:
            sys.exit(self.ERR_DICT[1])
        elif not all(self.cin.split('=')):
            sys.exit(self.ERR_DICT[2])
        elif re.findall(self.REG_FLT_EXP, self.cin):
            sys.exit(self.ERR_DICT[3])
        elif re.findall(self.REG_NEG_EXP, self.cin):
            sys.exit(self.ERR_DICT[4])
        elif re.findall(self.REG_WRG_INP, self.cin):
            sys.exit(self.ERR_DICT[5])
        elif 'xx' in self.cin.lower():
            sys.exit(self.ERR_DICT[5])

        # self.end_eq(2) if not all(self.cin.split('=')) else None
        # self.end_eq(3) if re.findall(self.REG_FLT_EXP, self.cin) else None
        # self.end_eq(4) if re.findall(self.REG_NEG_EXP, self.cin) else None
        # self.end_eq(5) if re.findall(self.REG_WRG_INP, self.cin) else None
        # self.end_eq(5) if 'xx' in self.cin.lower() else None

    @classmethod
    def end_eq(cls, num_err: int, err_msg: str = None) -> None:
        print(cls.ERR_DICT[num_err])
        # if num_err == 9:
            # print(f'the program doesnt handle {err_msg} exponent')
        # sys.exit(num_err)
