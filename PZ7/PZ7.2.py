# Дана строка-предложение на русском языке. Преобразовать строку так, чтобы
# каждое слово начиналось с заглавной буквы.

s = input('Введи строку-предложение на русском языке: ')

words = []
current_word = ''
for char in s:
    if char == ' ':
        if current_word != '':
            words.append(current_word)
            current_word = ''
        words.append(' ')  
    else:
        current_word += char

if current_word != '':
    words.append(current_word)

result_words = []
for word in words:
    if word != ' ' and len(word) > 0:
        first_char = word[0]
        if 'а' <= first_char <= 'я' or 'А' <= first_char <= 'Я' or first_char in 'ёЁ':
            if 'а' <= first_char <= 'я' or first_char == 'ё':
                new_first_char = chr(ord(first_char) - 32)
            elif first_char == 'ё':
                new_first_char = 'Ё'
            else:
                new_first_char = first_char
            
            result_words.append(new_first_char + word[1:])
        else:
            result_words.append(word)
    else:
        result_words.append(word)

result = ''.join(result_words)

print('Результат преобразования:')
print(result)
