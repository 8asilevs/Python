def summirovanie(list_chisel):
    summa = 0
    for slagaemoe in list_chisel:
        summa += int(slagaemoe)
    print(f'Сумма всех введённых чисел – {summa}')

chisla = input('Введите числа, разделённые пробелом').split(' ')

summirovanie(chisla)

eschyo_chisla = input('Введите ещё числа, разделённые пробелом').split(' ')

if eschyo_chisla == ['x']:
    pass
elif eschyo_chisla[-1] == 'x':
    del eschyo_chisla[-1]
    summirovanie(chisla + eschyo_chisla)
else:
    summirovanie(chisla + eschyo_chisla)
