from functools import wraps

# Задание 1
def repeat(n):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

@repeat(3)
def say_hi():
    print("Hi")

say_hi()
print("-" * 20)

# Задание 2
def multiply_by_two(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 2
    return wrapper

@multiply_by_two
def add(a, b):
    return a + b

print(add(2, 3))
print("-" * 20)

# Задание 3
is_admin = False

def check_admin(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        global is_admin
        if is_admin:
            return func(*args, **kwargs)
        else:
            print("Доступ запрещен!")
            return None
    return wrapper

@check_admin
def greet():
    print("Hello World")

greet()
print()

is_admin = True
greet()
print("-" * 20)

# Задание 4
def start_end(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print("Начало")
        result = func(*args, **kwargs)
        print("Конец")
        return result
    return wrapper

@start_end
def say_hello():
    print("Привет!")

say_hello()