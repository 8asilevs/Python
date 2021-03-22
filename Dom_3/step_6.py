def int_func(stroka):
    i = 0
    max = len(stroka)
    stroka_titled = ''
    while i < max:
        stroka_titled += stroka[i].title()
        stroka_titled += ' '
        i += 1
    print(f'Все слова с заглавной буквы – {stroka_titled}')

string = input('Введите строку').split(' ')

int_func(string)