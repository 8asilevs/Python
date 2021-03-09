file = open('primer_3.txt', 'r')

ch_sotrud = 0
summa_okladov = 0

print(f'Получают меньше 20 тысяч:')

while True:
    data = file.readline()
    if not data:
        break
    ch_sotrud += 1
    surname, oklad = data.split(' ')
    oklad = int(oklad)
    if oklad < 20:
        print(surname)
    summa_okladov += oklad

sred_zp = summa_okladov / ch_sotrud

print('')
print(f'Средняя зарплата – {sred_zp}')

file.close()