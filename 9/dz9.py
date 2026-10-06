# Задание 1
def convert_temperature(value, scale):
    scale = scale.upper()
    if scale == "C":
        return value * 9 / 5 + 32
    if scale == "F":
        return (value - 32) * 5 / 9
    return None

value = int(input("Введите температуру: "))
scale = input("Введите шкалу (C или F): ")
result = convert_temperature(value, scale)

if result is None:
    print("Неверная шкала температуры")
elif scale.upper() == "C":
    print(f"{value} C -> {result:.2f} F")
else:
    print(f"{value} F -> {result:.2f} C")

print("-" * 30)

# Задание 2
def change(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

lists = [
    [1, 2, 3],
    [9, 12, 33, 54, 105],
    ['c', 'л', 'о', 'н']
]

for item in lists:
    print("Исходный список:", item)
    print("Результат:", change(item))
