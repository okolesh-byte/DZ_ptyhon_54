
number = input("Введите пятизначное число: ").strip()
product = 1
total = 0
for digit in number:
    n = int(digit)
    product *= n
    total += n
mean = total / len(number)
print("Произведение цифр:", product)
print("Среднее арифметическое:", mean)

print("-" * 30)


n1 = float(input("Введите первое число: "))
n2 = float(input("Введите второе число: "))
n3 = float(input("Введите третье число: "))
n4 = float(input("Введите четвертое число: "))
sum_first = n1 + n2
sum_last = n3 + n4
result = sum_first / sum_last
print(f"Результат: {result:.2f}")

print("-" * 30)


a = 10
b = 20
print("До замены: a =", a, "b =", b)
a, b = b, a
print("После замены: a =", a, "b =", b)