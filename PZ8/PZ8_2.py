#Дан словарь на 6 персон, найти и вывести их средний возраст. 
people = {
    "Андрей": 32,
    "Виктор": 29,
    "Максим": 18,
    "Игорь": 25,
    "Дмитрий": 30,
    "Алексей": 24
}

print("Исходный словарь:", people)

total_age = 0

for age in people.values():
    total_age += age

average_age = total_age / len(people)

print("Средний возраст:", round(average_age, 2))
