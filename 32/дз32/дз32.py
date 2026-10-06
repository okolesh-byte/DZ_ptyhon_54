class Point3D:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __add__(self, other):
        return Point3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point3D(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        return Point3D(self.x * other.x, self.y * other.y, self.z * other.z)

    def __truediv__(self, other):
        return Point3D(self.x / other.x, self.y / other.y, self.z / other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __getitem__(self, key):
        if key == "x": return self.x
        if key == "y": return self.y
        if key == "z": return self.z

    def __setitem__(self, key, value):
        if key == "x": self.x = value
        if key == "y": self.y = value
        if key == "z": self.z = value

    def __str__(self):
        return f"({self.x}, {self.y}, {self.z})"

p1 = Point3D(12, 15, 18)
p2 = Point3D(6, 3, 9)

print(f"Каординаты 1-й точки: {p1.x}, {p1.y}, {p1.z}")
print(f"Каординаты 2-й точки: {p2.x}, {p2.y}, {p2.z}")
print(f"Сложение каординат: {p1 + p2}")
print(f"Вычитание каординат: {p1 - p2}")
print(f"Умножение: {p1 * p2}")
print(f"Деление: {p1 / p2}")
print(f"Равенство каординат: {p1 == p2}")

print(f"x = {p1.x} x1 = {p2.x}")
print(f"y = {p1.y} y1 = {p2.y}")
print(f"z = {p1.z} z1 = {p2.z}")

p1["x"] = 20
print(f"Запись значения в каординату x: {p1['x']}")