#В последовательности на n целых чисел умножить все элементы на первый элемент

try:
    numbers = [2, 4, 6, 8, 10]

    print("Исходная последовательность:", numbers)

    first = numbers[0]

    result = [x * first for x in numbers]

    print("Результат:", result)
  
except Exception as e:
    print("Ошибка:", e)
