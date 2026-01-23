# Дана строка. Преобразовать в ней все прописные латинские буквы в строчные.

s = input('Введи строку: ')

result = ''
for char in s:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    else:
        result += char

print('Результат преобразования:')
print(result)
