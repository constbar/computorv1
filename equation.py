# test return values by mypy??
# try catch 0

from termcolor import colored
import computorv1
import sys


class Eq:
    def __init__(self, clear_data: tuple):
        self.orig_clear_data = clear_data
        self.c, self.b, self.a, *self.d = clear_data
        self.print_high_red_form() if any(self.d) else None
        self.disc = None

        self.pol_dgr = 2 if self.a else 1 if self.b else 0
        self.results = self.make_calculations

    @property
    def make_calculations(self):  # -> tuple or float
        if self.pol_dgr == 2:
            return self.calc_quadratic_func
        elif self.pol_dgr == 1:
            return -1.0 * self.c / self.b
            # return self.calc_linear_func
        else:
            print('no real solutions')
            return  # smth

    @property
    def calc_quadratic_func(self) -> tuple or float:
        self.disc = Eq.make_power(self.b, 2) - 4 * self.a * self.c
        print(colored(self.disc, 'red'))
        if self.disc > 0:
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

    def print_high_red_form(self) -> None:
        print('reduced form: ', end='')
        red_form = list()
        for i in range(len(self.orig_clear_data)):
            if self.orig_clear_data[i] or i < 3:
                red_form.append(f'{Eq.show_int(self.orig_clear_data[i])} * x^{i}')
        red_form = '+'.join(red_form).replace('+-', ' - ').replace('+', ' + ')
        red_form = '- ' + red_form[1:] if red_form[0] == '-' else red_form
        print(colored(red_form + ' = 0', 'green'))
        for i, v in enumerate(self.d, 3):
            high_exp = i
            if i > high_exp and v:
                high_exp = i
        print('polynomial degree:', colored(f'{high_exp}', 'green'))
        print('the polynomial degree is strictly greater than 2. couldnt be solved')
        sys.exit(10)

    def print_result(self, raw: list) -> None:  # raw list ne nuzhen
        flag = 1
        prec = 4  # make it in input of func
        # write here original formula # flag
        shw_a = Eq.show_int(self.a)  # перенести все в инит
        shw_b = Eq.show_int(self.b)
        shw_c = Eq.show_int(self.c)
        str_a = f'- {shw_a * -1}' if self.a < 0 else f'+ {shw_a}'
        str_b = f'- {shw_b * -1}' if self.b < 0 else f'+ {shw_b}'
        str_c = f'- {shw_c * -1}' if self.c < 0 else f'+ {shw_c}'

        if self.pol_dgr == 1:
            red_form = f'{str_c} * x^0 {str_b} * x^1 = 0'
            red_form = red_form[2:] if red_form[0] == '+' else red_form
            print('reduced form: ', colored(f'{red_form}', 'green'))
            print('polynomial degree: ', colored(f'{self.pol_dgr}', 'green'))
            print('linear formula: b*x + c = 0')
            print('in our equation:', colored(f'b = {shw_b}; c = {shw_c}', 'green'))
            print('the solution is:')
            print(colored(Eq.show_int(self.results), 'green'))
            print('solutions in irreducible fraction:')
            # print(Eq.make_fraction(self.results, 1))
            # make round esli tol'ko its not an int
            # print(str(Eq.make_fraction(Eq.make_round(self.results, prec))))


        if self.pol_dgr == 2:
            red_form = f'{str_c} * x^0 {str_b} * x^1 {str_a} * x^2 = 0'
            red_form = red_form[2:] if red_form[0] == '+' else red_form
            print('reduced form: ', colored(f'{red_form}', 'green'))
            print('polynomial degree: ', colored(f'{self.pol_dgr}', 'green'))
            # if flag
            print('polynomial formula: a*x² + b*x + c = 0')
            print('in our equation: ', colored(f'a = {shw_a}; b = {shw_b}; c = {shw_c}', 'green'))
            print('discriminant formula: d = b² - 4*a*c')
            print('in our equation: ', colored(f'd = ({shw_b})² - 4*{shw_a}*{shw_c}', 'green'))
            # flag
            print('discriminant is ', colored(f'{Eq.show_int(self.disc)}', 'green'))
            if self.disc > 0:
                print('solutions formula: (-b ± √d) / (2*a)')  # if flag
                # flag
                print('in our equation: ', colored(f'(-{shw_b} ± √{Eq.show_int(self.disc)}) / (2*{shw_a})', 'green'))

                print('discriminant is strictly positive, the two solutions are:')
                # [print(colored(str(Eq.make_round(i, prec)), 'green')) for i in self.results]
                [print(colored(str(format(i, f'.{prec}f')), 'green')) for i in self.results]
                print(self.results) !!!!
                # esli celoe chislo to ego ne nado delat' drob'u
                # if flag == 1
                # make abs here / for 1 line of code
                print('solutions in irreducible fraction:')
                [print(colored('-' + str(Eq.make_fraction(Eq.make_round(-1 * i, prec))), \
                    'green')) if i < 0 else print(colored(str(Eq.make_fraction(Eq.make_round(i, \
                        prec))), 'green')) for i in self.results]


                 # if dics= 0

        if self.pol_dgr == 1:
            pass

        # DDISCR IS LOW 0

    def make_power(number, power) -> float or int:  # int?
        if power == 0:
            return 1.0
        return number * Eq.make_power(number, power - 1)

    def make_sqrt(n, temp=0.0) -> float or int:
        fin_sqrt = n / 2
        while fin_sqrt != temp:
            temp = fin_sqrt
            fin_sqrt = (n / temp + temp) / 2
        return fin_sqrt

    def show_int(digit) -> float or int:
        if int(digit) == 0:  # test here/ maybe error here
            return 0
        is_int = digit % int(digit) == 0
        return int(digit) if is_int else digit

    def make_round(number, decimal=0):
        # if int -> return
        return (int(Eq.make_power(10, decimal) * number - 0.5) + 1) / \
            Eq.make_power(10, decimal)

    def gcd(a, b) -> int:
        if a == 0:
            return b
        elif b == 0:
            return a
        if a < b:
            return Eq.gcd(a, b % a)
        else:
            return Eq.gcd(b, a % b)

    def make_fraction(number, prec=1000000000) -> str:
        int_val = int(number)
        flt_val = number - int_val
        gcd_val = Eq.gcd(Eq.make_round(flt_val * prec), prec)
        nume = int(Eq.make_round(flt_val * prec) // gcd_val)
        deno = int(prec // gcd_val)
        return f'{int_val * deno + nume}/{deno}'
