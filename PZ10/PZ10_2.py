# Из предложенного текстового файла (text18-4.txt) вывести на экран его содержимое,
#количество символов, принадлежащих к группе букв. Сформировать новый файл, в
#который поместить текст в стихотворной форме предварительно заменив символы верхнего
#регистра на нижний.

import string

try:
    uppercase_count = 0

    with open('text18-16.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()

    print("Содержимое файла:\n")

    for line in lines:
        print(line, end='')

        for char in line:
            if char.isupper():
                uppercase_count += 1

    print("\nКоличество букв в верхнем регистре:", uppercase_count)

    new_lines = []
    for line in lines:
        new_line = ''
        for char in line:
            if char in string.punctuation:
                new_line += '!'
            else:
                new_line += char
        new_lines.append(new_line)

    with open('text18-16_result.txt', 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

    print("Новый файл text18-16_result.txt создан")

except FileNotFoundError:
    print("Файл text18-16.txt не найден!")
except Exception as e:
    print("Ошибка:", e)
