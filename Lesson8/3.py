# Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Запрашивать у пользователя данные и заполнять список необходимо только числами.
# Класс-исключение должен контролировать типы данных элементов списка.

class Digcheck(Exception):
    """Класс проверки ввода числа"""
    def __init__(self, d):
        self.data = d
    def __str__(self):
        return f"Введенные данные '{self.data}' не являются числом"

Result = []
while True:
    data = input("Введите число, или stop для выхода: ")
    if "stop" in data:
        break
    try:
        if data.isdigit():
            Result.append(data)
        else:
            raise Digcheck(data)
    except Digcheck as err:
        print(err)


print("Введенные числа:", Result)