"""
Реализуйте базовый класс Car.
● у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А
также методы: go, stop, turn(direction), которые должны сообщать, что машина
поехала, остановилась, повернула (куда);
● опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
● добавьте в базовый класс метод show_speed, который должен показывать текущую
скорость автомобиля;
© geekbrains.ru 19
● для классов TownCar и WorkCar переопределите метод show_speed. При значении
скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о
превышении скоро
"""


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return self.name + ' поехала'

    def stop(self):
        return self.name + ' остановилась'

    def turn(self, direction):
        return self.name + '  остановилась ' + direction

    def show_speed(self):
        return 'Ваша скорость ', self.speed


class TownCar(Car):
    def show_speed(self):

        if self.speed > 60:
            return 'Привышение скорости, Остановитесь!'
        else:
            return 'Скорость нормальная' + self.name



class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return 'Привышение скорости, Остановитесь!' + self.name
        else:
            return 'Скорость нормальная' + self.name


class PoliceCar(Car):
    pass

class SportCar(Car):
    pass


town = TownCar('mazda', 90, 'blue', False)
print(town.go(), town.show_speed(), town.turn('повернула на право'), town.stop())

sport = SportCar('Bugatti', 980, 'black', False)
print(sport.go(), sport.show_speed(), sport.turn('повернула на право'), sport.stop())

work = WorkCar('tractor', 30, 'yellow', False)
print(work.go(), work.show_speed(), work.turn('повернула на лево'), work.stop())

police = PoliceCar('lada', 40, 'whight', True)
print( work.go(), work.show_speed(), work.turn('повернула на лево'))
