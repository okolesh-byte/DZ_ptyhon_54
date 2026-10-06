class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Line:
    def __init__(self, sp, ep, color="red", width=1):
        self.sp = sp
        self.ep = ep
        self.color = color
        self.width = width
        self.check_int()

    def check_int(self):
        if not (isinstance(self.sp.x, int) and isinstance(self.sp.y, int) and
                isinstance(self.ep.x, int) and isinstance(self.ep.y, int) and
                isinstance(self.width, int)):
            raise ValueError("Каординаты должны быть целочислеными")

    def draw(self):
        print(f"Рисование линии: ({self.sp.x}, {self.sp.y}), ({self.ep.x}, {self.ep.y}), {self.color}, {self.width}")

class Rect:
    def __init__(self, sp, ep, color="red", width=1):
        self.sp = sp
        self.ep = ep
        self.color = color
        self.width = width
        self.check_num()

    def check_num(self):
        if not (isinstance(self.sp.x, (int, float)) and isinstance(self.sp.y, (int, float)) and
                isinstance(self.ep.x, (int, float)) and isinstance(self.ep.y, (int, float)) and
                isinstance(self.width, (int, float))):
            raise ValueError("Каординаты должны быть числами")

    def draw(self):
        print(f"Рисование прямоугольника: ({self.sp.x}, {self.sp.y}), ({self.ep.x}, {self.ep.y}), {self.color}, {self.width}")

try:
    l1 = Line(Point(1, 2), Point(10, 20), "red", 1)
    l1.draw()
except ValueError as e:
    print(e)

try:
    l2 = Line(Point(10.2, 20), Point(100, 200), "green", 3)
    l2.draw()
except ValueError as e:
    print(e)

try:
    r1 = Rect(Point(7, 9), Point(12, 15), "red", 1)
    r1.draw()
except ValueError as e:
    print(e)

try:
    r2 = Rect(Point(30.5, 40.2), Point(50, 60), "red", 1)
    r2.draw()
except ValueError as e:
    print(e)