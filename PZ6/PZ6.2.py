# Дан целочисленный список размера N, содержащий ровно два одинаковых элемента.
# Найти номера одинаковых элементов и вывести эти номера в порядке возрастания.

import random

N = input('Введи размер списка N: ')
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input('Введи размер списка N: ')
while N < 2:
    print('Список должен содержать как минимум 2 элемента!')
    N = input('Введи размер списка N (>=2): ')
    while type(N) != int:
        try:
            N = int(N)
        except ValueError:
            print("Неправильно ввели!")
            N = input('Введи размер списка N: ')
A = []
t = 0
while t < N:
    A.append(random.randint(1, 10))
    t += 1

dup_value = random.randint(1, 10)
pos1 = random.randint(0, N-1)
pos2 = random.randint(0, N-1)
while pos2 == pos1: 
    pos2 = random.randint(0, N-1)

A[pos1] = dup_value
A[pos2] = dup_value

print('Сгенерированный список:', A)

found = False
for i in range(len(A)):
    for j in range(i + 1, len(A)):
        if A[i] == A[j]:
            print(f'Найдены одинаковые элементы: A[{i+1}] = A[{j+1}] = {A[i]}')
            if i < j:
                print(f'Номера одинаковых элементов: {i+1} и {j+1}')
            else:
                print(f'Номера одинаковых элементов: {j+1} и {i+1}')
            found = True
            break
    if found:
        break
