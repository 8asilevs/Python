list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 76, 123, 55, 100]

list_2 = list_1[1:]

list_3 = [j for i, j in zip(list_1, list_2) if j > i]

print(list_3)
