# Задание 1.
# Необходимо отсортировать первые две трети списка в порядке возрастания,
# если среднее арифметическое всех элементов больше нуля;
# иначе - лишь первую треть.
# Остальную часть списка не сортировать, а расположить
# в обратном порядке.
import random
def my_sort_one(mass):
    for j in range(value):
        for i in range(value):
            if mass[i] > mass[i+1]:
                mass[i],mass[i+1]= mass[i+1],mass[i]

def my_sort_two(mass, value):
    for j in range(value):
        for i in range(value):
            if mass[i] > mass[i+1]:
                mass[i],mass[i+1]= mass[i+1],mass[i]

mass = [random.randint(-10,10) for i in range(10)]
sr_z = sum(mass)/len(mass)
if sr_z < 0:
    value = (len(mass) // 3)*2
    my_sort_one(mass,value)
else:
    value = len(mass)//3
    my_sort_two(mass,value)
# Вводим 10 оценок от пользователя
grades = []

print("Введите 10 оценок студента (от 1 до 12):")
while len(grades) < 10:
    try:
        grade = int(input(f"Оценка {len(grades)+1}: "))
        if 1 <= grade <= 12:
            grades.append(grade)
        else:
            print("Оценка должна быть от 1 до 12.")
    except ValueError:
        print("Введите число!")
# Задание 2.
# Написать программу «успеваемость». Пользователь
# вводит 10 оценок студента. Оценки от 1 до 12. Реализовать
# меню для пользователя:
# ■ Вывод оценок (вывод содержимого списка);
# ■ Пересдача экзамена (пользователь вводит номер элемента списка и новую оценку);
# ■ Выходит ли стипендия (стипендия выходит, если
# средний бал не ниже 10.7);
# ■ Вывод отсортированного списка оценок: по возрастанию или убыванию.
grades = []
print("Введите 10 оценок студента (от 1 до 12):")
while len(grades) < 10:
    try:
        grade = int(input(f"Оценка {len(grades)+1}: "))
        if 1 <= grade <= 12:
            grades.append(grade)
        else:
            print("Оценка должна быть от 1 до 12.")
    except ValueError:
        print("Введите число!")
while True:
    print("\nМеню:")
    print("1. Вывод оценок")
    print("2. Пересдача экзамена")
    print("3. Проверка стипендии")
    print("4. Сортировка оценок")
    print("5. Выход")
    choice = input("Выберите пункт меню (1-5): ")
    if choice == '1':
        print("\n Оценки студента:")
        for i, g in enumerate(grades, 1):
            print(f"{i}: {g}")
    elif choice == '2':
        try:
            index = int(input("Введите номер оценки (1–10), которую хотите изменить: ")) - 1
            if 0 <= index < 10:
                new_grade = int(input("Введите новую оценку (1–12): "))
                if 1 <= new_grade <= 12:
                    grades[index] = new_grade
                    print("Оценка обновлена.")
                else:
                    print("Оценка должна быть от 1 до 12.")
            else:
                print("Неверный номер оценки.")
        except ValueError:
            print("Введите корректные числа.")

    elif choice == '3':
        avg = sum(grades) / len(grades)
        print(f"Средний балл: {avg:.2f}")
        if avg >= 10.7:
            print("Стипендия ВЫХОДИТ!")
        else:
            print("Стипендия НЕ выходит.")
    elif choice == '4':
        order = input("Введите 'в' для возрастания или 'у' для убывания: ").lower()
        if order == 'в':
            grades.sort()
            print("Список отсортирован по возрастанию.")
        elif order == 'у':
            grades.sort(reverse=True)
            print("Список отсортирован по убыванию.")
        else:
            print("Неверный ввод. Введите 'в' или 'у'.")
    elif choice == '5':
        print("Выход из программы.")
        break
    else:
        print("Неверный выбор. Повторите.")
# Задание 3.
# Написать программу, реализующую сортировку списка
# методом усовершенствованной сортировки пузырьковым
# методом. Усовершенствование состоит в том, чтобы анализировать количество перестановок на каждом шагу, если
# это количество равно нулю, то продолжать сортировку
# нет смысла — список отсортирован.
def bubble_sort_optimized(lst):
    n = len(lst)
    for i in range(n):
        swapped = False
        for j in range(0, n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                swapped = True
        if not swapped:
            break

    return lst