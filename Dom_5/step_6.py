file = open('primer_6.txt', 'r')

rezultat = {}

while True:
    data = file.readline()
    if not data:
        break
    data = data.split(' ')
    nazvanie = data[0][-100:-1]   #название предмета без двоиточия в конце
    data = data[1:]     #данные (о часах) – это всё, что идёт после названия
    summa = 0
    for chasy in data:
        chasy = ''.join([cifra for cifra in chasy if cifra in '0123456789'])
        #оставляем только числа, без разделения часов на лекционные,
        # практические или лабораторные
        if not chasy:
            continue
        #if срабатывает, если в исходных данных на соответствующем месте было
        # тире
        summa += int(chasy)
    rezultat.update({nazvanie: summa})

print(rezultat)

file.close()
