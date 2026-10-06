# Задание 1
numbers = [3, 7, 2, 5, 2, 8, 3, 9, 5, 1, 7, 4, 3, 6, 1]
print("Исходный список:", numbers)

result = []
for num in numbers:
    if numbers.count(num) == 1:
        result.append(num)

print("Очищенный список:")
print(result)

print("-" * 30)

# Задание 2
for i in range(len(result)):
    for j in range(len(result) - 1):
        if result[j] > result[j + 1]:
            result[j], result[j + 1] = result[j + 1], result[j]

print("Очищенный список по возрастанию:")
print(result)
