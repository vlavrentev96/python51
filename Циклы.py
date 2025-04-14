# # #for (УСЛОВИЕ):
# #     #ОПЕРАЦИЯ
# # for i in range(10,100):
# #     print("*" * i)
# #     i = 2
# sum = 0
# value = int(input("Введите число для ввода данных:"))
# for i in range(value):
#     sum = sum + int(input("Введите число: "))
#     print(i)
# print(i)
# print(f'Сумма чисел пользователя: {sum}')
for i in range(10):
    print('%' * i)
    for j in range(10):
        print("*", end=' ')
    print('\n')