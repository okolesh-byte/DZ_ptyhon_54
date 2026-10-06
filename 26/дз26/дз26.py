import math

# Задание 1: Класс Rectangle
class Rectangle:
    def __init__(self, length, width):
        # Приватное свойство длины
        self.__length = length
        # Приватное свойство ширины
        self.__width = width

    # Метод получения длины
    def get_length(self):
        return self.__length

    # Метод получения ширины
    def get_width(self):
        return self.__width

    # Метод вычисления площади
    def area(self):
        return self.__length * self.__width

    # Метод вычисления периметра
    def perimeter(self):
        return 2 * (self.__length + self.__width)

    # Метод вычисления диагонали (гипотенузы)
    def diagonal(self):
        return math.sqrt(self.__length**2 + self.__width**2)

    # Метод отрисовки прямоугольника
    def draw(self):
        for i in range(int(self.__width)):
            print("*" * int(self.__length))

length = 3
width = 9
rect = Rectangle(length, width)

print(f"Длина прямоугольника: {rect.get_length()}")
print(f"Ширина прямоугольника: {rect.get_width()}")
print(f"Площадь прямоугольника: {rect.area()}")
print(f"Периметр прямоугольника: {rect.perimeter()}")
print(f"Гипотенуза прямоугольника: {rect.diagonal():.2f}")
rect.draw()

print("-" * 30)

# Задание 2: Конвертер кг в фунты с @property
class WeightConverter:
    def __init__(self, kg):
        # Приватное свойство килограммов
        self.__kg = kg

    # Геттер для свойства kg
    @property
    def kg(self):
        return self.__kg

    # Сеттер для свойства kg с проверкой на число
    @kg.setter
    def kg(self, value):
        if isinstance(value, (int, float)):
            self.__kg = value
        else:
            print("Килограммы задаются только числами")

    # Метод перевода в фунты
    def to_pounds(self):
        return self.__kg * 2.20462

conv = WeightConverter(12)
print(f"{conv.kg} кг => {conv.to_pounds():.2f} фунтов")

conv.kg = 41
print(f"{conv.kg} кг => {conv.to_pounds():.3f} фунтов")

# Проверка сеттера (попытка передать строку)
conv.kg = "abc"