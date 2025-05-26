# Задание 1.
with open("file1.txt", "r", encoding="utf-8") as f1, open("file2.txt", "r", encoding="utf=8") as f2:
    lines1 = f1.readlines()
    lines2 = f2.reaflines()
lines1 = [line.strip() for line in lines1]
lines2 = [line.strip() for line in lines2]
if lines1 == lines2:
    print("Файлы совпадают полностью!")
else:
    print("Файлы не совпадают!")
max_len = max(len(lines1), len(lines2))
for i in range(max_len):
    line1 = lines1[i] if i < len(lines1) else ""
    line2 = lines2[i] if i < len(lines2) else ""
    if line1 != line2:
        print(f"\n Строка {i + 1}:")
        print(f"  В file1.txt: {line1}")
        print(f"  В file2.txt: {line2}")
# Задание 2.
glasnie = "аеёиоуыэюяaeiou"
soglasnie = "бвгджзйклмнпрстфхцчшщbcdfghjklmnpqrstvwxyz"
char_count = 0
line_count = 0
glasnie_count = 0
soglasnie_count = 0
digit_count = 0
with open("input.txt", "r", encoding="utf-8") as infile:
    for line in infile:
        line_count += 1
        for char in line:
            char_count += 1
            low_char = char.lower()
        if low_char in glasnie:
            glasnie_count += 1
        elif low_char in soglasnie:
            soglasnie_count += 1
        elif char.isdigit():
            digit_count += 1
with open("stats.txt", "w", encoding="utf-8") as outfile:
    outfile.write(f"Количество символов: {char_count}\n")
    outfile.write(f"Количество строк: {line_count}\n")
    outfile.write(f"Количество гласных букв: {glasnie_count}\n")
    outfile.write(f"Количество согласных букв: {soglasnie_count}\n")
    outfile.write(f"Количество цифр: {digit_count}\n")
# Задание 3.
with open("input.txt", "r", encoding="utf-8") as infile:
    lines = infile.relines()
if lines:
    lines == lines[:-1]
with open("output.txt", "w", encoding="utf-8") as outfile:
    outfile.writelines(lines)
# Задание 4.
with open("input.txt", "r", encoding="utf-8") as infile:
    lines = file.readlines()
if lines:
    max_length = max(len(line.rstrip('\n')) for line in lines)
    print("Длина самой длинной строки:", max_length)
else:
    print("Файл пустой")
# Задание 4.
import string
input_word = input("Введите слово для поиска: ").lower()
count = 0
with open("input.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.lower()
        line = line.translate(str.maketrans('', '', string.punctuation))
        words = line.split()
        count += words.count(input_word)
    print(f"Слово '{input_word}' встречается {count} раз(а) в файле.")
# Задание 5.
word_to_find = input("Введите слово для поиска: ")
word_to_replace = input("Введите слово для замены: ")
with open("input.txt", "r", encoding="utf-8") as file:
    content = file.read()
new_content = content.replace(word_to_find, word_to_replace)
with open("output.txt", "w", encoding="utf-8") as file:
    file.write(new_content)
print("Замена выполнена. Результат сохранён в файле output.txt")