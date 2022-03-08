# Создать текстовый файл (не программно), сохранить в нём несколько строк,
# выполнить подсчёт строк и слов в каждой строке.

strcount = 0
wordcount = 0
with open("my_file2.txt", 'r', encoding="utf-8") as f:
    for line in f:
        strcount += 1
        wordcount = wordcount + len(line.split())
print(f"В файле всего {strcount} строк и {wordcount} слов")
