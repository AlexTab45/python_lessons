import math #математическая библиотека

text="Давным давно в далекой галактике..."
print(len(text)) #считает символы, в т.ч. пробелы#
print(text.upper()) #переводит в заглавные буквы#
print(text.lower()) #маленькие буквы#
print(text.count("a")) #считает количество одинаковых символов#
print(text.lower().count("д")) #переводит в один формат и считает количество#
print(text.replace("Давным давно", "Вчера")) #замена текста#
print(text.replace(".", "!")) #замена текста#
print(text.replace(".", "!", 1)) #замена точки конкретной#

#нарезание на кусочки (slicing)#
print(text[0]) #выводит 1 символ#
print(text[-1])
print(text[0:13])
print(text[-12:-1]) #менять местами, т.к. -12 меньше -1#
print(text[::]) #копия текста#
print(text[::-1]) #переварачивает любую коллекцию#
print(text[::2]) #убирает каждый второй(можно3, 4 и т.д.) символ#
print(text[0:13:2]) #убирает каждый второй символ из кусочка текста#

#математические функции#
print(float("1.5")) #дробные числа#
print(bin(5)) #двоичный код символа#
print(bin(7)[2:])
print(int("3"))
print(int("101",2)) #бинарная или двоичная система#
print(int("fff",16)) #16-тиричная система#
print(int("a",16))

print(math.ceil(1.2)) #округление в большую сторону до целого числа#
print(math.floor(1.2)) #округление в меньшую сторону до целого числа#
print(round(1.2)) #округление по правилам округления#
print(round(1.3333333,2)) #округление до количества знаков после запятой#
print(pow(2, 3)) #возведение в степень#

