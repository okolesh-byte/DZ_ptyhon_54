secret_number = 56
attempts = 0

print("Игра 'Угадай число'")
print("Для выхода введите 0")

while True:
    guess_str = input("Введите число от 1 до 100: ")

    if guess_str == "0":
        print("Игра завершена.")
        break

    try:
        guess = int(guess_str)
    except ValueError:
        print("Нужно ввести целое число.")
        continue

    if guess < 1 or guess > 100:
        print("Число должно быть в диапазоне от 1 до 100.")
        continue

    attempts += 1

    if guess < secret_number:
        print("загаданное число больше")
    elif guess > secret_number:
        print("загаданное число меньше")
    else:
        print(f"Вы угадали загаданное число с {attempts} раза")
        break