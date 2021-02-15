"""
Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
"""



class Car:
    speed = None
    color = None
    name = None

    def __init__ (self, name, speed, color, is_police):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go (self):
        return '\nАвтомобиль завелся!\n'

    def stop (self):
        return 'двигатель остановился!!!'

    def turn_right (self):
        return f'{self.name} поворачивает на право'

    def turn_left (self):
        return f'{self.name} поворачивает на лево'


class TownCar (Car):

    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

    def show_speed(self):
        print (f'\nСкорость автомобиля {self.name}: {self.speed}')

        if self.speed > 40:
            return f'\nСкорость автомобиля {self.name} превышает допустимую скорость движения в городе!!!'
        else:
            return f'\nСкорость автомобиля {self.name} нормальная'


class SportCar (Car):
    def __init__ (self, name, speed, color, is_police):
        super ().__init__ (name, speed, color, is_police)

    def show_speed(self):
        print (f'\n\nСкорость автомобиля {self.name}: {self.speed}')


class WorkCar (Car):
    def __init__ (self, name, speed, color, is_police):
        super ().__init__ (name, speed, color, is_police)

    def show_speed(self):
        print (f'\nСкорость автомобиля {self.name}: {self.speed}')

        if self.speed > 60:
            return f'\nСкорость {self.name} превышает допустимую скорость для служебного автомобиля!!!'
        else:
            return f'\nСкорость автомобиля {self.name} нормальная'

class PoliceCar (Car):
    def __init__ (self, name, speed, color, is_police):
        super ().__init__ (name, speed, color, is_police)

    def show_speed(self):
        print (f'\nСкорость автомобиля {self.name}: {self.speed}')

    def police (self):
        if self.is_police:
            return f'\n\n{self.name} это полицейская машина!!!'
        else:
            return f'\n{self.name} это не полицейская машина'


audi = SportCar('АУДИ', 100, 'Черный', False)
oka = TownCar('ОКА', 300, 'Зеленый', False)
lada = WorkCar('ЛАДА', 69, 'Красный', True)
ford = PoliceCar('ФОРД', 113, 'Белый', True)


print(lada.turn_left())
print(f'Когда {oka.turn_right()}, то {audi.stop()}')
print(f'{lada.go()}')
print(f'{lada.name} ---- цвет автомобиля ---- {lada.color}')
print(f'\nЭто {audi.name} полицейская машина? {audi.is_police}')
print(f'Это {lada.name} полицейская машина? {lada.is_police}')
print(audi.show_speed())
print(oka.show_speed())
print(ford.police())
print(ford.show_speed())
