# Задание 1
s = input("Введите строку: ")
first_h = s.find('h')
last_h = s.rfind('h')
result = s[:first_h] + s[last_h + 1:]
print(result)

print("-" * 30)

# Задание 2
s = input("Введите строку: ")
first_h = s.find('h')
last_h = s.rfind('h')
middle = s[first_h + 1:last_h][::-1]
result = s[:first_h + 1] + middle + s[last_h:]
print(result)

print("-" * 30)

# Задание 3
s = input("Строка: ")
old = input("Ее заменяемая подстрока: ")
new = input("Новая подстрока: ")
result = s.replace(old, new)
print(result)

print("-" * 30)

# Задание 4
text = """Ежевику для ежат
Принесли два ежа.
Ежевику еле-еле
Ежата возле ели съели."""

words = text.split()
count = 0
for word in words:
    if word.lower().startswith('е'):
        count += 1

print("Количество слов:", count)