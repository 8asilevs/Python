from functools import reduce

l = [i for i in range(100, 1001) if i % 2 == 0]

def umnozh(a, b):
    return a * b

print(reduce(umnozh, l))