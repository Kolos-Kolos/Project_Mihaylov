# Дано вещественное число A и целое число N (>0). Используя один цикл,
# найти значение выражения 1 - A + A^2 - A^3 + ... + (-1)^N * A^N.
# Условный оператор не использовать.

while True:
    try:
        A = float(input("Введите вещественное число A: "))
        break
    except ValueError:
        print("Ошибка! Введите вещественное число.")
while True:
    try:
        N = int(input("Введите целое число N (>0): "))
        if N > 0:
            break
        else:
            print("N должно быть больше 0!")
    except ValueError:
        print("Ошибка! Введите целое число.")
S = 0.0
current_term = 1.0  
sign = 1  
for i in range(N + 1):
    S += sign * current_term
    sign = -sign  
    current_term *= A 
print(f"Значение выражения: {S}")
