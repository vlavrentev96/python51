# Задание 1.
with open("input.txt", "r", encoding="utf-8") as infile:
    text = infile.read()
import re
words = re.findall(r'\b\w{7,}\b', text)
with open("output.txt", "w", encoding="utf-8") as outfile:
    # Записываем найденные слова через пробел
    outfile.write(" ".join(words))
# Задание 2.
with open("input.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()
with open("output.txt", "w", encoding="utf-8") as outfile:
    outfile.writelines(lines)
# Задание 3.
with open("input.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()
lines.reverse()
with open("output.txt", "w", encoding="utf-8") as outfile:
    outfile.writelines(lines)
# Задание 4.
with open("input.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()
last_no_comma_index = -1
for i, line in enumerate(lines):
    if "," not in line:
        last_no_comma_index = i
if last_no_comma_index != -1:
    lines.insert(last_no_comma_index + 1, "************\n")
else:
    lines.append("************\n")
with open("output.txt", "w", encoding="utf-8") as outfile:
    outfile.writelines(lines)
# Задание 5.
char = input("Введите символ, с которого должны начинаться слова: ").lower()
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()
words = text.split()
count = 0
for word in words:
    if word.lower().startswith(char):
        count += 1
print(f"Количество слов, начинающихся с '{char}':", count)
# Задание 6.
with open("input.txt", "r", encoding="utf-8") as infile:
    lines = infile.readlines()
new_lines = []
for line in lines:
    new_line = ("")
    for char in line:
        if char == "+":
            new_line += "&"
        elif char == "&":
            new_line += "+"
        else:
            new_line += char
    new_lines.append(new_line)
with open("output.txt", "w", encoding="utf-8") as outfile:
    outfile.writelines(new_lines)
# Задание 7.
lines = ["Привет!", "Как дела?", "Это пример!", "Все хорошо."]
with open("output.txt", "w", encoding="utf-8") as file:
    for line in lines:
        file.write(line + "\n")
# Задание 8.
with open("input.txt", "r", encoding="utf-8") as file:
    text = file.read()
symbol_count = len(text)
print("Количество символов в тексте -", symbol_count)
# Задание 9.
with open("input.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
line_count = len(lines)
print("Количество строк в файле:", line_count)