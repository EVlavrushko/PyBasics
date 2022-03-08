# Реализовать базовый класс Worker (работник).
# определить атрибуты: name, surname, position (должность), income (доход);
# последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus};
# создать класс Position (должность) на базе класса Worker;
# в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income);
# проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.
class Worker:
    # Конструктор
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {"wage": w, "bonus": b}

class Position(Worker):
    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

    def get_full_name(self):
        return self.surname + " " + self.name

Manager = Position("Иван", "Иванов", "Менеджер продаж", 25000, 10000)
Director = Position("Петр", "Петров", "Генеральный директор", 50000, 100000)

print(f"Полный доход сотрудника {Director.get_full_name()} составляет {Director.get_total_income()}")
print(f"Полный доход сотрудника {Manager.get_full_name()} составляет {Manager.get_total_income()}")
