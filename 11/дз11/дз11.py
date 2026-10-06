tup = ('ab', 'abcd', 'cde', 'abc', 'def')
print("Исходный кортеж:", tup)

s = input("s = ")
if s in tup:
    print("Yes")
else:
    print("No")

print("-" * 30)

text = input("Введите по порядку, без пробелов, элементы кортежа: ")
tup2 = tuple(text)
print(tup2)

unique = []
for i in tup2:
    if i not in unique:
        unique.append(i)

for i in unique:
    count = tup2.count(i)
    print("Количество", i, "=", count)

print("-" * 30)

winning_numbers = {7, 15, 23, 42, 88}
user_num = int(input("Введите число от 1 до 100: "))

if user_num in winning_numbers:
    print("Поздравляем, вы угадали!")
else:
    print("Попробуйте еще раз")