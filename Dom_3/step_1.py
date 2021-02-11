def dividing(delimoe, delitel):
    if delitel == 0:
        return 'ОШИБКА ДЕЛЕНИЯ НА НОЛЬ'
    else:
        return delimoe/delitel

a = int(input('Введите первое число'))
b = int(input('Введите второе число'))

rezultat = dividing(a, b)

print(f'Первое число, делённое на второе, даст результат – {rezultat}')