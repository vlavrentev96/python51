# Задание 1.
def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1
list1 = [5, 8, 2]
list2 = [9, 1, 7]
list3 = [3, 6, 0]
list4 = [4, 10, 11]
merged_list = list1 + list2 + list3 + list4
choice = input("Сортировать по возрастанию (1) или по убыванию (2)? Введите 1 или 2: ")
if choice == "1":
    merged_list.sort()
elif choice == "2":
    merged_list.sort(reverse=True)
else:
    print("Неверный выбор. Список не будет отсортирован.")
print("Итоговый список:", merged_list)
search_value = int(input("Введите число для поиска: "))
position = linear_search(merged_list, search_value)
if position != -1:
    print(f"Число {search_value} найдено на позиции {position}")
else:
    print(f"Число {search_value} не найдено в списке.")
# Задание 2.
def find_unique_elements(list1, list2, list3, list4):
    all_lists = list1 + list2 + list3 + list4
    unique = []
    for num in all_lists:
        if all_lists.count(num) == 1:
            unique.append(num)
    return unique
def binary_search(sorted_list, target):
    left = 0
    right = len(sorted_list) - 1
    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == target:
            return mid
        elif sorted_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
list1 = [1, 2, 3]
list2 = [3, 4, 5]
list3 = [5, 6, 7]
list4 = [7, 8, 9]
unique_elements = find_unique_elements(list1, list2, list3, list4)
choice = input("Сортировать по возрастанию (1) или по убыванию (2)? ")
if choice == "1":
    unique_elements.sort()
elif choice == "2":
    unique_elements.sort(reverse=True)
else:
    print("Неверный выбор, список не будет отсортирован.")
print("Уникальные элементы:", unique_elements)
try:
    target = int(input("Введите число для поиска: "))
    sorted_for_search = sorted(unique_elements)
    position = binary_search(sorted_for_search, target)
    if position != -1:
        print(f"Число {target} найдено на позиции {position} (в отсортированном списке по возрастанию)")
    else:
        print(f"Число {target} не найдено.")
except ValueError:
    print("Ошибка: введите целое число.")