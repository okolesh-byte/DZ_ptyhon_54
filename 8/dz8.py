from random import randint

# Задание 1
matrix = []
negative_count = 0

for i in range(4):
    row = []
    for j in range(3):
        num = randint(-20, 10)
        row.append(num)
        if num < 0:
            negative_count += 1
    matrix.append(row)

for row in matrix:
    for num in row:
        print(num, end="\t")
    print()

print("Количество отрицательных элементов:", negative_count)

print("-" * 30)

# Задание 2
matrix = []
product = 1

for i in range(4):
    row = []
    for j in range(3):
        num = randint(0, 4)
        row.append(num)
        if num != 0:
            product *= num
    matrix.append(row)

for row in matrix:
    for num in row:
        print(num, end="\t")
    print()

print("Произведение ненулевых элементов:", product)

print("-" * 30)

# Задание 3
matrix = []
new_row = []

for i in range(6):
    row = []
    for j in range(6):
        row.append(randint(0, 10))
    matrix.append(row)

for i in range(6):
    new_row.append(randint(0, 10))

print("Исходный список:")
for row in matrix:
    for num in row:
        print(num, end="\t")
    print()

print(new_row)

for i in range(1, len(matrix), 2):
    matrix[i] = new_row[:]

print("Измененный список:")
for row in matrix:
    for num in row:
        print(num, end="\t")
    print()

