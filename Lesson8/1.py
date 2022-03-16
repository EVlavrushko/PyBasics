# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
# Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.
class Date:
    def __init__(self, d,m,y):
        if not m:
            raise Exception()
        self.day = d
        self.month = m
        self.year = y

    @classmethod
    def setdate(cls, data):
        try:
            d,m,y = map(int,data.split("-"))
            if cls.Val_Date(d, m, y):
                raise Exception(cls.Val_Date(d, m, y))
            return cls(d, m, y)
        except ValueError:
            print("Дата введена неверно")


    @staticmethod
    def Val_Date(d,m,y):
        res = 0
        if d < 1 or d > 31:
            res = "Число должно быть в диапазоне от 1 до 31."
        if m < 1 or m > 12:
            res = "Месяц должен быть в диапазоне от 1 до 12."
        if y < 1 or y > 2022:
            res = "Год должен быть в диапазоне от 1 до 2022."
        return res

i=Date.setdate("01-12-1697")
print(i)
print(i.day)
print(i.month)
print(i.year)

