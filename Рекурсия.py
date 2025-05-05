# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * factorial(n-1)
#
#
# print(factorial(6))
# # Рекурсивная функция для нахождения
# # степени числа
# def kvad(a,n):
#     if n == 0:
#         return 1
#     else:
#         return a*kvad(a,n-1)
# a = int(input())
# n = int(input())
# print(kvad(a,n))
# # Функция, вычисляет сумму элементов
# # между a,b.
# def sum_element(a,b):
#     if a==b:
#         return a
#     return a + sum_element(a+1,b)
# Функция, которая выводит N звезд в ряд
# N - задает пользователь.
# def f4(N):
#     if N==0:
#         return "*"
#     return "*" + f4(N-1)
# Функция которая принимает список из 100 случайных элементов,
# находит позицию, с которой начинается последовательность
# из 10 чисел, сумма которых минимальна.
import random
def f5(random_list,tek_pos=0, min_sum=1000, pos_sum=-1):
    #Проверка на конец списка
    if tek_pos > len(random_list) - 10:
        return pos_sum
    tek_sum = sum(random_list[tek_pos:tek_pos+10])
    # если текущая сумма меньше мин. суммы, обновляем ее и запоминаем позицию.
    if tek_sum < min_sum:
        min_sum = tek_sum
        pos_sum = tek_pos
    return f5(random_list,tek_pos+1, min_sum, pos_sum)
#MAIN
random_list = [random.randint(1,100)
               for i in range(100)]
print(f"Начальный список:{random_list}")
a = f5(random_list)
print("Позиция мин. суммы:", a)
print(f"Сумма: {random_list[a : a + 10]}")