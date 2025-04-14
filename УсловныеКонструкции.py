    # if (условие):
        #действие
    # elif:(условие):
        #действие
    # elif(условие):
        #действие
    # elif(условие):
        #действие
    # else:
        #действие
# value = int(input("Введите число:"))
# if value > 0:
#         print("Число положительное!")
# elif value == 0:
#         print("Число равно нулю!")
# else:
#         print("Число отрицательное!")
#     # value1 == value2
#     # value1 != value2
#     # value > 0
#     # value < 0
#     # value >= 0
#     # value <= 0
# age = int(input("Введите ваш возраст:"))
# if age < 10 and age > 0:
#     print("Вы еще малыш!")
# elif age >= 10 and age < 21:
#     print("Вы подросток!")
# elif age >= 21 and age < 45:
#     print("Вы молодежь!")
# elif age >= 45 and age <100:
#     print("Вы пенсионер!")
# else:
#     print("Некорректное значение возраста!")
# time = int(input("Введите значение текущего времени в часах:")) % 24
# ticket = False
# money = True
# luggage = False
#print(money or ticket and not luggage and time >6)
# car_speed = 50
# if ((car_speed >= 50) or (car_speed <= 120)) and car_speed != 200:
#     print("Машина двигается быстро! Снизьте скорость!")
#Исключения. Обработка событий ошибки
# try:
#     amount = int(input("Введите число предметов:"))
#
# except ValueError:
#     print("Ошибка! Введите только число!!!")
# value = int(input("Введите число 1:"))
# value2 = int(input("Введите число 2:"))
# try:
#     print(f"Деление {value / value2}")
# except ZeroDivisionError:
#     print("Делить на 0 нельзя!")
# finally:
#     print("Действие с делением было выполнено!")
#Практика
#Задание 1.
#Пользователь вводит с клавиатуры число. Нужно проверить его на
#четность/нечетность. Eсли четное - вывести even, обратно - odd
value = int(input("Введите число:"))
if value % 2 == 0:
    print('even')
else:
    print('odd')
#Задание 2. Пользователь вводит число. Нужно проверить его на кратность 7. Вывести надпись: Number is multiple 7,
#иначе: number is not multiple7
value = int(input("Введите число:"))
if value % 7 == 0:
    print('Number is multiple 7')
else:
    print("Number is not multiple 7")
#Задание 3. Пользователь вводит 2 числа. Нужно проверить их
#и найти максимум (наибольшее). Вывести его на экран.
value = int(input("Введите первое число:"))
value2 = int(input("Введите второе число:"))
if value > value2:
    print("value")
elif value < value2:
    print(value2)
else:
    print("value2")
#Задание 4. Пользователь вводит 2 числа. Нужно проверить их
#и найти минимальное (наименьшее). Вывести его на экран.
value = int(input("Введите первое число:"))
value2 = int(input("Введите второе число:"))
if value < value2:
    print("value")
elif value > value2:
    print(value2)
else:
    print("value2")
#Задание 5. Пользователь вводит 2 числа. В зависимости от
#выбора пользователя, необходимо показать сложения чисел,
#разность чисел, произведение, деление, сред. арифметическое.
value = int(input("Введите первое число:"))
value2 = int(input("Введите второе число:"))
value3 = int(input("Выбери действие: 1 - если хотите осуществить сложение. \n 2 - чтобы осуществить разность чисел, \n 3 - произведение чисел, \n 4 - деление, \n Ваш выбор: "))
if value3 == 1:
    print(value + value2)
elif value3 == 2:
    print(value - value2)
elif value3 == 3:
    print(value * value2)
elif value3 == 4:
    print(value / value2)
else:
    print("Вы ввели неверное значение!")