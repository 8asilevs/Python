slova = input('Введите слова, разделённые пробелом (фразу)')

slova_separated = slova.split( )

for i in enumerate(slova_separated, 1):
    i = list(i)
    if len(i[1]) > 10:
        i[1] = i[1][0:10]
    print(i)
