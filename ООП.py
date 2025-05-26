# Класс - набор обьектов, методов, атрибутов, - выступающий в роли контейнера
# (шаблона) для будующего обьекта,
# с которым работает уже пользователь
# Обьект - это воплощение требований, характеристик и качеств,
# которое приписываются конкретному классу.
class Car:
    #Конструктор класса
    def __init__(self, fuel,maxspeed):
        self.fuel = fuel
        self.maxspeed = maxspeed
    # Функция для заправки топлива
    def refuel(self, amount):
        self.fuel += amount
    # Функция для движения
    def drive(self):
        if self.fuel > 0:
            print("Машина едет.")
            self.fuel -= 1
        else:
            print("Нет топлива!")


polo = Car(50,50)
mini = Car(10,90)
beetle = Car(0,110)
print("Сейчас будет двигаться polo")
for i in range(10):
    polo.drive()
print("Сейчас будет двигаться mini")
for i in range(10):
    mini.drive()
print("Сейчас будет двигаться beetle")
for i in range(10):
    beetle.drive()


# Написать программу "Успеваемость студента." Пользователь вводит
# 10 оценок от 1 до 5. Реализовать меню для работы:
# 1) Вывод
# 2) Пересдача
# 3) Выходит ли стипендия?
# 4) Вывод отсортированных оценок по возрастанию и убыванию.
class Student:
    def __init__(self,eval_list):
        self.eval_list = eval_list
    def menu(self):
        while True:
            print("Меню: \n 1. Вывод \n "
              "2) Пересдача \n "
              "3) Стипендия \n "
              "4) Вывод отсортированных оценок по возрастанию и убыванию"
              "0) Выход")
            print("*"*11)
            value = int(input("Ваш выбор: "))
            if value == 1:
                self.Print() # Вызов функции вывода на экран
            elif value == 2:
                self.reEval() # Вызов функции пересдачи
            elif value == 3:
                self.ship() # Вызов функции вызов стипендии
            elif value == 4:
                self.sort_list() # Вызов функции сортировки
            elif value == 0:
                break
    # Функция замены оценок
    def reEval(self):
        self.Print()
        last_eval = int(input("Введите оценку на ЗАМЕНУ: "))
        new_eval = int(input("Введите НОВУЮ оценку: "))
        for i in range(len(self.eval_list)):
            if self.eval_list[i] == last_eval:
                self.eval_list[i] == new_eval
                break
        print("Оценка изменена!")
    # Функция вывода на экран
    def Print(self):
        print("Список оценок: ",end=' ')
        for i in self.eval_list:
            print(i, end=' ')
        print()
    def ship(self):
        if sum(self.eval_list)/len(self.eval_list) >= 4:
            print("Стипендия есть!")
        else:
            print("Низкий балл, не видать денежек ")
    def sort_list(self):
        if int(input("1 - Убывание, 2 - Возрастание \n Ваш выбор: ")) == 1:
            self.eval_list = sorted(self.eval_list, reverse=True)
        else:
            self.eval_list = sorted(self.eval_list)
        print("Сортировка выполнена! Вот ваш список оценок: ")
        self.Print()

student = Student([1,5,3,4,2,3,5,5,5,5])
student.menu()