# Дан список A размера N. Вывести его элементы в следующем порядке: 
# A1, A2, AN, AN-1, A3, A4, AN-2, AN-3, …

N = input('Введи размер списка N: ')
while type(N) != int:
    try:
        N = int(N)
    except ValueError:
        print("Неправильно ввели!")
        N = input('Введи размер списка N: ')
A = []
t = 0
while t < N:
    element = input(f'Введи элемент A[{t+1}]: ')
    while type(element) != int:
        try:
            element = int(element)
        except ValueError:
            print("Неправильно ввели!")
            element = input(f'Введи элемент A[{t+1}]: ')
    A.append(element)
    t += 1
  
print('Исходный список:', A)

result = []
left = 0
right = N - 1

print('Элементы в заданном порядке:')
while left <= right:
    if left < N:
        result.append(A[left])
        if left + 1 < N:
            result.append(A[left + 1])
    if right >= 0 and right > left:
        result.append(A[right])
        if right - 1 >= 0 and right - 1 > left:
            result.append(A[right - 1])
    
    left += 2
    right -= 2

for i, elem in enumerate(result):
    print(f'A{i+1} = {elem}')
