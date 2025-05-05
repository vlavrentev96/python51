# Напишите функцию, вычисляющую произведение элементов списка целых.
# Список передается в качестве параметра. Полученный результат возвращается из функции.
def f1(lst):
    result = 1
    for num in lst:
        result *= num
    return result
# Напишите функцию для нахождения минимума в
# списке целых. Список передаётся в качестве параметра.
# Полученный результат возвращается из функции.
def find_min_value(lst):
    if not lst:
        return None
    min_val = lst[0]
    for num in lst:
        if num < min_val:
            min_val = num
    return min_val
