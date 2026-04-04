# Составить генератор (yield), который переведет символы строки из нижнего регистра в верхний.

def to_upper_generator(text):
    for char in text:
        yield char.upper()


try:
    s = "привет, мир!"

    print("Исходная строка:", s)

    gen = to_upper_generator(s)
    result = ''.join(gen)

    print("Результат:", result)

except Exception as e:
    print("Ошибка:", e)
