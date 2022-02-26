#!/usr/bin/python3

from computorv1 import Comp

# e = Comp('x^4 + 4X^3 + 20x^3 + 1= 1 + 20x^3 + 4X^3')
# e = Comp('x^3 + 1 = x^3 + 1')
# e = Comp('22x^2 + 123 -1 = 22x^2 - 1')
# e = Comp('0x^2 + 4x - 2 = 0')
e = Comp('22x^2 + 4x + x  + 2 = 0 + x^2')




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
# e = Comp('3X^2= 2x')
# e = Comp('2X^2= x + 3') # good. celie chisla
# e = Comp('2X^2 - 123x = x + 41')
# e = Comp('2x^2 + 1x + 200 = 0')
# e = Comp('x^2 -6x + 9 = 0')
# e = Comp('4x = 0') # returns -0.0
# e = Comp('4x = 12')

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

# print()
# f = 12.2190121212312312

# # f=float(int(1000000*f))/1000000
# f=float(int(1000*f)) / 1000
# print(f)

# print(float(int(100000000000*s))/100000000000)
# print(123.0%int(123.2))
