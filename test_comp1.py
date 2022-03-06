from calculation import Calc

# no solution:
# e = Calc('2 = 1')
# e = Calc('X^2 = 0')
# e = Calc('10 = 10')
# e = Calc('4*X^0=8*X^0')
# e = Calc('X^2 + 16 = 0')
# e = Calc('2 * X^0 = 8 * X^0')
# e = Calc('32 + 3 + 00000001.000000000 = 04.00000000000000000000')

# any x is a solution
# e = Calc('7*X^0=7*X^0')
# e = Calc('5 * X^0 = 5 * X^0')
# e = Calc('1 + x^20= x^20 + 1')
# e = Calc('13x^23 + 1 = 1 + 13*x^23')

# wrong syntax
# e = Calc('')
# e = Calc('=')
# e = Calc('1 +* X = 3')
# e = Calc('^2 + X = 0')
# e = Calc('1 +- X = 3')
# e = Calc('error = solution')
# e = Calc('2 + X = X - 3 = X^2')
# e = Calc('Y^2 + 2 + 3 * X^1 = 0')
# e = Calc('X^-2 + 2 + 3 * X^1 = 3')
# e = Calc('+3x^2 + 3x^2-3x^2.2 - 4x + 22 = 123')
# e = Calc('+3x^2 + 3x^2-3x^2  - 4x + 22.21 =  ')
# e = Calc('+3x^2 + 3x^2-3x^-2 - 4x + 22.21 = 2')
# e = Calc('+3x^2 + 3x^2-3x^2 - 4x + 22.21 =  =')
# e = Calc('x^2 = 1209349432411111115555555555555555555558888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888888444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444444')

# polynomial degree > 2
# e = Calc('+3x^25 + 3x^2-3x^22 -4x + 22.21 = 3')
# e = Calc('8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0')
# e = Calc('-x - 3X^20 - 3x^4 + 2x^2 + 9x^54 + 4x^1 - 32x^7 + x + 2x + 2 = 0 - 4 - 13x^23')
# e = Calc('-333.123 - 22.123x^2 + 32.x^2 - 23.X^7 + 33.5x^4 + 4X^3 + 20x^3 + 1 - x^5 = 4X^2')
# e = Calc('X^3 + 2 - X^1 = 3')

# polynomial degree == 0 no solution
# e = Calc('X - X = 00000000000000000003')
# e = Calc('22x^2 + 123 -1 = 22x^2 - 1')
# e = Calc('+ 3.2x^2 - 4.3 + 1 + x^99= 2x + 4x^123 + 1x^99')

# polynomial degree == 1
# e = Calc('4x = 1')
# e = Calc('4x = 12')
# e = Calc('1 * X = 3')
# e = Calc('X + 1 = 0')
# e = Calc('x + 23 = 0')
# e = Calc('x - 47 = 0')
# e = Calc('8x + 2x = 8')
# e = Calc('0x^2 + 4x = 2')
# e = Calc('x^2 -6x + 9 = 0')
# e = Calc('5*X^0=4*X^0+7*X^1')
# e = Calc('8.76x + 2.9x = 8.2')
# e = Calc('5 + 4 * X + X^2 = X^2')
# e = Calc('X^2 + 4 + 2 * X^1 = 3')
# e = Calc('x^2 + 4x + x + 2 = 0 + x^2')
# e = Calc('5 * X^0 = 4 * X^0 + 7 * X^1')
# e = Calc('5 * x^0 + 4 * x^1 = 4 * x^0')
# e = Calc('1 * X  + 2 * X^1 + X - X = 3')
# e = Calc('6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1')

# discriminant == 0
# e = Calc('X^2 + 2 * X^1 = -1')
# e = Calc('42x^2 + x^2 + 1 = 1 + 42x^2')
# e = Calc('6 * X^0 + 11 * X^1 + 5 * X^2 = 1 * X^0 + 1 * X^1')

# # discriminant > 0
# e = Calc('3X ^ 2 = 2x')
# e = Calc('X^2 - 16 = 0')
# e = Calc('2X^2 = x + 3')
# e = Calc('3x^2 -3- 5x = 0')
# e = Calc('2x^2 - 3x = -1')
# e = Calc('2x^2 - 13x = -1')
# e = Calc('3x^2 - 6x + 1 = 0')
# e = Calc('5 * X^2 = 1 * X^0')
# e = Calc('2x^2 -22x - 1 = 0')
# e = Calc('2 * X^1 + X^2 = 0')
# e = Calc('X^2 -6 * X^1 + 5 = 0')
# e = Calc('2X^2 - 123x = x + 41')
# e = Calc('X^2 + 2 + 3 * X^1 = 3')
# e = Calc('+ X^2 + 2 + 3 * X^1 = 3')
# e = Calc('12.132888x^2 + 2x = + 1212')
# e = Calc('2.2x^2 - 3.3x^1 - 22.2 = 0')
# e = Calc('22x^2 + 33.2x + 1.213 = 3x^2 + 32')
# e = Calc('5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0')
# e = Calc('5 * X^0 + 4 * X^1 - 9.443 * X^2 = 1 * X^0 - 312')
# e = Calc('5 * X^0 + 13 * X^1 + 3 * X^2 = 1 * X^0 + 1 * X^1')

# # discriminant < 0
# e = Calc('3x^2 - 4x + 2 = 0')
# e = Calc('2x^2 + 1x + 200 = 0')
# e = Calc('X^2 -6 * X^1 + 13 = 0')
# e = Calc('+3x^2 + 3x^2-3x^2 - 4x + 22.21 = 2')
# e = Calc('5 * X^0 + 3 * X^1 + 3 * X^2 = 1 * X^0 + 0 * X^1')

# e = Calc('8 * X^0 - 6 * X^1 + 0 * X^2 - 5.6 * X^3 = 3 * X^0  - 5.6 * X^3')
# e = Calc('8 * X^0 - 6 * X^1 + 0 * X^2 + 10.6 * X^3 = 3 * X^0  - 5.6 * X^3')



# polynomes = [
# 	'5*X^0 + 3*X^1 + 3*X^2=1*X^0+0*X^1',
# 	]

# for example in polynomes:
# 	print('Example for testing : -> ' + example)
# 	os.system('python3 computor.py -v -s \' + example + '\')
# 	print(') - interesting 