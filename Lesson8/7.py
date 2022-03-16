# Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    def __init__(self, x, y):  # конструктор класса
        self.x = x
        self.y = y

    def __add__(self, other):  # перегружен "+"
        return Complex(self.x + other.x, self.y + other.y)

    def __mul__(self, other):   # перегружен "*"
        return Complex(self.x * other.x - self.y * other.y, self.x * other.y + other.x * self.y)

    def __str__(self):  # преобразование объекта в строку
        return str(self.x) + ' + ' + str(self.y) + 'j'

a = Complex(3, 7)
b = Complex(2, -1)
c = a + b
d = a*b
print("a =", a, "; b =", b)
print("a+b = ", a+b)
print("a*b = ", a*b)