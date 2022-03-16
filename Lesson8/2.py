# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class Zerodev(Exception):
    """Класс деления на ноль"""
    def __init__(self, txt="На ноль делить не положено!"):
        self.txt = txt
        super().__init__(self.txt)

err = True
while err:
    try:
        A = int(input("Ввести делимое A: "))
        B = int(input("Ввести делитель B: "))
        err = False
    except ValueError:
        print("Ввод некорректен")
try:
    if B==0:
        raise Zerodev
    print("A/B = ", A/B)
except Zerodev:
    print("На ноль делить не положено!")
