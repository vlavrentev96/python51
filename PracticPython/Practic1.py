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


