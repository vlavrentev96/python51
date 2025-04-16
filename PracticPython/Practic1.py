# #Модуль 2. Операторы ветвлений. Часть 2. Задание 1.
# a = int(input("Введите число в секундах прошедшее с начала : "))
# b = input("Выберите формат - 1 = часы, \n 2 = минуты, \n 3 = секунды: ")
# c = 86400
# if b == "1":
#     hours = ((c - a) // 3600)
#     print(f"Оставшееся часов до окончания суток: {hours} ")
# elif b == "2":
#     minutes = (c - a) // 60
#     print(f"Минуты: {minutes}")
# elif b == "3":
#     seconds = c - a
#     print(f"Осталось секунд: {seconds}")
# #Задание 2.
# a = int(input("Введите диаметр окружности: "))
# b = input("Выберите площадь или периметр - 1 = площадь, \n 2 = периметр: ")
# radius = a / 2
# pi = 3.14
# if b == "1":
#     area = pi * radius * radius
#     print(f"Площадь = {area}")
# elif b == "2":
#     perimeter = 2 * pi * radius
#     print(f"Периметр = {perimeter}")
# else:
#     print("Некорректное значение!")
#Задание 3
# price = float(input("Введите стоимость приставки: "))
# kol_vo = int(input("Введите кол-во приставок: "))
# discount = float(input("Введите процент скидки: "))
# vibor = input("Что считаем? (1 - общая сумма, \n 2- стоимость одной): ")
# discount_rate = discount / 100
#
# if vibor == "1":
#     sum = price * kol_vo
#     sum_with_discount = sum * (1 - discount_rate)
#     print("Общая сумма приставок с учетом скидок =", sum_with_discount)
# elif vibor == "2":
#     price_with_discount = price * (1 - discount_rate)
#     print("Цена одной приставки со скидкой =", price_with_discount)
# else:
#     print("Ошибка! Выберите число 1 или 2!")
#Задание 4
# file_gb = float(input("Введите размер файла (в ГБ): "))
# speed_bit = float(input("Введите скорость интернета (в битах/с): "))
# vibor = input("Что считать? (1 - часы, \n 2 - минуты, \n 3 - секунды): ")
#
# file_bit = file_gb * 8 * 1000000000
#
# time_seconds = file_bit / speed_bit
#
# if vibor == "1":
#     time_hours = time_seconds / 3600
#     print("Время в часах =", time_hours)
# elif vibor == "2":
#     time_minutes = time_seconds / 60
#     print("Время в минутах=", time_minutes)
# elif vibor == "3":
#     print("Время в секундах=", time_seconds)
# else:
#     print("Ошибка! Выберите значение из предложенных!")
# #Задание 5
# hours = int(input("Введите количество часов: "))
#
# if 0 <= hours < 6:
#     print("GoodNight")
# elif 6 <= hours < 13:
#     print("GoodMorning")
# elif 13 <= hours < 17:
#     print("GoodDay")
# elif 17 <= hours < 24:
#     print("GoodEvening")
# else:
#     print("Ошибка! Часы должны быть от 0 до 23")
#ОПЕРАТОРЫ ВЕТВЛЕНИЙ. ЧАСТЬ 3.
# #Задание 1
# number = int(input("Введите шестизначное число: "))
# if 100000 <= number <= 999999:
#     num_str = str(number)
#     sum_first3 = int(num_str[0]) + int(num_str[1]) + int(num_str[2])
#     sum_last3 = int(num_str[3]) + int(num_str[4]) + int(num_str[5])
#     if sum_first3 == sum_last3:
#         print("Число счастливое!")
#     else:
#         print("Число НЕ счастливое")
# else:
#     print("Ошибка! Введите шестизначное число")
#Задание 2
# number = int(input("Введите шестизначное число: "))
# if 100000 <= number <= 999999:
#     num_str = str(number)
#     antwort = int(num_str[5] + num_str[4] + num_str[2] + num_str[3] + num_str[1] + num_str[0])
#     print("Успех! Полученное число -", antwort)
# else:
#     print("Ошибка! Введите шестизначное число!")
# #Задание 3
# month = int(input("Введите номер месяца. Значение от 1 до 12: "))
# if 1 <= month <= 12:
#     if month == 1 or month == 2 or month == 12:
#         print("Winter!")
#     elif 3 <= month <= 5:
#         print("Spring!")
#     elif 6 <= month <= 8:
#         print("Summer!")
#     elif 9 <= month <= 11:
#         print("Autumn!")
# else:
#     print("Ошибка! Введите значение от 1 до 12!")
#Модуль 2. Операторы ветвлений. Часть 1.
# #Задание 1.
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# vibor = input("Что вычислить? (1 - сумма, \n 2 - произведение): ")
# if vibor == "1":
#     summa = num1 + num2 + num3
#     print("Сумма чисел:", summa)
# elif vibor == "2":
#     proizvedenie = num1 * num2 * num3
#     print("Произведение чисел:", proizvedenie)
# else:
#     print("Ошибка! Выберите 1 или 2")
# #Задание 2.
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# num3 = int(input("Введите третье число: "))
# vibor = input("Что вычислить? (1 - максимум, 2 - минимум, 3 - среднее): ")
# if vibor == "1":
#     result = max(num1, num2, num3)
#     print("Максимум:", result)
# elif vibor == "2":
#     result = min(num1, num2, num3)
#     print("Минимум:", result)
# elif vibor == "3":
#     result = (num1 + num2 + num3) / 3
#     print("Среднее:", result)
# else:
#     print("Ошибка! Выберите 1, 2 или 3")
#Задание 3.
# meters = float(input("Введите количество метров: "))
# vibor = input("Во что перевести? (1 - мили, \n 2 - дюймы, \n 3 - ярды): ")
# if vibor == "1":
#     result = meters * 0.000621371
#     print(f"{meters} метров = {result} миль")
# elif vibor == "2":
#     result2 = meters * 39.3701
#     print(f"{meters} метров = {result2} дюймов")
# elif vibor == "3":
#     result3 = meters * 1.09361
#     print(f"{meters} метров = {result3} ярдов")
# else:
#     print("Ошибка! Выберите 1, 2 или 3")
#Модуль 2. Операторы ветвлений. Часть 1.
#Задание 1.
# number = int(input("Введите число: "))
# if number % 2 == 0:
#     print(number, "Even Number")
# else:
#     print(number, "Odd number")
#Задание 2.
# number = int(input("Введите число: "))
# if number % 7 == 0:
#     print(number, "Number is multiple 7!")
# else:
#     print(number, "Number is not multiple 7!")
#Задание 3.
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# result = max(num1, num2)
# print("Максимум:", result)
#Задание 4.
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# result = min(num1, num2)
# print("Минимум:", result)
#Задание 5.
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# vibor = input("Что вычислить? (1 - сумма, \n 2 - разница, \n 3 - среднее, \n 4 - произведение): ")
# if vibor == "1":
#     result = num1 + num2
#     print("Сумма:", result)
# elif vibor == "2":
#     result = num1 - num2
#     print("Разница:", result)
# elif vibor == "3":
#     result = (num1 + num2) / 2
#     print("Среднее:", result)
# elif vibor == "4":
#     result = num1 * num2
#     print("Произведение:", result)
# else:
#     print("Ошибка! Выберите 1, 2, 3 или 4")
#Введение в Python. Часть 3.
#Задание 1.
# digit1 = int(input("Введите первую цифру: "))
# digit2 = int(input("Введите вторую цифру: "))
# digit3 = int(input("Введите третью цифру: "))
# number = digit1 * 100 + digit2 * 10 + digit3
# print("Число:", number)
#Задание 2.
# number = int(input("Введите четырёхзначное число: "))
# if 1000 <= number <= 9999:
#     digit1 = number // 1000
#     digit2 = (number // 100) % 10
#     digit3 = (number // 10) % 10
#     digit4 = number % 10
#     antwort = digit1 * digit2 * digit3 * digit4
#     print("Успех! Произведение равно = ", antwort)
# else:
#     print("Ошибка! Введите четырёхзначное число.")
#Задание 3.
# meters = float(input("Введите количество метров: "))
# vibor = input("Во что перевести? (1 - сантиметры, \n 2 - дециметры, \n 3 - миллиметры, \n 4 - мили): ")
# if vibor == "1":
#     result = meters * 100
#     print(f"{meters} метров = {result} сантиметров")
# elif vibor == "2":
#     result2 = meters * 10
#     print(f"{meters} метров = {result2} дециметров")
# elif vibor == "3":
#     result3 = meters * 1000
#     print(f"{meters} метров = {result3} миллиметров")
# elif vibor == "4":
#     result3 = meters * 0.000621371
#     print(f"{meters} метров = {result3} миль")
# else:
#     print("Ошибка! Выберите 1, 2, 3 или 4!")
# #Задание 4.
# base = float(input("Введите размер основания: "))
# height = float(input("Введите размер высоты: "))
# antwort = (base * height) / 2
# print("Площадь треугольника =", antwort)
#Задание 5.
# number = int(input("Введите четырехзначное число: "))
# if 1000 <= number <= 9999:
#     num_str = str(number)
#     antwort = int(num_str[3] + num_str[2] + num_str[1] + num_str[0])
#     print("Успех! Полученное число -", antwort)
# else:
#     print("Ошибка! Введите шестизначное число!")
#Введение в PYTHON! Часть 2.
#Задание 1.
# print("Nothing")
# print("will work")
# print("unless you do.")
#Задание 2.
# print("“Anyone who \n    stops \n        learning is old, \n            whether at twenty or eighty” \n                Henry Ford")
#Задание 3.
# num1 = int(input("Введите первое число: "))
# num2 = int(input("Введите второе число: "))
# vibor = input("Что вычислить? (1 - сумма, \n 2 - разница, \n 3 - произведение): ")
# if vibor == "1":
#     result = num1 + num2
#     print("Сумма:", result)
# elif vibor == "2":
#     result = num1 - num2
#     print("Разница:", result)
# elif vibor == "3":
#     result = num1 * num2
#     print("Произведение:", result)
# else:
#     print("Ошибка! Выберите 1, 2, или 3!")
# Задание 4.
# value = float(input("Введите число: "))
# percent = float(input("Введите процент: "))
# antwort = (value * percent) / 100
# print("Результат:", antwort)
#Задание 5.
# width = float(input("Введите ширину прямоугольника: "))
# height = float(input("Введите высоту прямоугольника: "))
# area = width * height
# print("Площадь прямоугольника:", area)





