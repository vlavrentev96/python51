# Задание 1.
def product_of_list(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result
# Задание 2.
def find_minimum(numbers):
    if not numbers:
        return None
    minimum = numbers[0]
    for num in numbers:
        if num < minimum:
            minimum = num
    return minimum
# Задание 3.
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def count_primes(numbers):
    count = 0
    for num in numbers:
        if is_prime(num):
            count += 1
    return count
# Задание 4.
def remove_number(numbers, target):
    original_length = len(numbers)
    numbers[:] = [num for num in numbers if num != target]
    removed_count = original_length - len(numbers)
    return removed_count
# Задание 5.
def merge_lists(list1, list2):
    return list1 + list2
# Задание 6.
def power_list(numbers, power):
    result = []
    for num in numbers:
        result.append(num ** power)
    return result