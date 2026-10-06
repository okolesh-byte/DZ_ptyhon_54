# Задание 1
numbers = []
n = int(input("n = "))

for i in range(n):
    numbers.append(int(input("-> ")))

for i in range(0, len(numbers), 2):
    print(numbers[i], end=" ")
print()

print("-" * 30)

# Задание 2
numbers = []
n = int(input("n = "))

for i in range(n):
    numbers.append(int(input("-> ")))

for i in range(1, len(numbers)):
    if numbers[i] > numbers[i - 1]:
        print(numbers[i], end=" ")
print()

print("-" * 30)

# Задание 3
n = int(input("Высота треугольника: "))

for i in range(1, n + 1):
    print("*" * i)

print()

for i in range(n, 0, -1):
    print("*" * i)

print("-" * 30)

# Дополнительно
size = int(input("Введите размер поля: "))
count = int(input("Введите количество символов: "))

for row in range(size):
    for col in range(size):
        if (row + col) % 2 == 0:
            print("* " * count, end="")
        else:
            print("  " * count, end="")
    print()
