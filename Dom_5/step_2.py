file = open('primer_2.txt', 'r')

ch_strok = 0

while True:
    data = file.readline()
    if not data:
        break
    ch_strok += 1
    ch_simvolov = len(data)
    print(f'Число символов в {ch_strok} строке – {ch_simvolov}')

print('')
print(f'Всего строк – {ch_strok}')

file.close()