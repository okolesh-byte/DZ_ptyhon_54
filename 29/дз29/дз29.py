class Liquid:
    def __init__(self, name, density):
        self.name = name
        self.density = density

    def change_density(self, new_density):
        self.density = new_density

    def volume(self, mass):
        return mass / self.density

    def mass(self, vol):
        return vol * self.density

    def print_info(self):
        print(f"Жидкость '{self.name}' (плотность = {self.density} kg/m^3).")

class Alcohol(Liquid):
    def __init__(self, name, density, strength):
        super().__init__(name, density)
        self.strength = strength

    def change_strength(self, new_strength):
        self.strength = new_strength

w = Alcohol("Wine", 1064.2, 14)
w.print_info()
w.change_density(1080)
w.print_info()

print()
print(f"Вес 0.5 m^3 of {w.name} саставляет {w.mass(0.5)} кг.")
print(f"Объем 300 кг {w.name} равен {w.volume(300)} m^3.")

print()
print(w.strength)
w.change_strength(20)
print(w.strength)