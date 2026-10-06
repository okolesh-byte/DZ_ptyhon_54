# Задание 1
mul = lambda a, b, c: a * b * c
print(mul(2, 5, 5))

print("-" * 30)

# Задание 2
students = [
    {'name': 'Jennifer', 'final': 95},
    {'name': 'David', 'final': 92},
    {'name': 'Nikolas', 'final': 98}
]

by_name = sorted(students, key=lambda x: x['name'])
print(by_name)

by_score = sorted(students, key=lambda x: x['final'], reverse=True)
print(by_score)

print("-" * 30)

# Задание 3
max_student = max(students, key=lambda x: x['final'])
min_student = min(students, key=lambda x: x['final'])

print(max_student)
print(min_student)

print("-" * 30)

# Задание 4
nums = [3, 5, 7, 3, 9, 5, 7, 2]

squares = list(map(lambda x: x ** 2, nums))
print(squares)

cubes = list(map(lambda x: x ** 3, nums))
print(cubes)