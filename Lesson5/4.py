# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

Digits = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре", "Five": "Пять", "Six": "Шесть",
          "Seven": "Семь", "Eight": "Восемь", "Nine": "Девять", "Ten": "Десять"}

f = open("text_4.txt", 'r', encoding="utf-8")
f2 = open("text_4-result.txt", 'w', encoding="utf-8")

for line in f:
    Dig = line.split()
    print(Dig[0], "замена на" , Digits[Dig[0].capitalize()])
    Dig[0] = Digits[Dig[0].capitalize()]
    f2.write(" ".join(Dig)+"\n")

f.close()
f2.close()
