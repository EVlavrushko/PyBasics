# Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента.
# Использовать функцию type() для проверки типа.
# Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.
Celoe = 98
Vesh = 98.783
Compl = complex(87, 56)
str = "Hello world"
bool = False
nnn = None
bytes = b"165187"
Spisok = [Celoe, Vesh, Compl, str, bool, nnn, bytes]
# print(Spisok)
for el in Spisok:
    print(f"Значение элемента: {el}, тип элемента {type(el)}")
