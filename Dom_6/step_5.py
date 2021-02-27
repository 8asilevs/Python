class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой {self.title}')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом {self.title}')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки маркером {self.title}')

stationery_1 = Stationery('Noname')
stationery_1.draw()

pen_1 = Pen('Pilot')
pen_1.draw()

pencil_1 = Pencil('Конструктор')
pencil_1.draw()

handle_1 = Handle('Stabilo')
handle_1.draw()




