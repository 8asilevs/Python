class Clothes:
    def __init__(self, name, chislo):
        self.name, self.chislo = name, chislo
        print(name, chislo)

class Coat(Clothes):
    def __init__(self, name, V):
        self.name, self.V = name, V
        print(name, V)

    @property
    def razmer_property(self):
        return self.V

    @razmer_property.setter
    def razmer(self, value):
        self.V = value + 1

    def rashod_calc(self):
        rashod = self.V / 6.5 + 0.5
        print(rashod)

class Suit(Clothes):
    def __init__(self, name, H):
        self.name, self.H = name, H
        print(name, H)

    def rashod_calc(self):
        rashod = 2 * self.H + 0.3
        print(rashod)

coat_1 = Coat('Ritter', 54)

coat_1.rashod_calc()

print()

coat_1.razmer = 55
print(coat_1.razmer)

print()

suit_1 = Suit('Stenser', 6)

suit_1.rashod_calc()
