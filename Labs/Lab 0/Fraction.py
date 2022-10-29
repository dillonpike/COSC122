class Fraction(object):
    '''Defines a Fraction type that has an integer numerator and a non-zero integer denominator'''

    def __init__(self, num=0, denom=1):
        '''Creates a new Fraction with numberator num and denominator denom'''
        self.numerator = num
        if denom != 0:
            self.denominator = denom
        else:
            raise ZeroDivisionError

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __eq__(self, other):
        return self.numerator / self.denominator == other.numerator / other.denominator

    def __repr__(self):
        """Repr"""
        return f"Fraction({self.numerator}, {self.denominator})"

class ReducedFraction(Fraction):   # is a sub-class of the Fraction class

    def __init__(self, numerator=0, denominator=1):
        super().__init__(numerator, denominator)  # explicitly use parent/super class __init__()
        self.__reduce__()

    def __reduce__(self):
        """Reduce"""
        divisor = find_gcd(self.numerator, self.denominator)
        self.numerator //= divisor
        self.denominator //= divisor

    def __add__(self, other):
        """Add"""
        result = Fraction.__add__(self, other)
        reduced_result = ReducedFraction(result.numerator, result.denominator)
        return reduced_result

    def __mul__(self, other):
        """Mul"""
        result = Fraction.__mul__(self, other)
        reduced_result = ReducedFraction(result.numerator, result.denominator)
        return reduced_result

    def __repr__(self):
        """Repr"""
        return f"ReducedFraction({self.numerator}, {self.denominator})"

class MixedNumber:
    """Ahhh"""
    def __init__(self, integer, fraction):
        """Init"""
        self.integer = integer
        self.fraction = ReducedFraction(fraction.numerator, fraction.denominator)

    def __repr__(self):
        """Repr"""
        return f"MixedNumber({self.integer}, {repr(self.fraction)})"

    def __str__(self):
        """Str"""
        return f"{self.integer} and {self.fraction}"

    def __add__(self, other):
        """Add"""
        fraction = ReducedFraction.__add__(self.fraction, other.fraction)
        integer = self.integer + other.integer + fraction.numerator // fraction.denominator
        fraction.numerator -= (fraction.numerator // fraction.denominator) * fraction.denominator
        return MixedNumber(integer, fraction)


def find_gcd(num1, num2):
    """
    Returns the Greatest Common Divisor (GCD) of num1 and num2.
    Assumes num1 and num2 are positive integers.
    """
    smaller = min(num1, num2)
    for i in range(smaller, 1, -1):
        if num1 % i == 0 and num2 % i == 0:
            return i
    return 1

mixed_num = MixedNumber(3, Fraction(4, 6))
print(mixed_num)

fraction_1 = Fraction(3, 4)
fraction_2 = Fraction(4, 6)
mixed_num_1 = MixedNumber(2, fraction_1)
mixed_num_2 = MixedNumber(1, fraction_2)
print(mixed_num_1 + mixed_num_2)


x = MixedNumber(3, Fraction(1, 3))
y = MixedNumber(-1, Fraction(2, 5))
z = x + y
print(z)
print(repr(z))
