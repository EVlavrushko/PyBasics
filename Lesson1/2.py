#Пользователь вводит время в секундах. Переведите время в часы, минуты, секунды и выведите в формате чч:мм:сс. Используйте форматирование строк.
Time = int(input("Введите время в секундах (1-86400): "))
print(Time)
Hours = Time//3600
Mins = Time//60 - Hours*60
Secs = Time - Hours*3600 - Mins*60
print(f"{Hours} : {Mins} : {Secs}")
print("%d : %d : %d" % (Hours, Mins, Secs))
print("{} : {} : {}".format(Hours, Mins, Secs))