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

class MixedFraction(Fraction):
    def __init__(self, whole, num, den):
        Fraction.__init__(self, num, den)
        self.__whole = whole
    def get_w(self):
        return self.__whole
    def print_f(self):
        print(self.__whole, end = " ")
        Fraction.print_f(self)
    def plus(self, addmf):
        sum_w = self.__whole + addmf.get_w()
        addf = Fraction.plus(self, addmf)
        sum_n = addf.get_n()
        sum_d = addf.get_d()
        return MixedFraction(sum_w, sum_n, sum_d)

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

mixedA = MixedFraction(2, 2, 6)
mixedB = MixedFraction(1, 3, 4)
mixedA.reduce()
mixedA.print_f()
mixedB.print_f()
summf = mixedA.plus(mixedB)
summf.print_f()


