# Для чисел в пределах от 20 до 240 найти числа, кратные 20 или 21. Решите задание в одну строку.
# Подсказка: используйте функцию range() и генератор.
#result = [i for i in range( 20 , 241 ) if i%20 == 0]
print("Числа от 20 до 240, кратные 20: ", [i for i in range( 20 , 241 ) if i%20 == 0] )
print("Числа от 20 до 240, кратные 21: ", [i for i in range( 20 , 241 ) if i%21 == 0] )