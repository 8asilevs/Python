class Cell:
    def __init__(self, stars):
        self.stars, self.dlina = stars, len(stars)
        if self.stars == 'Пусто':
            self.dlina = 0

    def __str__(self):
        return self.stars

    def to_stars(self, chislo):
        if chislo < 0:
            print('ОШИБКА! Результат меньше нуля')
            rezultat = 'Пусто'
        elif chislo == 0:
            print('Результат отсутствует')
            rezultat = 'Пусто'
        elif chislo > 0:
            rezultat = '*'
            if chislo > 1:
                for i in range(chislo-1):
                    rezultat += '*'
        return Cell(rezultat)

    def __add__(self, other):
        summa = self.dlina + other.dlina
        return self.to_stars(summa)

    def __sub__(self, other):
        raznost = self.dlina - other.dlina
        return self.to_stars(raznost)

    def __mul__(self, other):
        proizvedevie = self.dlina * other.dlina
        return self.to_stars(proizvedevie)

    def __truediv__(self, other):
        if other.dlina == 0:
            chastnoe = 0
        else:
            chastnoe = round(self.dlina / other.dlina)
        return self.to_stars(chastnoe)

    def make_order(self, n):
        dlina = self.dlina
        if dlina < 1 or n < 1:
            print('Недопустимые значения на входе функции')
        elif dlina >= 1:
            stroka = ''
            if dlina > 1 and dlina <= n:
                for i in range(dlina):
                    stroka += '*'
            elif dlina > 1 and dlina > n:
                while dlina >= n:
                    for i in range(n):
                        stroka += '*'
                    stroka += '\n'
                    dlina -= n
                if dlina >= 1:
                    for i in range(dlina):
                        stroka += '*'
        print(stroka)


cell_1 = Cell('**')

cell_2 = Cell('***')

cell_3 = cell_1 + cell_2
print(f'Клетка 3:\n{cell_3}')
print()

cell_4 = cell_1 - cell_2
print(f'Клетка 4:\n{cell_4}')
print()

cell_5 = Cell('*****')

cell_6 = cell_3 - cell_5
print(f'Клетка 6:\n{cell_6}')
print()

cell_7 = cell_2 - cell_1
print(f'Клетка 7:\n{cell_7}')
print()

cell_8 = cell_5 + cell_6
print(f'Клетка 8:\n{cell_8}')
print()

cell_9 = cell_1 * cell_5
print(f'Клетка 9:\n{cell_9}')
print()

cell_10 = cell_4 * cell_5
print(f'Клетка 10:\n{cell_10}')
print()

cell_11 = cell_9 / cell_1
print(f'Клетка 11:\n{cell_11}')
print()

cell_12 = cell_9 / cell_2
print(f'Клетка 12:\n{cell_12}')
print()

cell_13 = cell_9 / cell_6
print(f'Клетка 13:\n{cell_13}')
print()

print(cell_9.dlina)
print()
cell_9.make_order(13)
print()
cell_9.make_order(10)
print()
cell_9.make_order(7)
print()

print(cell_12.dlina)
cell_12.make_order(1)
print()

cell_14 = Cell('******************************')

print(cell_14.dlina)
cell_14.make_order(7)
print()

cell_14.make_order(6)
print()

