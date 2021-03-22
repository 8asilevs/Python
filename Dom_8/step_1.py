class Date:
    def __init__(self, full_date):
        self.full_date = full_date
        print(self.full_date)

    @classmethod
    def date_extraction(cls, full_date):
        day, month, year = full_date.split('.')
        day, month, year = int(day), int(month), int(year)
        print('День, месяц и год –', day, month, year)

    @staticmethod
    def date_check(full_date):
        day, month, year = full_date.split('.')
        day, month, year = int(day), int(month), int(year)
        checklist = 0
        if day < 1 or day > 31:
            print(f'Недопустимый номер дня – {day}!')
        else:
            checklist += 1
        if month < 1 or month > 12:
            print(f'Недопустимый номер месяца – {month}!')
        else:
            checklist += 1
        if checklist == 2:
            print(f'{full_date} – это валидная дата')

date_1 = Date('07.03.2021')

date_1.date_extraction('07.03.2021')
Date.date_extraction('07.03.2021')

print()

date_1.date_check('30.20.2021')

print()

Date.date_check('404.12.2021')

print()

date_1.date_check('07.03.2021')



