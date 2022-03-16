# Реализовать класс Stationery (канцелярская принадлежность).
# определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение «Запуск отрисовки»;
# создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
# в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить уникальное сообщение;
# создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.
class Stationery:
    # Конструктор
    def __init__(self, t):
        self.title = t

    def draw(self):
        print(self.title, "рисует прекрасно")


class Pen(Stationery):
    def draw(self):
        print(self.title, "пишет прекрасно")


class Pencil(Stationery):
    def draw(self):
        print(self.title, "чертит прекрасно")


class Handle(Stationery):
    def draw(self):
        print(self.title, "красит неплохо")


P1 = Pen("Parker")
P2 = Pencil("Koh-I-Noor")
P3 = Handle("Ikea")

P1.draw()
P2.draw()
P3.draw()
