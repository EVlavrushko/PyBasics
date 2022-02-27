# Реализуйте базовый класс Car.
# у класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
# опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
# добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
# для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Вызовите методы и покажите результат.

class Car:
    # Конструктор
    def __init__(self, s, c, n, p):
        self.speed = s
        self.color = c
        self.name = n
        self.is_police = p
        pass

    def go(self):
        print(f"Машина {self.name} поехала.")

    def stop(self):
        print(f"Машина {self.name} остановилась.")

    def turn(self, direction):
        print(f"Машина {self.name} повернула", direction)

    def show_speed(self):
        print(f"скорость машины {self.name}:", self.speed)

class TownCar(Car):
    def show_speed(self):
        print(f"скорость машины {self.name}:", self.speed)
        if self.speed > 60:
            print("Максимальная скорость превышена!!!")

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        print(f"скорость машины {self.name}:", self.speed)
        if self.speed > 40:
            print("Максимальная скорость превышена!!!")

class PoliceCar(Car):
    pass

Car1 = TownCar(60,"Желтый", "KIA", False)
Car2 = SportCar(120,"Красный", "Ferrari", False)
Car3 = WorkCar(60,"Белый", "Fiat", False)
Car4 = PoliceCar(80,"Синий", "Ford", True)

Car1.go()
Car2.go()
Car3.go()
Car4.go()

Car1.turn("Направо")
Car2.turn("Налево")
Car3.turn("Назад")
Car4.turn("Полицейский разворот")

Car1.show_speed()
Car2.show_speed()
Car3.show_speed()
Car4.show_speed()

Car1.stop()
Car2.stop()
Car3.stop()
Car4.stop()
