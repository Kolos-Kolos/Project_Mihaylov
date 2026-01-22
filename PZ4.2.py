# Даны положительные числа A и B (A > B). На отрезке длины A размещено
# максимально возможное количество отрезков длины B (без наложений).
# Не используя операции умножения и деления, найти количество отрезков B,
# размещенных на отрезке A.
while True:
    try:
        A = float(input("Введите положительное число A: "))
        if A > 0:
            break
        else:
            print("A должно быть положительным!")
    except ValueError:
        print("Ошибка! Введите число.")
while True:
    try:
        B = float(input(f"Введите положительное число B (меньше {A}): "))
        if 0 < B <= A:
            break
        else:
            print(f"B должно быть положительным и не больше {A}!")
    except ValueError:
        print("Ошибка! Введите число.")
count = 0
remaining = A 

while remaining >= B:
    remaining -= B
    count += 1
print(f"На отрезке длины {A} помещается {count} отрезков длины {B}")
print(f"Остаток: {remaining}")
