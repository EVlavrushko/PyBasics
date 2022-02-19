# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
#
from sys import argv
script_name, Tabel, Stavka, Premia = argv
#print("Имя скрипта: ", script_name)
try:
    Tabel = float (Tabel)
    Stavka = float (Stavka)
    Premia = float (Premia)
    print("ЗП сотрудника за указанное время: ", round( (Tabel * Stavka )+Premia , 1))
except ValueError:
    print("Аргументы введены некорректно!")
