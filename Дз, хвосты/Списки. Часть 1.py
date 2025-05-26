# Задание 1.
text = input("Введите строку: ")
processed_text = text.replace(" ", "").lower()
if processed_text == processed_text[::-1]:
    print("Это палиндром!")
else:
    print("Это не палиндром.")
# Задание 2.
text = input("Введите текст: ")
reserved_input = input("Введите зарезервированные слова через пробел: ")
reserved_words = reserved_input.lower().split()
words = text.split()
for i in range(len(words)):
    if words[i].lower() in reserved_words:
        words[i] = words[i].upper()
result_text = " ".join(words)
print("Изменённый текст:")
print(result_text)
# Задание 3.
text = input("Введите текст: ")
import re
sentences = re.split(r'[.!?]+', text)
sentences = [s.strip() for s in sentences if s.strip()]
count = len(sentences)
print("Количество предложений в тексте:", count)