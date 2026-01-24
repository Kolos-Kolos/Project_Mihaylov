#Даны три целых числа: A, B, C. Проверить истинность высказывания: «Ровно два из чисел A, B, C являются положительными».

while True:
    try:
        a = int(input('Введите первое целое число: '))
        b = int(input('Введите второе целое число: '))
        c = int(input('Введите третье целое число: '))
        break
    except ValueError:
        print("Число должно быть целым")
count_positive = 0
if a > 0:
    count_positive += 1
if b > 0:
    count_positive += 1
if c > 0:
    count_positive += 1

if count_positive == 2:
    print("Истина: ровно два из чисел являются положительными")
else:
    print("Ложь: количество положительных чисел не равно двум")
