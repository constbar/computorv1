#!/usr/bin/python3
# при конвертации в инт если не получилось то вызов трай кетч
# вывод и финал можно делать в мейне
# степень не омжет быть с - или дробным числом
# if no right or no left -> part shold not be empty
# if empty input -> can arg parse work with it
# manage delenie na 0
# esli otvet celoe chislo -> vivod lkak int
# rename na compv1 not main.py
# проверка на несколько xXxxXXXxx
# flag full shows all strings -v 'x^2  + 2 = 0' - dima expample
# make my sum function

import re
import sys
from my_math import Equation
from termcolor import colored


class Comp:
    ERR_DICT = {
        1: 'equation should have only one equal sign',
        2: 'both sides of the equation must be',
        3: 'expression musst have a integer exponent',
        4: 'expression must have a non-negative exponent',
        5: 'equation could not be solved, invalid syntax'
        # 5: 'expression must have a valid exponent [0, 1, 2]',
    }

    REG_NEG_EXP = r'[xX]\^(?:(?:-\d))'
    REG_FLT_EXP = r'[xX]\^(?:(?:\d*\.))'
    REG_00_POL = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^0'
    REG_01_POL = r'[-+]?(?:(?:\d*\.\d*)|(?:\d+))'
    REG_1_POLY = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX](?:\^1)?'
    REG_2_POLY = r'[-+]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^2'
    # REG_01_POLY = r'[-+]?(?:(?:\d*\.\d*)|\d+)\*?[xX]?(?:\^0)?' # ,

    # REG_INVAL_EXPONENT = r'[xX]\^(?:(?:-\d)|(?:\d*\.))' # old good
    REG_HIGH_EXPONENT = r'[xX]\^(?:(?:\d{2,})|(?:[3-9]))'  # old good

    reg0 = r'qwe'

    def __init__(self, equation: str, extend_param=None):
        self.orig = equation
        self.cin = self.cutted_input
        self.check_input()
        print(self.cin)

        self.raw_lists = self.sort_variables
        print(self.raw_lists)

        self.eq = Equation(self.convert_variables)

        # simple reduced form
        # bonus reduced form

        # self.rdf = self.make_reduced_form
        # self.polynomal degree
        # discriminant chech
        # solutions

        # if after all calc poly != 0 with case poly self.poly == 0 -> no solution
        # self.poly0 = 4*x^0 = 8*x^0 -> this no solution
        # self.pow1 =
        # self.pow2 =

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
        # 1. проверка на слова и буквы, по регексу должны быть только числа хХ или знаки
        # сотальное на выход сделать эту проверку вообще первым делом
        # 
        # 2. in other time -> shold show first polynom that doesnt match
        # self.error_func(5) if re.findall(self.REG_HIGH_EXPONENT, self.cin) else None

    @property
    def sort_variables(self) -> tuple:
        left_part, right_part = self.cin.split('=')

        # 1. proverka na to chto 2 storoni equals !
        # sdelat' func проверяющая что обе части равны между собой
        # это может начаинаться как функция мейк клиар варс только без
        # переноса все в одну часть с минусом.

        # 2. потом проверка что полином больше 2х

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
        self.error_func(5) if len(left_part) != 0 or len(
            right_part) != 0 else None
        list_x0.extend(tmp_lst)
        return (list_x0, list_x1, list_x2)

    @property
    def convert_variables(self) -> tuple:
        def get_sum(exp_list: list, exponent: int) -> float:
            fin_list = [i.replace('X', 'x').replace(f'^{exponent}', '') for i in exp_list]
            fin_list = ['1' if i == 'x' else '-1' if i == '-x' else i for i in fin_list]
            if exponent == 0:
            	return sum(map(float, (i.replace('*x', '') for i in fin_list)))
            return sum(map(float, (i.replace('*x', '').replace('x', '') for i in fin_list)))
        total = tuple(get_sum(self.raw_lists[i], i) for i in range(len(self.raw_lists)))
        return total





    def finall_output():
        pass

    @classmethod
    def error_func(cls, num_err) -> None:
        # esli oshibka to dolzhni vivodit' Polynom i procchee
        print(colored(cls.ERR_DICT[num_err], 'red'))
        sys.exit(num_err)


# e = Comp('+3x^2 + 	3x^2-3x^2  -4x + 22.21 =  =')
# e = Comp('+3x^25 + 	3x^2-3x^22  -4x + 22.21 =3' ) # high exp
# e = Comp('+3x^2 + 	3x^2-3x^2  -4x + 22.21 =  ') # exit 2
# e = Comp('+3x^2 + 	3x^2-3x^2.2  -4x + 22 = 123') # pow float
# e = Comp('+3x^2 + 	3x^2-3x^-2  -4x + 22.21 = 2') # negative
# e = Comp('+3x^2 + 	3x^2-3x^2  -4x + 22.21 = 2') # try it good

# subj
# e = Comp('5 * X^0 +4 * X^ 1 - 9.3 * X^2 = 1 * x^0')
# e = Comp('5* x^0 + 4 * x^1 = 4* x^0')
# e = Comp('8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0')
# e = Comp('5 + 4 * X + X^2= X^2')
e = Comp('3X^2= 2x')

# check list
# 5 * X^0 = 5 * X^0
# 2 * X^0 = 8 * X^0
# 5 * X^0 = 4 * X^0 + 7 * X^1
# 5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1
# 6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1 # disc = 0
# 5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1 # neg disc

# my test
# e = Comp(
#     '5*X^0\
# 		333\
# 		-1*X^0\
# 		-1*x^0\
# 		+1*x^0\
# 		+5*X^0\
# 		X^0\
# 		-x^0\
# 		-123\
# 		+ 13.12\
# 		-424\
# 		-99.3\
# 		-123.2 \
# 		\
# 		+3*X^1\
# 		+4*X^1\
# 		-4*X^1\
# 		+0*X^1\
# 		+12X\
# 		-12*X\
# 		-4.2*X^1\
# 		+4.23X^1\
# 		+X\
# 		-x\
# 		= \
# 		+22.3*X^2\
# 		-9.3*X^2\
# 		+123*X^2\
# 		4x^2\
# 		+3*X^2\
# 		+3x^2\
# 		-1*x^2\
# 		-9.3*X^2\
# 		x^2'
# )


# f = 12.212312
# f=float(int(1000000*f))/1000000
# print(f)

# s = [3.0, 4.0, -4.0, 0.0, 12.0, -12.0, -4.2, 4.23, 1.0, -1.0]
# s = [-4.2, 4.23]
# s = sum(s)
# print(float(int(100000000000*s))/100000000000)
# print(123.0%int(123.2))
