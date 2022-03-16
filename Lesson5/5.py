# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
import random

sum = 0
spisok = [random.randint(0, 100) for i in range(random.randint(2, 20))]
with open("my_file5.txt", 'w', encoding="utf-8") as f:
    f.write(" ".join(map(str, spisok)) + "\n")
for dig in spisok:
    sum = sum + int(dig)
print("Сумма чисел в файле = ", sum)