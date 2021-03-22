def my_func(x, y, z):
    list = [int(x), int(y), int(z)]
    return sum(list) - min(list)

a, b, c = input('Введите три числа через пробел').split(' ')

print(f'Сумма двух наибольших введённых чисел – {my_func(a, b, c)}')
