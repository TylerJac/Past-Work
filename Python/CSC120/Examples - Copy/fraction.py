class Fraction:
    def __init__(self, numerator, denominator):
        if not (isinstance(numerator, int) and isinstance(denominator, int)):
            raise TypeError("numerator and denominator must be int.")
        if denominator == 0:
            raise ValueError("Dived by zero error.")
        if denominator > 0:
            self.__numerator = numerator
            self.__denominator = denominator
        else:
            self.__numerator = -numerator
            self.__denominator = -denominator
        self.reduce()

    def __str__(self):
        if self.__denominator == 1:
            return str(self.__numerator)
        return f"{self.__numerator}/{self.__denominator}"

    def __repr__(self):
        return f"Fraction(numerator={self.__numerator}, denominator={self.__denominator})"

    def get_numerator(self):
        return self.__numerator

    def get_denominator(self):
        return self.__denominator

    def set_numerator(self, new_numerator):
        if not (isinstance(new_numerator, int)):
            raise TypeError("numerator must be int.")
        self.__numerator = new_numerator

    def set_denominator(self, new_denominator):
        if not (isinstance(new_denominator, int)):
            raise TypeError("denominator must be int.")
        self.__numerator = new_denominator

    def reduce(self):
        gcd = self.__calc_gcd()

        self.__numerator = self.__numerator // gcd
        self.__denominator = self.__denominator // gcd

    def __calc_gcd(self):
        a = max(abs(self.__numerator), abs(self.__denominator))
        b = min(abs(self.__numerator), abs(self.__denominator))

        while b != 0:
            temp = b
            b = a % b
            a = temp

        return a

    def __neg__(self):
        return Fraction(-self.__numerator, self.__denominator)

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("right side operand must be of type Fraction.")
        numerator = self.__numerator * other.get_denominator() + other.get_numerator() * self.__denominator
        denominator = self.__denominator * other.get_denominator()
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("right side operand must be of type Fraction.")
        return self + -other

    def __mul__(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError("right side operand must be of type 'int' or Fraction.")
        if isinstance(other, int):
            numerator = self.__numerator * other
            denominator = self.__denominator
        else:
            numerator = self.__numerator * other.get_numerator()
            denominator = self.__denominator * other.get_denominator()

        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError("right side operand must be of type 'int' or Fraction.")
        if isinstance(other, int):
            if other == 0:
                raise ValueError("Divided by zero error.")
            numerator = self.__numerator
            denominator = self.__denominator * other
        else:
            if other.get_numerator() == 0:
                raise ValueError("Divided by zero error.")
            numerator = self.__numerator * other.get_denominator()
            denominator = self.__numerator * other.get_numerator()

        return Fraction(numerator, denominator)

    def __eq__(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError("right side operand must be of type 'int' or Fraction.")
        if isinstance(other, int):
            return self.__numerator == self.__denominator * other
        else:
            return self.__numerator * other.get_denominator() == self.__numerator * other.get_numerator()

    def __ne__(self, other):
        return not self == other

    def __lt__(self, other):
        if not isinstance(other, (int, Fraction)):
            raise TypeError("right side operand must be of type 'int' or Fraction.")
        if isinstance(other, int):
            return self.__numerator < self.__denominator * other
        else:
            return self.__numerator * other.get_denominator() < self.__numerator * other.get_numerator()

    def __le__(self, other):
        return self == other or self < other

    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other
