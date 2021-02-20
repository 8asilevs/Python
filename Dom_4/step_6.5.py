from itertools import cycle

chisla = [10, 15, 32, 5, 44, 13, 7, 98]

gen_chisla = cycle(chisla)

i = 1

for num in gen_chisla:
    print(num)
    if i > 16:
        break
    i += 1
