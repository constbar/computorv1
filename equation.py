# test return values by mypy??
# try catch 0
# check in properties getters -> None by mypy
# mozhet podojdet self.data HERE print_final_result(self, inp_dict: dict) -
# if solution -0.0
# return after getting results?
# check # EQ.showint in every show print

from termcolor import colored
import computorv1
import sys


class Eq:
    def __init__(self, data: dict):
        self.data = data
        self.disc = None
        self.results = list()
        self.pol_dgr = self.get_poly_degree
        if len(self.data) > 3:
            self.print_final_result()
        self.make_calculations()        
        self.print_final_result()

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
        flag = 1 # flag of full showing of all features

        red_form = ''
        for i in self.data.keys():
            red_form += f'{Eq.try_int(self.data[i])} * x^{i}+'
        red_form = red_form.replace('+-', ' - ').replace('+', ' + ')
        red_form = '- ' + red_form[1:] if red_form[0] == '-' else red_form
        red_form = red_form[:-2] + '= 0'
        
        print('reduced form:', colored(red_form, 'green'))
        print('polynomial degree:', colored(f'{self.pol_dgr}', 'green')) # 

        if len(self.data) > 3:
            sys.exit('the polynomial degree is strictly greater \
                than 2. couldnt be solved')
        elif self.pol_dgr == 1:
            print('linear formula: b*x + c = 0')
            print('in our equation:', 
                colored(f'b = {Eq.try_int(self.data[1])}; ' # EQ.showint
                        f'c = {Eq.try_int(self.data[0])}', 'green')) # EQ.showint
        elif self.pol_dgr == 2: # and flag is == 1
            # if flag
            print('quadratic equation formula: a*x² + b*x + c = 0')
            print('in our equation: ', colored(f'a = {self.data[2]}; '
                f'b = {self.data[1]}; c = {self.data[0]}', 'green')) # make EQ.showint
            print('discriminant formula: d = b² - 4*a*c')
            print('in our equation: ', colored(f'd = ({shw_b})² - 4*{shw_a}*{shw_c}', 'green')) # EQ.showint



        elif self.disc < 0:
            sys.exit('discriminant less than zero. no solutions')
            # print('solutions in irreducible fraction:')
            # print(Eq.make_fraction(self.results, 1))
            # make round esli tol'ko its not an int
            # print(str(Eq.make_fraction(Eq.make_round(self.results, prec))))
        
        print('the solution is:')
        for i in self.results: # here i will need str format for int and float
            if isinstance(Eq.try_int(i), float):
                print(colored(format(i, f'.{prec}f').strip('0'), 'green'))
            else:
                print(colored(Eq.try_int(i), 'green'))
        # if flag
        print('solutions in irreducible fraction:')
        for i in self.results: # 1 / 10000000 ???
            sign = ''
            if i % int(i) == 0:
                print(colored((str(int(i)) + (prec * '0')) + '/' + 
                    ('1' + prec * '0') , 'green'))
                continue
            elif i < 0:
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
            print(colored('disc is less 0', 'cyan'))
            self.print_final_result()

    def print_result(self, raw: list) -> None:  # raw list ne nuzhen
        if self.pol_dgr == 1:
            pass # ok

        if self.pol_dgr == 2:

            # if flag
            
            
            
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
