# todo:
# 1. delete spaces and tabs
# 2. minus pow -2 
# 3. в регэксе есть еденичная \d* возможно лучше поставить \d+
# 4. init main
# 5 could solve only quadratic polynomial


import re

x2 = [
	r'+3x^2+3x^2-3x^2+3.4x^2+3.3x^2',
	r'*3*x^2',
	r'-3*x^2',
	r'+4*x^2',
	r'-3.4*x^2',
	r'-544*x^2',
	r'239x^2',
	r'-3.0X^2',
	r'3x^2',
	r'3*x^2',
	r'-3x^2',
	r'-23x^2',
	r'-3x^2-2*x^2',
	r'3x^2',
	r'x^2+2'
	]

x1 = [
	'-4x',
	'4.3x^1',
	'24.3x^1-x',
	'12.123*x^1',
	'x',
	'2x',
	'3.3x',
	'-x',
	'-22x',
	'-99*x',
	'-12*x^1',
	'-12x^1',
	'-x',
	'-5x',
	'-123.123123x+123123123.123123123x',
	'123.22x-4.212312x',
	'23.33*x^1-2x',
	'23.33x^1-x',
	'-x',
	'-1.x'
]

x0 = [
	r'+123',
	r'-123123',
	r'-1',
	r'+2',
	r'+0.2',
	r'123',
	r'123',
	r'1234',
	r'5234',
	r'6',
	r'45',
	r'3.1232312',
	r'-4x+2',
	r'4.3x^0+3',
	r'-24.3x^0+12123123.123',
	r'-12*x^0',
	r'-12x^0',
	'123.0',
	'123.'
]

t = x2[0]

# reg2 = r'[+-]?(?:(?:\d*)|(?:\d*\.\d*))[*]?[xX]\^2'# this worked
reg2 = r'[+-]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX]\^2' # new
# match = re.findall(reg2, t)
# print(match)

# for i in x2:
	# match = re.findall(reg2, i)
	# print(match)


# reg1 = r'[+-]?(?:(?:\d*)|(?:\d*\.\d*))\*?[xX](?:\^1)?'
# for i in x1:
# 	match = re.findall(reg1, i)
	# print(match)


reg0 = r'[+-]?(?:(?:\d*\.\d*)|\d+)\*?[xX]?(?:\^0)?'
for i in x0:
	match = re.findall(reg0, i)
	print(match)
