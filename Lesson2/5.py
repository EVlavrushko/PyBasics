# Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает.
# У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них.
my_list = [7, 5, 3, 3, 2]
print("Исходный список рейтингов: ", my_list)
my_list.append(int(input("Введите новый рейтинг:")))
my_list.sort(reverse=True)
print("Итоговый список рейтнгов: ", my_list)