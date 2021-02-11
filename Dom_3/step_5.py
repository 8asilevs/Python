def summirovanie(*kwargs):
    summa = 0
    for slagaemoe in kwargs[0]:
        summa += int(slagaemoe)
    return summa

chisla = input('Введите числа, разделённые пробелом').split(' ')
if chisla[-1] == '':
    del chisla[-1]

rezultat = summirovanie(chisla)

print(f'Сумма всех введённых чисел – {rezultat}')

eschyo_chisla = input('Введите ещё числа, разделённые пробелом').split(' ')
if eschyo_chisla[-1] == '':
    del eschyo_chisla[-1]

if eschyo_chisla == ['x']:
    pass
elif eschyo_chisla[-1] == 'x':
    del eschyo_chisla[-1]
    rezultat = summirovanie(chisla + eschyo_chisla)
    print(f'Сумма всех введённых чисел – {rezultat}')
else:
    rezultat = summirovanie(chisla + eschyo_chisla)
    print(f'Сумма всех введённых чисел – {rezultat}')