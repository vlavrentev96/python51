# Задание 1.
ids = [103, 101, 102]
phones = [5551234, 5555678, 5552345]
while True:
    print("\nМеню:")
    print("1. Отсортировать по идентификационным кодам")
    print("2. Отсортировать по номерам телефона")
    print("3. Вывести список пользователей")
    print("4. Выход")
    choice = input("Выберите пункт меню (1-4): ")
    if choice == '1':
        combined = list(zip(ids, phones))
        combined.sort()
        ids, phones = zip(*combined)
        ids = list(ids)
        phones = list(phones)
        print("Сортировка по ID выполнена.")
    elif choice == '2':
        combined = list(zip(phones, ids))
        combined.sort()
        phones, ids = zip(*combined)
        ids = list(ids)
        phones = list(phones)
        print("Сортировка по телефонам выполнена.")
    elif choice == '3':
        print("\nСписок пользователей:")
        for i in range(len(ids)):
            print(f"ID: {ids[i]}, Телефон: {phones[i]}")
    elif choice == '4':
        # Выход из программы
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Попробуйте снова.")

#Задание 2.
titles = ["Мастер и Маргарита", "Преступление и наказание", "Война и мир"]
years = [1967, 1866, 1869]
while True:
    print("\nМеню:")
    print("1. Отсортировать по названию книг")
    print("2. Отсортировать по годам выпуска")
    print("3. Вывести список книг с названиями и годами выпуска")
    print("4. Выход")
    choice = input("Выберите пункт меню (1-4): ")
    if choice == '1':
        combined = list(zip(titles, years))
        combined.sort(key=lambda x: x[0])
        titles, years = zip(*combined)
        titles = list(titles)
        years = list(years)
        print("Сортировка по названию выполнена.")
    elif choice == '2':
        combined = list(zip(titles, years))
        combined.sort(key=lambda x: x[1])
        titles, years = zip(*combined)
        titles = list(titles)
        years = list(years)
        print("Сортировка по году выпуска выполнена.")
    elif choice == '3':
        print("\nСписок книг:")
        for i in range(len(titles)):
            print(f"{titles[i]} — {years[i]} год")
    elif choice == '4':
        # Выход
        print("Выход из программы.")
        break

    else:
        print("Некорректный ввод. Попробуйте снова.")