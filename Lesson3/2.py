# Выполнить функцию, которая принимает несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы. Осуществить вывод данных о пользователе одной строкой.

def dataout(Name, Surname, Year, Email, Phone, City="Москва", ):
    print(f"{Surname} {Name} {Year} года рождения проживает в городе {City}, e-mail: {Email}, телефон: {Phone} ")

Userdata = {"Name": "Иван", "Surname": "Иванов", "Year": "1999", "City": "Санкт-Петербург", "Email": "tratata@yud.com",
            "Phone": "900"}
dataout(Name=Userdata["Name"], Surname=Userdata["Surname"], Year=Userdata["Year"], Email=Userdata["Email"],
        Phone=Userdata["Phone"])
# Город не вводится в функцию умышленно - и без ввода меняется на Москву по умолчанию
