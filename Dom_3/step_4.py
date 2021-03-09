def my_func(x, y):
    znamenatel = 1
    i = 1
    max = -y
    while i <= max:
        znamenatel = znamenatel*x
        i += 1
    return 1/znamenatel

a = float(input('Введите действительное число (десятичную дробь)'))
b = int(input('Введите отрицательное целое число (степень)'))

print(f'Результат возведения в степень – {my_func(a, b)}')