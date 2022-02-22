# при конвертации в инт если не получилось то вызов трай кетч
# вывод и финал можно делать в мейне

from termcolor import colored
import sys

class Comp:
	# err_dict = {
	# 		1: 'equation should have only one equal sign',
	# 		2: 'onother one'
	# 	}
	# reg0 = r'qwe'

	def __init__(self, equation: str):
		self.orig = equation
		self.cin = self.cutted_input
		self.first_check()

	@property
	def cutted_input(self):
		cut_inp = self.orig
		cut_inp = cut_inp.replace('\t', '').replace(' ', '')
		return cut_inp

	@classmethod
	def error_func(cls):
		d = {
			1: 'equation should have only one equal sign',
			2: 'onother one'
		}
		# print(colored(d[1], 'red'))
		# sys.exit(num_err)
		return num_err

	def first_check(self):
		print(cls.error_func())
		# if self.cin.count('=') != 1:
			# error_func(1)
		# проверка на = 
		# на больше чем 3 степерь не дробная она ли
		# проверки .. на всякие разные знаки




e = Comp('+3x^2 + 	3x^2-3x^2  -4x + 22.21 =  =')



