class Complex:

    def __init__(self, r, i):
        self.r = r
        self.i = i

    def __str__(self):
        ch = '' if self.i < 0 else '+'
        return f'{self.r} {ch} {self.i}i'

    def __add__(self, other):
        return Complex(self.r + other.r, self.i + other.i)


a = Complex(3, 4)
b = Complex(7, -2)
print(a)
print(b)
print(a + b)
