#Задание 4
import random
import datetime
print("Добро пожаловать в игру <Угадай число!>")
print("Правила очень просты, ты пытаешься угадать число от 1 до 500, а я даю подсказки")
print("*"*11)
user_choice_count = 0
user_choice_time = datetime.datetime.now()#текущее время
print(f"Начало игры в {user_choice_time}")
random_value = random.randint(1, 500)
#randint функция вывода случайного числа в интервале
while True:
    user_choice_count += 1
    value_user = int(input("Введите предпологаемое число: "))
    if value_user ==random_value:
        print("Вы угадали число! /Поздравляю!")
        break
    elif value_user < random_value:
        print("Ваше число меньше загаданного!")
    elif value_user > random_value:
        print("Ваше число боьше загаданного!")
    print("*"*11)
delta_time = datetime.datetime.now() - user_choice_time

print(f"Статистика: \n Попыток ->{user_choice_count} \n старт->{user_choice_time} \n Время->{delta_time}")
#Задание 1
# number = int(input("Введите число: "))
# for i in range(1, 11):
#     print(f"{number}* {i} = {number * i}")
# Задание 2
# rub = int(input("Введите количество рублей: "))
# var = int(input("Введите 1 для пересчёта Рубля к доллару, \n2 - Для пересчёта рубля к евро"))
# if var == 1:
#     print(rub / 82)
# elif var ==2:
#     print(rub / 92)
#Задание 3
# niz = int(input("Введите нижний диапазон"))
# ver = int(input("Введите верхний диапазон"))
# ch = int(input(f"Введите число для проверки которое должно находится в диапазоне от {niz} до {ver}"))
# #if niz <= ch <= ver:
# for i in range(niz, ver + 1):
#     if  i == ch:
#         print("!"+str(i)+"!", end=' ')
#     else:
#         print(i,end=' ')