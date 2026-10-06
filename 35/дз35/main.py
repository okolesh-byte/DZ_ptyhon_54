from figures import Circle, Rectangle, Cylinder

c = Circle(5)
print(f"Круг: радиус={c.radius}, плошадь={c.area():.2f}, периметр={c.perimeter():.2f}")

r = Rectangle(4, 6)
print(f"Прямоугольник: {r.length}x{r.width}, плошадь={r.area()}, периметр={r.perimeter()}")

cyl = Cylinder(3, 7)
print(f"Цилиндр: r={cyl.radius}, h={cyl.height}, обьём={cyl.volume():.2f}, площадь={cyl.surface():.2f}")