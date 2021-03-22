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
        if value > 64:
            self.V = 64

    def rashod_calc(self):
        rashod = self.V / 6.5 + 0.5
        print(f'Расход ткани для производства пальто – {rashod}')

class Suit(Clothes):
    def __init__(self, name, H):
        self.name, self.H = name, H
        print(name, H)

    def rashod_calc(self):
        rashod = 2 * self.H + 0.3
        print(f'Расход ткани для производства костюма – {rashod}')

coat_1 = Coat('Ritter', 54)
coat_1.rashod_calc()

print()

coat_1.razmer = 100
print(coat_1.razmer)

coat_1.rashod_calc()

print()

suit_1 = Suit('Stenser', 6)
suit_1.rashod_calc()
