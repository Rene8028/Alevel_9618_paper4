class Fraction:
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        self.__denominator = denominator

    def get_n(self):
        return int(self.__numerator)

    def get_d(self):
        return int(self.__denominator)
    
    def gcd(self, x, y):
        reminder = x % y
        if reminder == 0:
            return y
        else:
            return self.gcd(y, reminder)

    def print_f(self):
        print(f'{self.__numerator} / {self.__denominator}')

    def reduce(self):
        gcd_nd = int(self.gcd(self.__numerator, self.__denominator))
        self.__numerator = int(self.__numerator / gcd_nd)
        self.__denominator = int(self.__denominator / gcd_nd)
        return self

    def plus(self, addf):
        sum_n = addf.get_n() * self.__denominator + self.__numerator * addf.get_d()
        sum_d = addf.get_d() * self.__denominator
        return Fraction(sum_n, sum_d).reduce()
        
    def times(self, prof):
        pro_n = prof.get_n() * self.__numerator
        pro_d = prof.get_d() * self.__denominator
        return Fraction(pro_n, pro_d).reduce()



a = Fraction(2, 4)  #1/2
a.reduce()
a.print_f()

b = Fraction(2, 6)  #1/3
b.reduce()
b.print_f()

sum_ab = a.plus(b)
sum_ab.print_f()  #5/6
pro_ab = a.times(b)
pro_ab.print_f()  #1/6
