class Matrix:
    def __init__(self, *args):
        self.data = args
        self.vysota, self.dlinna = len(self.data), len(self.data[0])
        print(f'Высота матрицы – {self.vysota}')
        print(f'Длинна матрицы – {self.dlinna}')

    def __str__(self):
        stroka = ''
        for i in range(self.vysota):
            for j in range(self.dlinna):
                stroka += str(self.data[i][j]) + ' '
            stroka += '\n'
        return stroka

    def __add__(self, other):
        summa = self.data
        slagaemoe = other.data
        for i in range(self.vysota):
            for j in range(self.dlinna):
                summa[i][j] += slagaemoe[i][j]
        return Matrix(*summa)

m_1 = Matrix([1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2])

print(m_1)

m_2 = Matrix([10, 11, 12, 13], [14, 15, 16, 17], [18, 19, 20, 21])

print(m_2)

m_3 = m_1 + m_2

print(m_3)

