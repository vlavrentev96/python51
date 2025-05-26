# Задание 1.
size = int(input("Введите размер стороны квадрата: "))
for i in range(size):
    print("*" * size)
# Задание 2.
height = int(input("Введите высоту прямоугольника: "))
width = int(input("Введите ширину прямоугольника: "))
for i in range(height):
    print("*" * width)
# Задание 3.
size = int(input("Введите размер стороны квадрата: "))
for i in range(size):
    if i == 0 or i == size - 1:
        print("*" * size)
    else:
        print("*" + " " * (size - 2) + "*")
# Задание 4.
height = int(input("Введите высоту (ширину) прямоугольника: "))
width = int(input("Введите длину прямоугольника: "))
for i in range(height):
    if i == 0 or i == height - 1:
        print("*" * width)
    else:
        print("*" + " " * (width - 2) + "*")