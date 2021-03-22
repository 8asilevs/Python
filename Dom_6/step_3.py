class Worker:
    def __init__(self, name, surname, position, **income):
        self.name, self.surname = name, surname
        self.position, self._income = position, income

class Position(Worker):
    def get_full_name(self):
        print(f'Полное имя сотрудника – {self.name} {self.surname}')

    def get_total_income(self):
        total_income = self._income['wage'] + self._income['bonus']
        print(f'Суммарный доход сотрудника – {total_income}')

position_1 = Position('Тимур', 'Карасёв', 'джуниор', wage = 70, bonus = 5)
position_2 = Position('Ульяна', 'Шувалова', 'миддл', wage = 100, bonus = 15)

position_1.get_full_name()
print(f'Должность сотрудника – {position_1.position}')
position_1.get_total_income()

print()

position_2.get_full_name()
print(f'Должность сотрудника – {position_2.position}')
position_2.get_total_income()
