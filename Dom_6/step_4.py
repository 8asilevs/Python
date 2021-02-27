class Car:
    def __init__(self, speed, direction, color, name, is_police=False):
        self.speed, self.direction, self.color = speed, direction, color
        self.name, self.is_police = name, is_police

    def go(self):
        if self.speed > 0:
            print(f'Машина едет')

    def stop(self):
        if self.speed == 0:
            print(f'Машина стоит')

    def turn(self):
        if self.direction == 'none':
            print(f'Машина никуда не поворачивает, так как никуда не едет')
        elif self.direction == 'straight':
            print(f'Машина едет прямо')
        elif self.direction == 'left':
            print(f'Машина поворачивает налево')
        elif self.direction == 'right':
            print(f'Машина поворачивает направо')

    def show_speed(self):
        if self.speed == 0:
            print(f'Машина стоит на месте')
        else:
            print(f'Машина едет со скоростью {self.speed} км/ч')

class SportCar(Car):
    pass

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'ПРЕВЫШЕНИЕ ДОПУСТИМОЙ СКОРОСТИ')

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'ПРЕВЫШЕНИЕ ДОПУСТИМОЙ СКОРОСТИ')

class PoliceCar(Car):
    def __init__(self, speed, direction, color, name, is_police=True):
        super().__init__(speed, direction, color, name, is_police)

car_1 = SportCar(80, 'left', 'red', 'Porsche')
print(f'Марка машины – {car_1.name}')
print(f'Является ли машина полицейской – {car_1.is_police}')
car_1.show_speed()

print()

car_2 = TownCar(0, 'none', 'black', 'Peugeot')
print(f'Марка машины – {car_2.name}')
car_2.go()
car_2.stop()
car_2.show_speed()

print()

car_3 = TownCar(50, 'right', 'grey', 'Kia')
print(f'Марка машины – {car_3.name}')
car_3.go()
car_3.stop()
car_3.show_speed()

print()

car_4 = TownCar(70, 'straight', 'grey', 'Mazda')
print(f'Марка машины – {car_4.name}')
car_4.go()
car_4.stop()
car_4.show_speed()

print()

car_5 = WorkCar(50, 'straight', 'yellow', 'Bobcat')
print(f'Марка машины – {car_5.name}')
print(f'Является ли машина полицейской – {car_1.is_police}')
car_5.show_speed()
car_5.turn()

print()

car_6 = WorkCar(30, 'right', 'yellow', 'JCB')
print(f'Марка машины – {car_6.name}')
car_6.show_speed()
car_6.turn()

print()

car_7 = PoliceCar(80, 'left', 'blue', 'Volkswagen')
print(f'Марка машины – {car_7.name}')
print(f'Является ли машина полицейской – {car_7.is_police}')
car_7.show_speed()
car_7.turn()

print()

car_8 = PoliceCar(0, 'none', 'blue', 'Ford')
print(f'Марка машины – {car_8.name}')
print(f'Является ли машина полицейской – {car_8.is_police}')
car_8.show_speed()
car_8.turn()

