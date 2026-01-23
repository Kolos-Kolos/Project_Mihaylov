# Дан список A размера N и целое число K (1 < K < 4, K < N).
# Осуществить циклический сдвиг элементов списка вправо на K позиций

import random

N = input('Введи размер списка N: ')
while type(N) != int: 
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input('Введи размер списка N: ')

while N <= 1:
    print('Список должен содержать как минимум 2 элемента!')
    N = input('Введи размер списка N (>=2): ')
    while type(N) != int:
        try:
            N = int(N)
        except ValueError:
            print("Неправильно ввели!")
            N = input('Введи размер списка N: ')

K = input(f'Введи K (1 < K < 4 и K < {N}): ')
while type(K) != int: 
    try:
        K = int(K)
    except ValueError:
        print("Неправильно ввели!")
        K = input(f'Введи K (1 < K < 4 и K < {N}): ')

while not (1 < K < 4 and K < N):
    print(f'K должно удовлетворять: 1 < K < 4 и K < {N}')
    K = input(f'Введи K (1 < K < 4 и K < {N}): ')
    while type(K) != int:
        try:
            K = int(K)
        except ValueError:
            print("Неправильно ввели!")
            K = input(f'Введи K (1 < K < 4 и K < {N}): ')

A = []
t = 0
while t < N:
    A.append(random.randint(1, 100))
    t += 1

print('Исходный список A:', A)

temp = [0, 0, 0, 0]

i = 0
while i < K:
    temp[i] = A[N - K + i]
    i += 1

i = N - 1
while i >= K:
    A[i] = A[i - K]
    i -= 1

i = 0
while i < K:
    A[i] = temp[i]
    i += 1

print(f'Список A после циклического сдвига вправо на {K} позиций:')
print(A)

print(f'\nКак работает сдвиг:')
print(f'Последние {K} элемента(ов) стали первыми:')
for i in range(K):
    print(f'  A[{i+1}] = {A[i]} (было A[{N-K+i+1}] = {temp[i]})')
