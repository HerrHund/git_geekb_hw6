# Реализуйте базовый класс Car.

# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). 
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, 
# остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed. 
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

# Создайте экземпляры классов, передайте значения атрибутов. 
# Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.


class Car:
    # atributes
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    # methods
    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'

class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


Bmw = SportCar(100, 'Red', 'BMW', False)
Tavria = TownCar(30, 'White', 'TAVRIA', False)
Lanos = WorkCar(70, 'Rose', 'Lanos', True)
Toyota = PoliceCar(110, 'Blue',  'TOYOTA', True)
print(Lanos.turn_left())
print(f'When {Tavria.turn_right()}, then {Bmw.stop()}')
print(f'{Lanos.go()} with speed exactly {Lanos.show_speed()}')
print(f'{Lanos.name} is {Lanos.color}')
print(f'Is {Bmw.name} a police car? {Bmw.is_police}')
print(f'Is {Lanos.name}  a police car? {Lanos.is_police}')
print(Bmw.show_speed())
print(Tavria.show_speed())
print(Toyota.police())
print(Toyota.show_speed())

