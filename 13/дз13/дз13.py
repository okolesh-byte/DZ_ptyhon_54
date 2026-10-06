# Задание 1
students = [("Иван", 25), ("Мария", 23), ("Петр", 25), ("Анна", 23)]

result = {}
for name, age in students:
    if age not in result:
        result[age] = []
    result[age].append(name)

print(result)

# Задание 2
nums = [1, 1, 1, 2, 2, 3]
k = 3

from collections import Counter
count = Counter(nums)
most_common = count.most_common(k)
result2 = [item[0] for item in most_common]

print(result2)

# Задание 3
dict1 = {
    1: {"name": "Иван", "age": 17},
    2: {"name": "Максим", "age": 27},
    3: {"name": "Петр", "age": 30}
}

dict2 = {
    2: {"name": "Мария", "age": 20},
    4: {"name": "Анна", "age": 22}
}

merged = {**dict1, **dict2}
filtered = {k: v for k, v in merged.items() if v["age"] >= 18}

print(filtered)