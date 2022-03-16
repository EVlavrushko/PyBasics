# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class OrgSklad:
    def __init__(self,s=0):
        self.size = s
        self.Totallist = []
        self.Typelist = {}

    def Teh_in(self,teh, q):
        if not self.Typelist.get(teh.type) == None:
            self.Typelist[teh.type] +=q
        else:
            self.Typelist.update({teh.type : q})
        for i in range(q):
            self.Totallist.append(teh)

    def Teh_out(self,teh):
        if self.Totallist.count(teh)>0:
            self.Totallist.remove(teh)
            self.Typelist[teh.type]-=1

        else:
            raise Exception("Требуемого обрудования нет на складе")

class Digcheck(Exception):
    def __init__(self, d):
        self.data = d
    def __str__(self):
        return f"Введенные данные '{self.data}' не являются числом"



class Orgteh:
    def __init__(self,b,m,p):
        self.brand = b
        self.model = m
        self.price = p

class Printer(Orgteh):
    def __init__(self,b,m,p):
        self.brand = b
        self.model = m
        self.price = p
        self.type = "Принтер"

class Scanner(Orgteh):
    def __init__(self,b,m,p):
        self.brand = b
        self.model = m
        self.price = p
        self.type = "Сканер"

class Xerox(Orgteh):
    def __init__(self,b,m,p):
        self.brand = b
        self.model = m
        self.price = p
        self.type = "Ксерокс"

sklad = OrgSklad(20)

p1 = Printer("Canon","X500",15000)
s1 = Scanner("Epson","z8",10000)
x1 = Xerox("Minolta","Tram8",20000)

sklad.Teh_in(p1,1)
sklad.Teh_in(s1,2)
sklad.Teh_in(x1,1)

Type = input("Введите тип принимаемого оборудования (P-Принтер,S-Сканнер, X-Ксерокс):")
str = input("Введите через пробел данные для приема оборудования на склад ('Производитель' 'модель' 'цена' 'количество'):\n").split()

try:
    if str[3].isdigit():
        str[3] = int(str[3])
        if Type == "P":
            sklad.Teh_in(Printer(str[0], str[1], str[2]), str[3])
        elif Type == "S":
            sklad.Teh_in(Scanner(str[0], str[1], str[2]), str[3])
        elif Type == "X":
            sklad.Teh_in(Xerox(str[0], str[1], str[2]), str[3])
        else:
            print("Ввод некорректный")
    else:
        raise Digcheck(str[3])
except Digcheck as err:
    print(err)

sklad.Teh_in(p1,1)

sklad.Teh_out(s1)

print("Количество типов единиц: ", sklad.Typelist)
print("Список всех единиц и параметров:")

for en in sklad.Totallist:
    print(en.brand, en.model , en.price)

