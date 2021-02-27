file = open('primer_1.txt', 'w')

while True:
    stroka = input('Введите строку')
    if not stroka:
        break
    file.write(stroka)
    file.write('\n')

file.close()

#import os
#os.remove('primer_1.txt')

