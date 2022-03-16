# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def Divide(arg1, arg2):
    try:
        return arg1 / arg2
    except ZeroDivisionError:
        return "На ноль делить не положено!"


a = float(input("Введите делимое (a) = "))
b = float(input("Введите делитель (b)= "))
res = Divide(a, b)
if type(str) == "class 'float'":
    print("a/b= ", res)
else:
    print(res)
