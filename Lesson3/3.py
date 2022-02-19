# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.

def my_func(a, b, c):
    arguments = [a, b, c]
    try:
        arguments.sort(reverse=True)
        print("Сумма 2 максимальных аргументов: ", arguments[0] + arguments[1])
    except TypeError:
        print("нельзя сложить элементы разных типов")


data = input("Введите 3 аргумента через пробел: ").split()
for el in range(len(data)):
    try:
        data[el] = float(data[el])
    except ValueError:
        data[el] = data[el]

my_func(data[0], data[1], data[2])
