dohod = float(input('Введите размер вашего дохода.'))
ubytok = float(input('Введите размер вашего убытка.'))

if ubytok > dohod:
    print(f'Фирма работает в минус')
elif ubytok == dohod:
    print(f'Фирма работает в ноль')
else:
    pribyl = dohod - ubytok
    print(f'Фирма работает в плюс с рентабельностью {100*pribyl/dohod}%')
    shtat = float(input('Введите число ваших сотрудников.'))
    print(f'Прибыль в расчёте на одного сотрудника составляет {pribyl/shtat} '
          f'рублей')
