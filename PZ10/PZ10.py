#Средствами языка Python сформировать текстовый файл (.txt), содержащий
#последовательность из целых положительных и отрицательных чисел. Сформировать
#новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
#обработку элементов:
#Исходные данные:
#Количество элементов:
#Положительные числа:
#Количество положительных чисел:
#Отрицательные числа:
#Количество отрицательных чисел:

try:
    numbers = [-10, 5, 7, -3, 12, -8, 0, 4]

    with open('data_16_1.txt', 'w') as f:
        for num in numbers:
            f.write(str(num) + ' ')

    print("Исходные данные записаны в файл data_16_1.txt")
  
    with open('data_16_1.txt', 'r') as f:
        data = f.read().split()

    data = [int(x) for x in data]

    positive = [x for x in data if x > 0]
    negative = [x for x in data if x < 0]

    with open('data_16_2.txt', 'w') as f:
        f.write("Исходные данные:\n")
        f.write(' '.join(map(str, data)) + '\n')

        f.write(f"Количество элементов: {len(data)}\n")

        f.write("Положительные числа:\n")
        f.write(' '.join(map(str, positive)) + '\n')
        f.write(f"Количество положительных чисел: {len(positive)}\n")

        f.write("Отрицательные числа:\n")
        f.write(' '.join(map(str, negative)) + '\n')
        f.write(f"Количество отрицательных чисел: {len(negative)}\n")
      
    print("Результат записан в файл data_16_2.txt")
  
except Exception as e:
    print("Ошибка:", e)
