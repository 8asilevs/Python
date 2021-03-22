file = open('primer_5.txt', 'w')

file.write('1 1 2 3 5 8 13 21 34 55 89')

file.close()

file = open('primer_5.txt', 'r')

data = file.read()
chisla = data.split(' ')

summa = 0

for chislo in chisla:
    summa += int(chislo)

print(f'Сумма чисел в файле – {summa}')

file.close()

#import os
#os.remove('primer_5.txt')
