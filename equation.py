# test return values by mypy??
# try catch 0
# check in properties getters -> None by mypy
# mozhet podojdet self.data HERE print_final_result(self, inp_dict: dict) -
# if solution -0.0
# return after getting results?

from termcolor import colored
import computorv1
import sys


class Eq:
    def __init__(self, data: dict):
        self.data = data
        self.disc = None
        self.results = list()
        self.i_data = self.try_int_data
        self.pol_dgr = self.get_poly_degree
        if len(self.data) > 3:
            self.print_final_result()
        self.make_calculations()
        self.print_final_result()

    @property
    def try_int_data(self) -> dict:
        return {k: Eq.try_int(v) for k, v in self.data.items()}

    @property
    def get_poly_degree(self) -> int:
        degree = 0
        for k, v in self.data.items():
            if v and degree < k:
                degree = k
        return degree

    def print_final_result(self) -> None:
        # make flag of prec
        prec = 4
        flag = 1  # flag of full showing of all features

        red_form = ''
        for i in self.data.keys():
            red_form += f'{Eq.try_int(self.data[i])} * x^{i}+'
        red_form = red_form.replace('+-', ' - ').replace('+', ' + ')
        red_form = '- ' + red_form[1:] if red_form[0] == '-' else red_form
        red_form = red_form[:-2] + '= 0'

        print('reduced form:', colored(red_form, 'green'))
        print('polynomial degree:', colored(f'{self.pol_dgr}', 'green'))

        if len(self.data) > 3:
            sys.exit('the polynomial degree is strictly greater \
                than 2. couldnt be solved')
        elif self.pol_dgr == 1:
            print('linear formula: b*x + c = 0')
            print('in our equation:',
                  colored(f'b = {self.i_data[1]}; '
                          f'c = {self.i_data[0]}', 'green'))
            # print('solutions in irreducible fraction:')
            # print(Eq.make_fraction(self.results, 1))
            # make round esli tol'ko its not an int
            # print(str(Eq.make_fraction(Eq.make_round(self.results, prec))))
        elif self.pol_dgr == 2:  # and flag is == 1
            # if flag
            print('quadratic equation formula: a*x² + b*x + c = 0')
            print('in our equation: ',
                  colored(f'a = {self.i_data[2]}; '
                          f'b = {self.i_data[1]}; '
                          f'c = {self.i_data[0]}', 'green'))

            print('discriminant formula: d = b² - 4*a*c')
            print('in our equation: ',
                  colored(f'd = ({self.i_data[1]})² - '
                          f'4*{self.i_data[2]}*'
                          f'{self.i_data[0]}', 'green'))

            print('discriminant is',
                  colored(f'{Eq.try_int(self.disc)}', 'green'))

            if self.disc < 0:
                sys.exit('discriminant less than zero. no solutions')

            elif self.disc > 0:
                print('solutions formula: (-b ± √d) / (2*a)')  # if flag
                print('in our equation: ',
                      colored(f'(-({self.i_data[1]}) ± '
                              f'√{Eq.try_int(self.disc)}) / '
                              f'(2*{self.i_data[2]})', 'green'))

            # if self.disc == 0:
                # print("printprintprintprintprintprintprintprint")


        if self.disc is not None and self.disc != 0: # need i != 0? 
            print('discriminant is strictly positive, the two solutions are:')
        else:
            print('the solution is:')

        for i in self.results:  # here i will need str format for int and float
            if isinstance(Eq.try_int(i), float):
                # print(i)
                print(colored(format(i, f'.{prec}f').rstrip('0'), 'green'))
            else:
                print(colored(Eq.try_int(i), 'green'))
        # if flag
        print('solutions in irreducible fraction:')
        for i in self.results:  # 1 / 10000000 ???
            sign = ''
            # if Eq.try_int(i) == 0:
            # if -1 > i > 1 and i % int(i) == 0:
            # if -1 > i > 1:
            try:
                if i % int(i) == 0:
                    print(colored((str(int(i)) + (prec * '0')) + '/' +
                                  ('1' + prec * '0'), 'green'))
                    # print(colored((str(Eq.try_int(i)) + (prec * '0')) + '/' +
                    continue
            except ZeroDivisionError:
                if i == 0:
                    print(colored('0', 'green'))
                pass
                # print(colored('0', 'green'))
                # continue
            if i < 0:
                i *= -1
                sign = '-'
            print(colored(sign + Eq.make_fraction(i, int(f"1{prec * '0'}")), 'green'))

    def make_calculations(self):  # -> tuple or float
        if self.pol_dgr == 2:
            self.calc_quadratic_func()
            # return # need i?
        else:
            self.results.append(-1.0 * self.data[0] /
                                self.data[1])
            # return # need i?

    def calc_quadratic_func(self) -> None:
        '''
        if disc == 0 -> eq has 1 solution
        -- '' --

        all solutions added to self.results
        '''
        self.disc = Eq.make_power(self.data[1], 2) - \
            4 * self.data[2] * self.data[0]
        if self.disc == 0:
            self.results.append((-1.0 * self.data[1]) /
                                (2 * self.data[2]))
        elif self.disc > 0:
            def find_solutions(type) -> float:
                sign = 1.0 if type == '+' else -1.0
                numerator = -1 * self.data[1] + sign * \
                    Eq.make_sqrt(self.disc)
                denominator = 2 * self.data[2]
                return numerator / denominator

            self.results.append(find_solutions('+'))
            self.results.append(find_solutions('-'))
        else:
            self.print_final_result()

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
        if digit == 0:
            return 0
        if -1 < digit < 1:
            return digit
        # if int(digit) == 0:  # test here/ maybe error here
        #     return 0
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
