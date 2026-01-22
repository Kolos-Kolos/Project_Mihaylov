#Описать функцию Power1(A, B) вещественного типа, находящую величину AB по формуле AB = exp(B*ln(A)) (параметры A и B — вещественные). В случае нулевого или отрицательного параметра A функция возвращает 0. С помощью этой функции найти степени AP, BP, CP, если даны числа P, A, B, C.

import math

def Power1(A, B):
    """
    Функция для вычисления A^B по формуле exp(B*ln(A))
    Возвращает 0, если A <= 0
    """
    if A <= 0:
        return 0
    else:
        return math.exp(B * math.log(A))

while True:
    try:
        P = float(input("Введите степень P (вещественное число): "))
        break
    except ValueError:
        print("Ошибка! Введите число.")

while True:
    try:
        A = float(input("Введите число A (вещественное число): "))
        break
    except ValueError:
        print("Ошибка! Введите число.")

while True:
    try:
        B = float(input("Введите число B (вещественное число): "))
        break
    except ValueError:
        print("Ошибка! Введите число.")

while True:
    try:
        C = float(input("Введите число C (вещественное число): "))
        break
    except ValueError:
        print("Ошибка! Введите число.")
      
result_A = Power1(A, P)
result_B = Power1(B, P)
result_C = Power1(C, P)

print(f"\nРезультаты возведения в степень {P}:")
print(f"A^{P} = {result_A}")
print(f"B^{P} = {result_B}")
print(f"C^{P} = {result_C}")
