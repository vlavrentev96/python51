# Задание 1.
num = int(input("Введите число, для которого нужна таблица умножения: "))
print(f"\nТаблица умножения для числа {num}:")
for i in range(1, 11):
    result = num * i
    print(f"{num} * {i} = {result}")
# Задание 2.
def show_menu():
    print("\n КОНВЕРТЕР ВАЛЮТ")
    print("1. Рубли → Доллары")
    print("2. Рубли → Евро")
    print("3. Доллары → Рубли")
    print("4. Евро → Рубли")
    print("5. Выход")
def rub_to_usd(rub):
    return rub / 79
def rub_to_eur(rub):
    return rub / 90
def usd_to_rub(usd):
    return usd * 79
def eur_to_rub(eur):
    return eur * 90
while True:
    show_menu()
    choice = input("Выберите пункт меню (1-5): ")
    if choice == "1":
        rub = float(input("Введите сумму в рублях: "))
        print(f"{rub} руб = {rub_to_usd(rub):.2f} $")
    elif choice == "2":
        rub = float(input("Введите сумму в рублях: "))
        print(f"{rub} руб = {rub_to_eur(rub):.2f} €")
    elif choice == "3":
        usd = float(input("Введите сумму в долларах: "))
        print(f"{usd} $ = {usd_to_rub(usd):.2f} руб")
    elif choice == "4":
        eur = float(input("Введите сумму в евро: "))
        print(f"{eur} € = {eur_to_rub(eur):.2f} руб")
    elif choice == "5":
        print("Выход из программы. Спасибо!")
        break
    else:
        print("Неверный выбор. Попробуйте снова.")
# Задание 3.
start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
if start > end:
    start, end = end, start
while True:
    number = int(input(f"Введите число в диапазоне от {start} до {end}: "))
    if start <= number <= end:
        break
    print("Число не входит в диапазон! Попробуйте снова.")
for i in range(start, end + 1):
    if i == number:
        print(f"!{i}!", end=" ")
    else:
        print(i, end=" ")
# Задание 4.
import random
import time
print("Добро пожаловать в игру 'Угадай число'!")
print("Я загадал число от 1 до 500.")
print("Попробуй его угадать. Введи 0, если хочешь выйти.")
secret_number = random.randint(1, 500)
attempts = 0
start_time = time.time()
while True:
    guess = int(input("Введите ваше предположение: "))
    if guess == 0:
        print("Вы вышли из игры. Загаданное число было:", secret_number)
        break
    attempts += 1
    if guess < secret_number:
        print("Моё число больше.")
    elif guess > secret_number:
        print("Моё число меньше.")
    else:
        # Победа
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Поздравляю! Вы угадали число {secret_number} за {attempts} попыток.")
        print(f"Это заняло {elapsed_time:.2f} секунд.")
        break
