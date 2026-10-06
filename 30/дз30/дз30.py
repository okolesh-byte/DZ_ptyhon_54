class Student:
    def __init__(self, name, laptop):
        self.name = name
        self.laptop = laptop

    def print_info(self):
        print(f"{self.name} => {self.laptop.model}, {self.laptop.processor}, {self.laptop.memory}")

    class Laptop:
        def __init__(self, model, processor, memory):
            self.model = model
            self.processor = processor
            self.memory = memory

# создаем вложеный класс
lap1 = Student.Laptop("HP", "i7", 16)
lap2 = Student.Laptop("HP", "i7", 16)

s1 = Student("Roman", lap1)
s2 = Student("Vladimir", lap2)

# вывод инфы
s1.print_info()
s2.print_info()