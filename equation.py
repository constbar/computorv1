# make __str__ dang method withc will show all a_B_c values for full version of ./script
# test return values by mypy??
# try catch 0
# send thru show_int
from termcolor import colored


class Eq:
    def __init__(self, clear_data: tuple):
        self.c, self.b, self.a = clear_data
        self.disc = None
        print(f'clear data: {clear_data}')

        self.pol_dgr = 2 if self.a else 1 if self.b else 0
        print(f'polynomial degree is {self.pol_dgr}')
        print(self.make_calculations)

    @property
    def make_calculations(self):  # -> tuple or float
        if self.pol_dgr == 2:
            return self.calc_quadratic_func
        elif self.pol_dgr == 1:
            return -1.0 * self.c / self.b
            # return self.calc_linear_func
        else:
            print('no real solutions')
            return # smth

    @property
    def calc_quadratic_func(self) -> tuple or float:
        self.disc = Eq.make_power(self.b, 2) - 4 * self.a * self.c
        print(f'discriminant is {self.disc}')
        if self.disc > 0:
            # message that disc is more than 0
            def find_solutions(s='+') -> float:
                sign = 1.0 if s == '+' else -1.0
                numerator = -1 * self.b + sign * \
                    Eq.make_sqrt(self.disc)  # here i del (-1)
                denominator = 2 * self.a
                return numerator / denominator

            sol1 = find_solutions('-')
            sol2 = find_solutions()
            return sol1, sol2

        elif self.disc == 0:
            sol0 = (-1.0) * self.b / 2 * self.a
            return sol0
            # massage that Eq has only 1 solution
        else:
            # call sys exit err
            print('disc is lower than 0. no solutions')
            return

    def show_result(self, raw: list) -> None: # raw list ne nuzhen
        print()
        flag = 1
        # write here original formula
        shw_a = Eq.show_int(self.a)
        shw_b = Eq.show_int(self.b)
        shw_c = Eq.show_int(self.c)

        str_a = f'- {shw_a * -1}' if self.a < 0 else f'+ {shw_a}'
        str_b = f'- {shw_b * -1}' if self.b < 0 else f'+ {shw_b}'
        str_c = f'- {shw_c * -1}' if self.c < 0 else f'+ {shw_c}'

        # if polnim degree = 2 
        red_form = f'{str_c} * X ^ 0 {str_b} * X ^ 1 {str_a} * X^2 = 0'
        red_form = red_form[2:] if red_form[0] == '+' else red_form
        print(colored(f'reduced form: {red_form}', 'green'))
        print(colored(f'polynomial degree: {self.pol_dgr}', 'green'))
        print('polynomial formula: a*x² + b*x + c = 0')                 # if flag
        print(colored(f'in our equation: a = {shw_a}; b = {shw_b}; c = {shw_c}', 'green'))
        print(f'discriminant formula: d = b² - 4*a*c')
        print(colored(f'in our equation: d = {shw_b}² - 4*{shw_a}*{shw_c}', 'green'))
        print(colored(f'discriminant is {self.disc}', 'green'))

        DDISCR IS LOW 0







    def make_power(num, power) -> float or int:  # int?
        if power == 0:
            return 1.0
        return num * Eq.make_power(num, power - 1)

    def make_sqrt(n, temp: float = 0.0) -> float:
        fin_sqrt = n / 2
        while fin_sqrt != temp:
            temp = fin_sqrt
            fin_sqrt = (n / temp + temp) / 2
        return fin_sqrt

    def show_int(digit) -> float or int:
        # if -
        # if 0 return zero bez tochki
        is_int = digit % int(digit) == 0
        return int(digit) if is_int else digit
