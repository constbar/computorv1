#!/usr/bin/python3

# степень не омжет быть с - или дробным числом
# if no right or no left -> part shold not be empty
# if empty input -> can arg parse work with it
# manage delenie na 0
# esli otvet celoe chislo -> vivod lkak int
# rename na compv1 not main.py
# проверка на несколько xXxxXXXxx
# flag full shows all strings -v 'x^2  + 2 = 0' - dima expample
# make my sum function
# можно по параметру сделать точность по заяпятой - если хочешь округление до 6 - пиши 6 или 7

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
        5: 'expression can only have allowed syntax'

        # : 'equation could not be solved, invalid syntax'
        # 5: 'expression must have a valid exponent [0, 1, 2]',
    }

    REG_NEG_EXP = r'[xX]\^(?:(?:-\d))'
    REG_FLT_EXP = r'[xX]\^(?:(?:\d*\.))'
    REG_WRG_INP = r'[^xX\d*\d*\.\d*\^\=\*\-\+]'
    REG_HGH_EXP = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^(?:[3-9]|\d{2,})'
    # REG_HGH_EXP = r'[xX]\^(?:(?:\d{2,})|(?:[3-9]))'

    REG_00_POL = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^0'
    REG_01_POL = r'[-+]?(?:(?:\d*\.\d*)|(?:\d+))'
    REG_1_POLY = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX](?:\^1)?'
    REG_2_POLY = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^2'

    def __init__(self, equation: str, extend_param=None):
        self.orig = equation
        self.cin = self.cutted_input
        self.check_input()
        print(self.cin)

        self.raw_lists = self.sort_variables
        print(f'raw list: {self.raw_lists}')

        self.eq = Eq(self.convert_variables)

        # simple reduced form
        # bonus reduced form

    @property
    def cutted_input(self) -> str:
        cut_inp = self.orig
        cut_inp = cut_inp.replace('\t', '').replace(' ', '')
        return cut_inp

    def check_input(self) -> None:
        self.error_func(1) if self.cin.count('=') != 1 else None
        self.error_func(2) if not all(self.cin.split('=')) else None
        self.error_func(3) if re.findall(self.REG_FLT_EXP, self.cin) else None
        self.error_func(4) if re.findall(self.REG_NEG_EXP, self.cin) else None
        self.error_func(5) if re.findall(self.REG_WRG_INP, self.cin) else None
        self.error_func(5) if 'xx' in self.cin.lower() else None

        # 2. in other time -> shold show first polynom that doesnt match
        # self.error_func(5) if re.findall(self.REG_HIGH_EXPONENT, self.cin) else None

    @property
    def sort_variables(self) -> tuple:
        left_part, right_part = self.cin.split('=')

        # 2. потом проверка что полином больше 2х
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
            
            print(left_list)
            print(right_list)


            sys.exit() #

        check_equal_sides(left_part, right_part)

        def make_clear_vars(reg: str, l_part: str, r_part: str) -> tuple:
            ret_list = list()
            ret_list.extend(re.findall(reg, l_part))
            l_part = re.sub(reg, '', l_part)
            ret_list = [i.replace('+', '') for i in ret_list]

            temp = ['-' + i for i in re.findall(reg, r_part)]
            ret_list.extend([i.replace('-+', '-').replace('--', '')
                             for i in temp])
            r_part = re.sub(reg, '', r_part)
            return (ret_list, l_part, r_part)

        list_x2, left_part, right_part = make_clear_vars(
            self.REG_2_POLY, left_part, right_part)
        list_x0, left_part, right_part = make_clear_vars(
            self.REG_00_POL, left_part, right_part)
        list_x1, left_part, right_part = make_clear_vars(
            self.REG_1_POLY, left_part, right_part)
        tmp_lst, left_part, right_part = make_clear_vars(
            self.REG_01_POL, left_part, right_part)
        #
        self.error_func(5) if len(left_part) != 0 or len(
            right_part) != 0 else None
        list_x0.extend(tmp_lst)
        return (list_x0, list_x1, list_x2)

    @property
    def convert_variables(self) -> tuple:
        def get_sum(exp_list: list, exponent: int) -> float:
            fin_list = [i.replace('X', 'x').replace(f'^{exponent}', '') for i in exp_list]
            fin_list = ['1' if i == 'x' else '-1' if i ==
                        '-x' else i for i in fin_list]
            return sum(map(float, (i.replace('*x', '').replace('x', '') for i in fin_list)))
        total = tuple(get_sum(self.raw_lists[i], i)
                      for i in range(len(self.raw_lists)))
        return total

    def finall_output():
        pass

    @classmethod
    def error_func(cls, num_err) -> None:
        # esli oshibka to dolzhni vivodit' Polynom i procchee
        # text could be directly in sys.exit
        print(colored(cls.ERR_DICT[num_err], 'red'))
        sys.exit(num_err)
