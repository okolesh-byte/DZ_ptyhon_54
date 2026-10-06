filename = "countries.txt"


def load_data():
    countries = {}
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line:
                    country, capital = line.split(";")
                    countries[country] = capital
    return countries


def save_data(countries):
    with open(filename, "w", encoding="utf-8") as f:
        for country, capital in countries.items():
            f.write(f"{country};{capital}\n")
    print("Файл сохранен")


import os

countries = load_data()


def add_data():
    country = input("Введите название страны (с заглавной буквы): ")
    capital = input("Введите название столицы страны (с заглавной буквы): ")
    countries[country] = capital
    save_data(countries)


def delete_data():
    country = input("Введите страну для удаления: ")
    if country in countries:
        del countries[country]
        save_data(countries)
        print(f"{country} удалена")
    else:
        print("Страна не найдена")


def search_data():
    country = input("Введите страну для поиска: ")
    if country in countries:
        print(f"Столица: {countries[country]}")
    else:
        print("Страна не найдена")


def edit_data():
    country = input("Введите страну для редактирования: ")
    if country in countries:
        new_capital = input("Введите новую столицу: ")
        countries[country] = new_capital
        save_data(countries)
        print("Данные обновлены")
    else:
        print("Страна не найдена")


def view_data():
    print(countries)


while True:
    print("**************************")
    print("Выбор действия:")
    print("1 - добавление данных")
    print("2 - удаление данных")
    print("3 - поиск данных")
    print("4 - редактирование данных")
    print("5 - просмотр данных")
    print("6 - завершение работы")

    choice = input("Ввод: ")

    if choice == "1":
        add_data()
    elif choice == "2":
        delete_data()
    elif choice == "3":
        search_data()
    elif choice == "4":
        edit_data()
    elif choice == "5":
        view_data()
    elif choice == "6":
        break
    else:
        print("Неверный выбор")