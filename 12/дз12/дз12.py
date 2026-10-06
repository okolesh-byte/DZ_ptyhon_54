# Задание 1
dict1 = {1: 10, 2: 20}
dict2 = {3: 30, 4: 40}
dict3 = {5: 50, 6: 60}

result = {**dict1, **dict2, **dict3}
print(result)

print("-" * 30)

# Задание 2
employees = {
    'emp1': {'name': 'Jhon', 'salary': 7500},
    'emp2': {'name': 'Emma', 'salary': 8000},
    'emp3': {'name': 'Brad', 'salary': 6500}
}

print(employees['emp3'])
print(employees['emp3']['salary'])

employees['emp3']['salary'] = 8500

for emp in employees:
    print(emp)
    print("name :", employees[emp]['name'])
    print("salary :", employees[emp]['salary'])

print("-" * 30)

# Задание 3
students = {}
n = int(input("Количество студентов: "))

for i in range(1, n + 1):
    name = input(f"{i}-й студент: ")
    score = int(input("Балл: "))
    students[name] = score

avg = sum(students.values()) / len(students)
print(f"\nСредний бал: {avg:.0f}. Студенты с балом выше среднего:")

for name, score in students.items():
    if score > avg:
        print(name)