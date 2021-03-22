spisok = []

while True:
    chislo = input('Введите число')
    if chislo == 'stop':
        break
    try:
        chislo = int(chislo)
    except ValueError:
        print('Вы ввели не число')
    else:
        spisok.append(chislo)

print(spisok)
