def dividing(delimoe, delitel):
    if delitel == 0:
        return 'ОШИБКА ДЕЛЕНИЯ НА НОЛЬ'
    else:
        return delimoe/delitel

a = int(input('Введите первое число'))
b = int(input('Введите второе число'))

print(f'Частное от деления первого числа на второе – {dividing(a, b)}')
