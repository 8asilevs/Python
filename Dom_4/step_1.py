from sys import argv

name, vyrabotka, stavka, premiya = argv

def zarplata(vyr, stav, prem):
    vyr, stav, prem = int(vyr), int(stav), int(prem)
    money = (vyr * stav + prem)
    return money

print("Выработка – ", vyrabotka)
print("Ставка – ", stavka)
print("Премия – ", premiya)
print("Зарплата – ", zarplata(vyrabotka, stavka, premiya))