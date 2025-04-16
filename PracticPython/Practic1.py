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
price = float(input("Введите стоимость приставки: "))
kol_vo = int(input("Введите кол-во приставок: "))
discount = float(input("Введите процент скидки: "))
vibor = input("Что считаем? (1 - общая сумма, \n 2- стоимость одной): ")
discount_rate = discount / 100

if choise == "1":
    sum = price * kol_vo
    sum_discount = ((sum / price)/100) * (100 - discount)
    print(f"Общая сумма приставок = {sum}, с учетом скидок = {sum_discount}")
