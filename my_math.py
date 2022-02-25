# make __str__ dang method withc will show all a_B_c values for full version of ./script
#  −b/2a.

class Equation:
    def __init__(self, clear_data: tuple):
        self.c, self.b, self.a = clear_data
        self.disc = None
        print(f'clear data: {clear_data}')

        self.pol_dgr = 2 if self.a else 1 if self.b else 0
        print(f'polynomial degree is {self.pol_dgr}')
        self.make_calculations

    @property
    def make_calculations(self):  # ->
        if self.pol_dgr == 2:
            return self.calc_quadratic_func
        return
        # elif self.pol_dgr == 1:
        # 	return calc_linear_func()
        # else:
        # 	return calc_const_function()

    def make_power(num, power) -> float or int: # int? 
        if power == 0:
            return 1.0
        return num * Equation.make_power(num, power - 1)

    @property
    def calc_quadratic_func(self):
        self.disc = Equation.make_power(self.b, 2) - 4 * self.a * self.c
        print(f'discriminant is {self.disc}')
        if self.disc > 0:
        	def find_solutions(sign='+'):# -> float:
        		numerator = Non
        		# numerator = (-1) + Equation.make_power(self.disc, 1/2)
        		print(numerator)
        		# denominator
        	sol2 = find_solutions()
        	# sol1 = find_solutions('-')

        elif self.disc < 0:
        	pass
        else:
        	pass # est' 1 корень
        return

    def print_int(digit):
        # if -
        is_int = digit % int(digit) == 0
        return int(digit) if is_int else digit
