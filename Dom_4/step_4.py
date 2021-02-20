chisla = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

list_unik = []

max = len(chisla)

for i in range(max):
    list_unik.append(True)

for i in range(max):
    for j in range(max):
        if j == i:
            pass
        elif chisla[i] == chisla[j]:
            list_unik[i] = False
            break

list_new = [x for x, y in zip(chisla, list_unik) if y == True]

print(list_new)
