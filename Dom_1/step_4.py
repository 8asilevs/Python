num = int(input('Введите целое положительное число.'))

max = 0

while num >= 10:
    i = num%10
    num = (num - i)/10
    if i > max:
        max = i

max = int(max)

print(f'Самая большая цифра в данном числе – {max}')