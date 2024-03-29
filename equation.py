import sys

from termcolor import colored


class Eq:
    def __init__(self, data: dict, prec: int, frac: bool, verb: bool):
        self.data = data
        self.prec = prec
        self.frac = frac
        self.verb = verb
        self.disc = None
        self.results = list()
        if len(self.data) > 3:
            if self.check_high_poly():
                self.print_final_result()
        self.make_calculations()
        self.print_final_result()

    def check_high_poly(self) -> bool:
        h_vals = list(filter(lambda i: i > 2, self.data.keys()))
        for v in h_vals:
            if self.data[v]:
                return True
        return False

    @property
    def int_data(self) -> dict:
        return {k: Eq.try_int(v) for k, v in self.data.items()}

    @property
    def poly_degree(self) -> int:
        degree = 0
        for k, v in self.data.items():
            if v and degree < k:
                degree = k
        return degree

    def print_final_result(self) -> None:
        max_len_of_input = max(map(len, map(
            str, map(int, (self.data.values())))))
        if max_len_of_input > self.prec:
            self.prec = max_len_of_input

        red_form = ''
        for i in self.data.keys():
            red_form += f'{Eq.try_int(self.data[i])} * x^{i}+'
        red_form = red_form.replace('+-', ' - ').replace('+', ' + ')
        red_form = '- ' + red_form[1:] if red_form[0] == '-' else red_form
        red_form = red_form[:-2] + '= 0'

        print('reduced form:', colored(red_form, 'green'))
        print('polynomial degree:', colored(f'{self.poly_degree}', 'green'))

        if self.check_high_poly():
            sys.exit(f'the polynomial degree is strictly'
                     f' greater than 2. couldn\'t be solved')
        elif self.poly_degree == 0:
            sys.exit('no solution')
        elif self.poly_degree == 1 and self.verb:
            print('linear formula: b*x + c = 0')
            print('in our equation:',
                  colored(f'b = {self.int_data[1]}; '
                          f'c = {self.int_data[0]}', 'green'))
        elif self.poly_degree == 2:
            if self.verb:
                print('quadratic equation formula: a*x² + b*x + c = 0')
                print('in our equation: ',
                      colored(f'a = {self.int_data[2]}; '
                              f'b = {self.int_data[1]}; '
                              f'c = {self.int_data[0]}', 'green'))

                print('discriminant formula: d = b² - 4*a*c')
                print('in our equation: ',
                      colored(f'd = ({self.int_data[1]})² - '
                              f'4*{self.int_data[2]}*'
                              f'{self.int_data[0]}', 'green'))
                print('discriminant:',
                      colored(f'{Eq.try_int(self.disc)}', 'green'))

            if self.disc < 0:
                sys.exit('discriminant less than zero. no solution')
            elif self.disc > 0 and self.verb:
                print('solutions formula: (-b ± √d) / (2*a)')
                print('in our equation: ',
                      colored(f'(-({self.int_data[1]}) ± '
                              f'√{Eq.try_int(self.disc)}) / '
                              f'(2*{self.int_data[2]})', 'green'))
            elif self.disc == 0 and self.verb:
                print('solutions formula: (-b) / (2*a)')
                print('in our equation: ',
                      colored(f'(-({self.int_data[1]}) / '
                              f'(2*{self.int_data[2]})', 'green'))

        if self.disc is not None and self.disc != 0:
            print('discriminant is strictly positive, the two solutions are:')
        else:
            print('the solution is:')

        for i in self.results:
            if isinstance(Eq.try_int(i), float):
                print(colored(format(i, f'.{self.prec}f').rstrip('0'),
                              'green'))
            elif 'e+' in str(i):
                print(colored(i, 'green'))
            else:
                print(colored(Eq.try_int(i), 'green'))

        if self.frac or self.verb:
            print('solutions in irreducible fraction:')
            for i in self.results:
                sign = ''
                try:
                    if i % int(i) == 0:
                        print(colored((str(int(i)) + (self.prec * '0')) + '/' +
                                      ('1' + self.prec * '0'), 'green'))
                        continue
                except ZeroDivisionError:
                    if i == 0:
                        print(colored('0', 'green'))
                        continue
                if i < 0:
                    i *= -1
                    sign = '-'
                print(colored(sign + Eq.make_fraction(i, int(f"1{self.prec * '0'}")),
                              'green'))

    def make_calculations(self) -> None:
        """
        defines the degree of a polynomial
        """
        if self.poly_degree == 2:
            self.calc_quadratic_func()
        elif self.poly_degree == 1:
            self.results.append(-1.0 * self.data[0] /
                                self.data[1])
        else:
            self.print_final_result()

    def calc_quadratic_func(self) -> None:
        """
        if disc == 0 -> eq has 1 solution
        if disc > 1 -> eq has 2 solutions
        if disc < 0 -> eq has no solution
        all solutions add to self results
        """
        self.disc = Eq.make_power(self.data[1], 2) - \
            4 * self.data[2] * self.data[0]
        if self.disc == 0:
            self.results.append((-1.0 * self.data[1]) /
                                (2 * self.data[2]))
        elif self.disc > 0:
            def find_solutions(sign_type: str) -> float:
                sign = 1.0 if sign_type == '+' else -1.0
                numerator = -1 * self.data[1] + sign * \
                    Eq.make_sqrt(self.disc)
                denominator = 2 * self.data[2]
                return numerator / denominator

            self.results.append(find_solutions('+'))
            self.results.append(find_solutions('-'))
        else:
            self.print_final_result()

    @staticmethod
    def make_power(number: float, power: int) -> int | float:
        if power == 0:
            return 1.0
        return number * Eq.make_power(number, power - 1)

    @staticmethod
    def make_sqrt(n: float, temp: float = 0.0) -> float:
        fin_sqrt = n / 2
        while fin_sqrt != temp:
            temp = fin_sqrt
            fin_sqrt = (n / temp + temp) / 2
        return fin_sqrt

    @staticmethod
    def try_int(digit: float) -> int | float | str:
        if digit == 0:
            return 0
        if -1 < digit < 1:
            return digit
        try:
            is_int = digit % int(digit) == 0
        except OverflowError:
            sys.exit('number is too big. number should not be inf')
        return int(digit) if is_int else digit

    @staticmethod
    def make_round(number: int | float, decimal: int = 0) -> int | float:
        return (int(Eq.make_power(10, decimal) * number - 0.5) + 1) / \
            Eq.make_power(10, decimal)

    @staticmethod
    def gcd(a: int | float, b: int | float) -> int | float:
        if a == 0:
            return b
        elif b == 0:
            return a
        if a < b:
            return Eq.gcd(a, b % a)
        else:
            return Eq.gcd(b, a % b)

    @staticmethod
    def make_fraction(number: float, prec: int = 1000000000) -> str:
        if number == 0:
            return '0'
        int_val = int(number)
        flt_val = number - int_val
        gcd_val = Eq.gcd(Eq.make_round(flt_val * prec), prec)
        nume = int(Eq.make_round(flt_val * prec) // gcd_val)
        deno = int(prec // gcd_val)
        return f'{int_val * deno + nume}/{deno}'
