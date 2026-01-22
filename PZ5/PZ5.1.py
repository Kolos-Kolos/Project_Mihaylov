#Найти сумму чисел ряда 1,2,3,4,... от числа n до числа m. Суммирование оформить функцией с параметрами. Значения n и m программа должна запрашивать.

def sum_range(n, m):
    """
    Функция для вычисления суммы чисел от n до m включительно
    """
    total = 0
    for i in range(n, m + 1):
        total += i
    return total
while True:
    try:
        n = int(input("Введите начальное число n: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число.")
while True:
    try:
        m = int(input("Введите конечное число m: "))
        break
    except ValueError:
        print("Ошибка! Введите целое число.")
if m >= n:
    result = sum_range(n, m)
    print(f"Сумма чисел от {n} до {m} равна: {result}")
else:
    print("Ошибка: m должно быть больше или равно n!")
