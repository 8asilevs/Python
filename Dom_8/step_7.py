class ComplexNumber:
    def __init__(self, ab):
        self.a, self.sign, self.b = ab.split(' ')
        if self.sign == '+':
            self.sign = 1
        else:
            self.sign = -1
        self.a, self.b = int(self.a), self.sign*int(self.b[0:-1])

    def vydacha(self, a, b):
        if b >= 0:
            return f'{a} + {b}i'
        elif b < 0:
            return f'{a} - {-b}i'

    def __str__(self):
        return self.vydacha(self.a, self.b)

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return ComplexNumber(self.vydacha(a, b))

    def __mul__(self, other):
        a = self.a * other.a
        b = self.b * other.b
        return ComplexNumber(self.vydacha(a, b))

z_1 = ComplexNumber('4 + 2i')

z_2 = ComplexNumber('5 + 3i')

z_3 = z_1 + z_2
print(f'z_3 = {z_3}')

print()

z_4 = z_1 + z_3
print(f'z_4 = {z_4}')

print()

z_5 = z_1 * z_2
print(f'z_5 = {z_5}')

print()

z_6 = ComplexNumber('-7 - 8i')

z_7 = z_1 + z_6
print(f'z_7 = {z_7}')

print()

z_8 = z_2 * z_7
print(f'z_8 = {z_8}')

print()

z_9 = z_6 * z_7
print(f'z_9 = {z_9}')
