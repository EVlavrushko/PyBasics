# Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц: 3 на 2, 3 на 3, 2 на 4.
# 31    32         3    5    32        3    5    8    3
# 37    43         2    4    6         8    3    7    1
# 51    86        -1   64   -8
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с первым элементом
# первой строки второй матрицы и т.д.

class Matrix:
    def __init__(self, m):
        self.matrix = m

    def __str__(self):
        res = ""
        for i in self.matrix:
            res = res + " ".join(map(str, i)) + "\n"
        return res

    def __add__(self, other):
        maxi = max(len(self.matrix), len(other.matrix))
        maxj = max(len(self.matrix[0]), len(other.matrix[0]))
        zero = [[0 for j in range(maxj)] for i in range(maxi)]
        for i in range(len(zero)):
            for j in range(len(zero[0])):
                m1 = 0 if ((i >= len(self.matrix)) or (j >= len(self.matrix[0]))) else self.matrix[i][j]
                m2 = 0 if ((i >= len(other.matrix)) or (j >= len(other.matrix[0]))) else other.matrix[i][j]
                zero[i][j] = m1 + m2
        return Matrix(zero)


m1 = Matrix([[1, 2, 3, 10], [4, 5, 6, 10], [7, 8, 9, 10]])
m2 = Matrix([[11, 22, 33], [44, 55, 66], [77, 88, 99], [77, 88, 99]])

print("Первая матрица:\n", m1, sep="", end="")
print("Вторая матрица:\n", m2, sep="", end="")
print("Сумма матриц:\n", m1 + m2, sep="", end="")
