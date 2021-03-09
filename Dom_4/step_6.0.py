from sys import argv

name, nachalo = argv

nachalo = int(nachalo)

def generator(n=nachalo):
    while True:
        yield n
        n += 1

for num in generator():
    print(num)
    if num >= 10:
        break