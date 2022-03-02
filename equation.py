# test return values by mypy??
# try catch 0

from termcolor import colored
import computorv1
import sys


class Eq:
    def __init__(self, data: dict):
        self.data = data
        print(data)
        if len(data) > 3:  # make self.data
            self.print_reduce_form(data)

        self.disc = None
        self.pol_dgr = 2 if data[2] else 1  # if data[1] else 0
        self.results = self.make_calculations
        print('solutions: ', self.results)

        # print(colored(data, "cyan"))
        # self.int_data results= {} # here will be str data for printing
        # self.drobnaya data results

        sys.exit(132)
        self.c, self.b, self.a, *self.d = data
        self.print_high_red_form() if any(self.d) else None
        self.disc = None
        self.results = self.make_calculations

    def print_reduce_form(self, inp_dict: dict) -> None:
        red_form = ''
        for i in inp_dict.keys():
            red_form += f'{Eq.try_int(inp_dict[i])} * x^{i}+'
        red_form = red_form.replace('+-', ' - ').replace('+', ' + ')
        red_form = '- ' + red_form[1:] if red_form[0] == '-' else red_form
        red_form = red_form[:-2] + '= 0'

        print(colored(red_form, 'green'))
        if len(inp_dict) > 3:
            # может будет ниже
            print('polynomial degree:', colored(f'{max(inp_dict.keys())}', 'green'))
            print('the polynomial degree is strictly greater than 2. couldnt be solved')
            sys.exit(10)
        # if solution -0.0

    @property
    def make_calculations(self):  # -> tuple or float
        print(self.pol_dgr)
        if self.pol_dgr == 2:
            return self.calc_quadratic_func
        else:
            return -1.0 * self.data[0] / self.data[1]

    @property
    def calc_quadratic_func(self) -> tuple or float:
        # print(self.data)
        self.disc = Eq.make_power(self.data[1], 2) - \
            4 * self.data[2] * self.data[0]
        
        if self.disc == 0:
            return (-1.0 * self.data[1]) / (2 * self.data[2])
        elif self.disc > 0:
            def find_solutions(type) -> float:
                sign = 1.0 if type == '+' else -1.0
                numerator = -1 * self.data[1] + sign * \
                    Eq.make_sqrt(self.disc)
                denominator = 2 * self.data[2]
                return numerator / denominator

            sol1 = find_solutions('+')
            sol2 = find_solutions('-')
            return sol1, sol2
        else:
            # perenesti v reduced form надо надо
            sys.exit('disc is lower than 0. no solutions')
            

    def print_result(self, raw: list) -> None:  # raw list ne nuzhen
        flag = 1
        prec = 4  # make it in input of func
        # write here original formula # flag
        shw_a = Eq.try_int(self.a)  # перенести все в инит
        shw_b = Eq.try_int(self.b)
        shw_c = Eq.try_int(self.c)
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
            print(colored(Eq.try_int(self.results), 'green'))
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
            print('discriminant is ', colored(f'{Eq.try_int(self.disc)}', 'green'))
            if self.disc > 0:
                print('solutions formula: (-b ± √d) / (2*a)')  # if flag
                # flag
                print('in our equation: ', colored(f'(-{shw_b} ± √{Eq.try_int(self.disc)}) / (2*{shw_a})', 'green'))

                print('discriminant is strictly positive, the two solutions are:')
                # [print(colored(str(Eq.make_round(i, prec)), 'green')) for i in self.results]
                [print(colored(str(format(i, f'.{prec}f')), 'green')) for i in self.results]
                # if ne float make dtrobi
                # print(self.results) !!!!
                # esli celoe chislo to ego ne nado delat' drob'u
                # if flag == 1
                # make abs here / for 1 line of code
                print('solutions in irreducible fraction:')
                [print(colored('-' + str(Eq.make_fraction(Eq.make_round(-1 * i, prec))),
                               'green')) if i < 0 else print(colored(str(Eq.make_fraction(Eq.make_round(i,
                                                                                                        prec))), 'green')) for i in self.results]

                # if dics= 0

        if self.pol_dgr == 1:
            pass
        # усли дискриминант менььше 0 то нет real solutions
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

    def try_int(digit) -> float or int:
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
