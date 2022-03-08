# Реализовать два небольших скрипта:
# итератор, генерирующий целые числа, начиная с указанного;
# итератор, повторяющий элементы некоторого списка, определённого заранее.
# Подсказка: используйте функцию count() и cycle() модуля itertools.
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Предусмотрите условие его завершения.
# #### Например, в первом задании выводим целые числа, начиная с 3.
# При достижении числа 10 — завершаем цикл.
# Вторым пунктом необходимо предусмотреть условие, при котором повторение элементов списка прекратится.


import itertools

from sys import argv

script_name, SN = argv


def Script1():
    try:
        Start = int(input("Введите начальное значение:"))
        Stop = int(input("Введите конечное значение: "))
    except ValueError:
        print("Аргументы введены некорректно!")
        return

    for el in itertools.count(Start):
        if el > Stop:
            break
        else:
            print(el)


def Script2(spisok):
    i = 0
    try:
        Stop = int(input("Сколько раз осуществляется перебор: "))
    except ValueError:
        print("Число введено некорректно!")
        return

    for el in itertools.cycle(spisok):
        if i > Stop:
            break
        else:
            print(el)
            i += 1


# Сама программа
spisok = ["В", "Ы", "П", "У", "С", "Т", "И", " ", "М", "Е", "Н", "Я", "!"]

try:
    SN = int(SN)
    if SN == 1:
        Script1()
    if SN == 2:
        Script2(spisok)
except ValueError:
    print("Номер скрипта введен некорректно!")
