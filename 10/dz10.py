from math import pi


def rectangle_area(a, b):
    return a * b


def triangle_area(a, h):
    return a * h / 2


def circle_area(r):
    return pi * r ** 2


def read_positive_number(message):
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value
            print("Число должно быть больше 0")
        except ValueError:
            print("Введите число")


while True:
    try:
        figure = int(input("1 - прямоугольник, 2 - треугольник, 3 - круг, 0 - выход: "))
    except ValueError:
        print("Введите номер фигуры")
        continue

    if figure == 0:
        break
    if figure == 1:
        a = read_positive_number("Сторона a: ")
        b = read_positive_number("Сторона b: ")
        print(f"Площадь: {rectangle_area(a, b):.2f}")
    elif figure == 2:
        a = read_positive_number("Основание: ")
        h = read_positive_number("Высота: ")
        print(f"Площадь: {triangle_area(a, h):.2f}")
    elif figure == 3:
        r = read_positive_number("Радиус: ")
        print(f"Площадь: {circle_area(r):.2f}")
    else:
        print("Нет такой фигуры")
