while True:
    print("\n--- Калькулятор ---")
    print("1. Сложение (+)")
    print("2. Вычитание (-)")
    print("3. Умножение (*)")
    print("4. Деление (/)")
    print("5. Возведение в степень (**)")
    print("6. Целочисленное деление (//)")
    print("7. Остаток от деления (%)")
    print("8. Минимум из двух чисел")
    print("9. Максимум из двух чисел")
    print("0. Выход")

    operation = input("Выберите номер операции: ")

    if operation == "0":
        print("Программа завершена.")
        break

    if operation not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("Ошибка! Введите номер от 0 до 9.")
        continue

    try:
        num1 = float(input("Введите первое число: "))
        num2 = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка! Нужно ввести число.")
        continue

    result = 0
    error = False

    if operation == "1":
        result = num1 + num2
    elif operation == "2":
        result = num1 - num2
    elif operation == "3":
        result = num1 * num2
    elif operation == "4":
        try:
            result = num1 / num2
        except ZeroDivisionError:
            print("Делить на ноль нельзя!")
            error = True
    elif operation == "5":
        result = num1 ** num2
    elif operation == "6":
        try:
            result = num1 // num2
        except ZeroDivisionError:
            print("Делить на ноль нельзя!")
            error = True
    elif operation == "7":
        try:
            result = num1 % num2
        except ZeroDivisionError:
            print("Делить на ноль нельзя!")
            error = True
    elif operation == "8":
        result = min(num1, num2)
    elif operation == "9":
        result = max(num1, num2)

    if not error:
        if result == int(result):
            result = int(result)
        print("Результат:", result)