from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, color="white"):
        self.color = color

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def info(self):
        pass


class Square(Shape):
    def __init__(self, side, color="red"):
        super().__init__(color)
        self.side = side

    def perimeter(self):
        return 4 * self.side

    def area(self):
        return self.side ** 2

    def draw(self):
        for i in range(self.side):
            print("*" * self.side)

    def info(self):
        print("===Квадрат===")
        print(f"Сторона: {self.side}")
        print(f"Цвет: {self.color}")
        print(f"Плошадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")


class Rectangle(Shape):
    def __init__(self, length, width, color="green"):
        super().__init__(color)
        self.length = length
        self.width = width

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def draw(self):
        for i in range(self.width):
            print("*" * self.length)

    def info(self):
        print("===Прямоугольник===")
        print(f"Длина: {self.length}")
        print(f"Ширина: {self.width}")
        print(f"Цвет: {self.color}")
        print(f"Плошадь: {self.area()}")
        print(f"Периметр: {self.perimeter()}")


class Triangle(Shape):
    def __init__(self, a, b, c, color="yellow"):
        super().__init__(color)
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5

    def draw(self):
        for i in range(1, self.a + 1):
            print(" " * (self.a - i) + "*" * (2 * i - 1))

    def info(self):
        print("===Треугольник===")
        print(f"Сторона 1: {self.a}")
        print(f"Сторона 2: {self.b}")
        print(f"Сторона 3: {self.c}")
        print(f"Цвет: {self.color}")
        print(f"Плошадь: {self.area():.2f}")
        print(f"Периметр: {self.perimeter()}")


figures = [
    Square(3, "red"),
    Rectangle(5, 3, "green"),
    Triangle(5, 4, 4, "yellow")
]

for fig in figures:
    fig.info()
    fig.draw()
    print()