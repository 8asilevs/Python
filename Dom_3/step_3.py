def my_func(x, y, z):
    list = [int(x), int(y), int(z)]
    return sum(list) - min(list)

a, b, c = input('Введите три числа через запятую').split(', ')

rezultat = my_func(a, b, c)

print(f'Сумма двух наибольших чисел – {rezultat}')