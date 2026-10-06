# Вариант A: обычные сеттеры и геттеры
class Point:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def set_x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x
        else:
            print("Должно быть число")

    def get_y(self):
        return self.__y

    def set_y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y
        else:
            print("Должно быть число")

p1 = Point(10, 20)
print("Исходная каордината x:", p1.get_x())
p1.set_x(50)
print("Новая каордината x:", p1.get_x())

print("-" * 30)

# Вариант B: через @property
class PointProp:
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if isinstance(x, (int, float)):
            self.__x = x
        else:
            print("Должно быть число")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if isinstance(y, (int, float)):
            self.__y = y
        else:
            print("Должно быть число")

p2 = PointProp(10, 20)
print("Исходная каордината x:", p2.x)
p2.x = 50
print("Новая каордината x:", p2.x)