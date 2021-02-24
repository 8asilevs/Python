file = open('primer_6.txt', 'r')

rezultat = {}

while True:
    data = file.readline()
    if not data:
        break
    data = data.split(' ')
    nazvanie = data[0][-100:-1]
    data = data[1:]
    summa = 0
    for chasy in data:
        chasy = ''.join([cifra for cifra in chasy if cifra in '0123456789'])
        if not chasy:
            continue
        summa += int(chasy)
    rezultat.update({nazvanie: summa})

print(rezultat)

file.close()