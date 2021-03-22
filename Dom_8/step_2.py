class MyExceptions(Exception):
    def __init__(self):
        pass

try:
    delimoe = input('Введите делимое')
    delitel = input('Введите делитель')
    delimoe, delitel = int(delimoe), int(delitel)
    if delitel == 0:
        raise MyExceptions()
except MyExceptions:
    print('Результат деления – бесконечность')
else:
    print(f'Результат деления – {delimoe / delitel}')
