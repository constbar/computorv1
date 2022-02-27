#!/usr/bin/python3

# if empty input -> can arg parse work with it
# make my_sum function
# можно по параметру сделать точность по заяпятой - если хочешь округление до 6 - пиши 6 или 7
# прокомментить все функции
# change chmod here
# ubrat' vse prints

import re
import sys
from equation import Eq
from termcolor import colored


class Comp:
    ERR_DICT = {
        1: 'equation should have only one equal sign',
        2: 'both sides of the equation must be',
        3: 'expression musst have a integer exponent',
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
    REG_HGH_EXP = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^(?:[3-9]|\d{2,})'
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

        def check_equal_sides(ch_left: str, ch_right: str):  # ->
            reg_list = [self.REG_HGH_EXP, self.REG_2_POLY,
                        self.REG_00_POL, self.REG_1_POLY, self.REG_01_POL]
            left_list = list()
            right_list = list()
            for i in reg_list:
                left_list.extend(re.findall(i, ch_left))
                ch_left = re.sub(i, '', ch_left)
                right_list.extend(re.findall(i, ch_right))
                ch_right = re.sub(i, '', ch_right)
            left_list = sorted(i.lower().replace('+', '') for i in left_list)
            right_list = sorted(i.lower().replace('+', '') for i in right_list)
            return left_list == right_list

        # high_exp = re.findall(self.REG_HGH_EXP, left_part + '+' + right_part)
        equal_sides = check_equal_sides(left_part, right_part)        

        if equal_sides and not 'x' in self.cin.lower():
            self.end_eq(6)
        elif 'x' not in self.cin.lower():
            self.end_eq(7)
        elif equal_sides:
            self.end_eq(8)

        def make_clear_vars(reg: str, l_part: str, r_part: str) -> tuple:
            ret_list = list()
            ret_list.extend(re.findall(reg, l_part))
            l_part = re.sub(reg, '', l_part)

            ret_list = [i.replace('+', '') for i in ret_list]
            temp = ['-' + i for i in re.findall(reg, r_part)]
            ret_list.extend([i.replace('-+', '-').replace('--', '') for i in temp])
            r_part = re.sub(reg, '', r_part)
            return (ret_list, l_part, r_part)

        high_exp_list, left_part, right_part = make_clear_vars(
            self.REG_HGH_EXP, left_part, right_part)        
        list_high = list()
        if high_exp_list:
            high_str = '+'.join(high_exp_list).replace('+-', '-')
            high_str = '+' + high_str if high_str[0] != '-' else high_str
            max_exp = max(list(set(i.split('^')[-1] for i in high_exp_list)))
            for i in range(3, int(max_exp) + 1):
                reg_inc = rf'[-]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^{i}'
                list_high.append(re.findall(reg_inc, high_str))
                high_str = re.sub(reg_inc, '', high_str)

        list_x2, left_part, right_part = make_clear_vars(
            self.REG_2_POLY, left_part, right_part)
        list_x0, left_part, right_part = make_clear_vars(
            self.REG_00_POL, left_part, right_part)
        list_x1, left_part, right_part = make_clear_vars(
            self.REG_1_POLY, left_part, right_part)
        tmp_lst, left_part, right_part = make_clear_vars(
            self.REG_01_POL, left_part, right_part)
        self.end_eq(5) if len(left_part) != 0 or len(
            right_part) != 0 else None
        list_x0.extend(tmp_lst)

        return (list_x0, list_x1, list_x2) + tuple(list_high)

    @staticmethod
    def convert_variables(conv_list: tuple) -> tuple:
        def get_sum(exp_list: list, exponent: int) -> float:
            fin_list = [i.replace('X', 'x').replace(f'^{exponent}', '') for i in exp_list] # make lower()
            fin_list = ['1' if i == 'x' else '-1' if i == '-x' else i for i in fin_list]
            return sum(map(float, (i.replace('*x', '').replace('x', '') for i in fin_list)))

        total = tuple(get_sum(conv_list[i], i) for i in range(len(conv_list)))
        return total

    def check_input(self) -> None:
        self.end_eq(1) if self.cin.count('=') != 1 else None
        self.end_eq(2) if not all(self.cin.split('=')) else None
        self.end_eq(3) if re.findall(self.REG_FLT_EXP, self.cin) else None
        self.end_eq(4) if re.findall(self.REG_NEG_EXP, self.cin) else None
        self.end_eq(5) if re.findall(self.REG_WRG_INP, self.cin) else None
        self.end_eq(5) if 'xx' in self.cin.lower() else None

    @classmethod
    def end_eq(cls, num_err: int, err_msg: str=None) -> None:
        print(cls.ERR_DICT[num_err])
        if num_err == 9:
            print(f'the program doesnt handle {err_msg} exponent')
        sys.exit(num_err)
