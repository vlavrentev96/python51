# # print("Hello world!!!")
# #Функция для печати текста
# # и его вывода в консоль
# # name = input("Введите ваше имя: ")
# # age = input("Введите ваш возраст: ")
# # print("Привет," , name , " Тебе ",age ," лет")
#
# #Калькулятор
# value1 = int(input("Введите первую переменную:"))
# value2 = int(input("Введите вторую переменную:"))
# print(f"{value1} + {value2} = {value1 + value2}")#сумма элементов
# #string - тип данных для текста
# #int - тип данных для целочисленных чисел
# #float - тип данных с плавающей точкой
# #bool - тип данных логический, True, False
# print(f"{value1} - {value2} = {value1 - value2}")
# print(f"{value1} * {value2} = {value1 * value2}")
# print(f"{value1} / {value2} = {value1 / value2}")
# print(f"{value1} // {value2} = {value1 // value2}")
# print(f"{value1} % {value2} = {value1 % value2}")
# print(f"{value1} ** {value2} = {value1 ** value2}")
# print("*" * 11)
# #Проверка и сравнение данных
# print(value1 > value2)
# print(value1 < value2)
# print(value1 ==value2)
# print(value1 == 'Hello world!!!') #Проверка на равенства
# print("hello" > "hello world!!!") #Проверка на неравенства
# print("hello" > "hello world")

#Пользователь вводит с клавиатуры три числа.
# Необходимо найти сумму чисел, произведение чисел.
#Результат вычислений вывести на экран.
# value_number = int(input("Введите число 1: "))
# value_number2 = int(input("Введите число 2: "))
# value_number3 = int(input("Введите число 3: "))
# сумма = value_number + value_number2 + value_number3
# произведение = value_number + value_number2 + value_number3
# print(f" Сумма: {сумма}")
# print(f"Произведение")
#Задание 2
#Первое число - Зарплата за месяц,
#Второе число - сумма месячного платежа по кредиту,
#Третье число - задолженность за коммунальные услуги
#Необходимо вывести на экран сумму
#которая останется у пользователя после всех выплат.
# value_number = int(input("Введите зарплату: "))
# value_number2 = int(input("Введите платеж по кредиту: "))
# value_number3 = int(input("Введите коммуналка: "))
# result = value_number - value_number2 - value_number3
# print(f" ЗП: {value_number}, "
#       f"\n Платеж: {value_number2}, "
#       f"\n Коммуналка: {value_number3}, "
#       f"\n Остаток: {result}")
# #Экранирование символов
# #Вызов спец. символа \ для создания команды вставки символов.
# # \\ - добавляет обратный слэш
# # \" - добавляет двойные кавычки
# # \' - добавляет одиночные кавычки
# # \n - переход на новую строку
# # \t - вставка 3х пробелов
# # \b - удаление пред. символа
# string = ("Фраза для работы со строкой")
# print(value_number, string, value_number2, value_number3, sep="*\n")
# #sep - это строка, для вставки, между значениями элементов вывода для print
# #end - вставка символа в конце строки, вместо \n
# print(value_number, string, value_number2, value_number3, end="***")
#Выведите на экран надпись To be or not to be на разных строках. Пример вывода:
#To be
#            or not
#                         to be
# print("To be \n \t\t or not \n \t\t\t\t to be")
# print(f" To be", "or not","to be", start='\t', end ='', sep='\n')
# # print(f" To be","\n","or not","\n","to be")
#Пользователь вводит с клавиатуры три цифры.
#Необходимо создать число, содержащее эти цифры.
#Например, если с клавиатуры введено 1, 5, 7,
# тогда нужно сформировать число 157.
#Пользователь вводит с клавиатуры число, состоящее из четырех цифр.
# Требуется найти произведение цифр.
#Например, если с клавиатуры введено 1324,
# тогда результат произведение 1*3*2*4 = 24
# value1 = int(input("Введите число из 4 чисел: "))
# print( (value1//1000)*((value1//100)%10)*((value1//10)%10)*(value1 % 10))
# #либо
# value1 = input("Введите число из 4 чисел: ")
# print(int(value1[0])*int(value1[1])*int(value1[2])*int(value1[3]))
#Строки и их свойства
string = "My name is Ara"
print(type(string)) #Проверка типа данных
print(string + string) #Сложение строк
print(string * 4) #Умножение строк
print(string.capitalize()) #Приводит первую букву в верхний регистр
print(string.lower()) #Приводит все символы в нижний регистр
print(string.swapcase()) #Меняет текущий регистр буквы, на противоположный
print(string.title()) #Преобразует первые буквы всех слов в верхний регистр
print(string.upper()) #Преобразует все буквы в верхний регистр
print(string.count("my",0, 5)) #Подсчитывает количество элементов в строке
print(string.endswith("!")) #Проверяет заканчивается ли строка подстрокой
print(string.startswith("!")) #Проверяет начинается ли строка подстрокой
print(string.find("is")) #Ищет подстроку в строке слева направо
print(string.rfind("Ara")) # Ищет подстроку в строку справа налево
#Возвращает первое вхождение (индекс) подстроки
print(string.index("Ara")) #Ищет подстроку в строке слева направо
print(string.rindex("Ara")) #Ищет подстроку в строку справа налево
#Возвращает первое вхождение (индекс) подстроки, если элемента нет, будет ошибка
#Классификация(Определение) строк
print(string.isalnum()) #Определяет, состоит ли строка из букв и чисел
print(string.isalpha()) #Определяет, состоит ли строка из букв
print(string.isdigit()) #Состоит ли строка из чисел
print(string.islower())
print(string.isupper())
print(string.istitle())
print(string.isspace()) #Проверяет наличие в строке пробельных символов
#Форматирование и выравнивание строк
print("main".center(10, "*")) #Выравнивание строки по центру
print("main\t\t\tmain".expandtabs(tabsize=1)) #Заменяет табуляцию на пробелы
print("main main".ljust(10, "@")) #Выравнивание по левому краю
print("main main".rjust(10, "?")) #Выравнивание по правому краю
print("main main".lstrip()) #Все пробельные символы с левого края будут удалены
print("main main".rstrip()) #Все пробельные символы с правого края будут удалены
print("main main".replace("main", "own")) #Заменяет подстроку