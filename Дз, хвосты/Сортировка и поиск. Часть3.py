# Задание 1.
import random
lst = [random.randint(0, 99) for _ in range(10)]
print("Список:", lst)
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
target = int(input("Введите число для поиска (линейный поиск): "))
pos = linear_search(lst, target)
if pos != -1:
    print(f"Число {target} найдено на позиции {pos}")
else:
    print(f"Число {target} не найдено")
# Задание 2.
import random
lst = [random.randint(0, 99) for _ in range(10)]
lst.sort()
print("Отсортированный список:", lst)
def binary_search(lst, target):
    left = 0
    right = len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
target = int(input("Введите число для поиска (бинарный поиск): "))
pos = binary_search(lst, target)
if pos != -1:
    print(f"Число {target} найдено на позиции {pos}")
else:
    print(f"Число {target} не найдено")