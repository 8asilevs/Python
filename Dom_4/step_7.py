i, factorial = 1, 1

n = int(input('Введите целое положительное число'))

def fact(the_end=n):
    global i
    global factorial
    while i <= the_end:
        factorial *= i
        i += 1
        yield factorial

#print(next(fact()))
#print(next(fact()))
#print(next(fact()))
#print(next(fact()))
#print(next(fact()))

for el in fact():
    print(el)