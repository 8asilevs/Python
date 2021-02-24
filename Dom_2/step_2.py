slovo = list(input('Введите слово'))

i = 1
max = len(slovo)//2

while i < max:
    slovo[i], slovo[i-1] = slovo[i-1], slovo[i]
    i += 2

print(slovo)