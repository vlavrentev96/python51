# Задание 1.
def power(base, exponent):
    if exponent == 0:
        return 1
    return base * power(base, exponent - 1)
# Задание 2.
def sum_range(a, b):
    if a > b:
        return 0
    return a + sum_range(a + 1, b)
# Задание 3.
def print_stars(n):
    if n <= 0:
        return
    print('*', end='')
    print_stars(n - 1)
# Задание 4.
# Задача написать приложение крестики-нолики уже была сделана ранее.
# Задание 5.
import random
def find_min_sum_position(lst, index=0, best_index=0, min_sum=None):
    if index + 10 > len(lst):
        return best_index
    current_sum = sum(lst[index:index + 10])
    if min_sum is None or current_sum < min_sum:
        return find_min_sum_position(lst, index + 1, index, current_sum)
    return find_min_sum_position(lst, index + 1, best_index, min_sum)
random.seed(0)
numbers = [random.randint(0, 100) for _ in range(100)]
# Задание 6.
def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
def days_in_month(month, year):
    if month == 2:
        return 29 if is_leap_year(year) else 28
    elif month in [4, 6, 9, 11]:
        return 30
    return 31
def date_to_days(day, month, year):
    days = 0
    for y in range(1, year):
        days += 366 if is_leap_year(y) else 365
    for m in range(1, month):
        days += days_in_month(m, year)
    days += day
    return days
def days_between_dates(d1, m1, y1, d2, m2, y2):
    days1 = date_to_days(d1, m1, y1)
    days2 = date_to_days(d2, m2, y2)
    return abs(days2 - days1)
