class Film:
    def __init__(self, name, genre, director, year, time, studio, actors):
        self.name = name
        self.genre = genre
        self.director = director
        self.year = year
        self.time = time
        self.studio = studio
        self.actors = actors


class Model:
    def __init__(self):
        self.films = []

    def add_film(self, film):
        self.films.append(film)

    def get_all(self):
        return self.films

    def get_one(self, number):
        if 0 <= number < len(self.films):
            return self.films[number]
        return None

    def delete_film(self, number):
        if 0 <= number < len(self.films):
            return self.films.pop(number)
        return None


class View:
    def menu(self):
        print("===== Редактирование данных каталога фильмов =====")
        print("Действия с фильмами:")
        print("1 - добавление фильма")
        print("2 - каталог фильмов")
        print("3 - просмотр определенного фильма")
        print("4 - удаление фильма")
        print("q - выход из программы")
        return input("Выберите вариант действия: ")

    def input_film(self):
        name = input("Название фильма: ")
        genre = input("Жанр: ")
        director = input("Режисер: ")
        year = input("Год выпуска: ")
        time = input("Длительность: ")
        studio = input("Студия: ")
        actors = input("Актеры: ")
        return Film(name, genre, director, year, time, studio, actors)

    def show_film(self, film):
        if film is None:
            print("Такого фильма нет")
            return
        print("Название:", film.name)
        print("Жанр:", film.genre)
        print("Режисер:", film.director)
        print("Год выпуска:", film.year)
        print("Длительность:", film.time)
        print("Студия:", film.studio)
        print("Актеры:", film.actors)

    def show_all(self, films):
        if len(films) == 0:
            print("Каталог пуст")
            return
        for i, film in enumerate(films, 1):
            print(i, "-", film.name)

    def input_number(self):
        return int(input("Номер фильма: ")) - 1


class Controller:
    def __init__(self):
        self.model = Model()
        self.view = View()

    def run(self):
        while True:
            choice = self.view.menu()
            if choice == "1":
                film = self.view.input_film()
                self.model.add_film(film)
                print("Фильм добавлен")
            elif choice == "2":
                self.view.show_all(self.model.get_all())
            elif choice == "3":
                number = self.view.input_number()
                self.view.show_film(self.model.get_one(number))
            elif choice == "4":
                number = self.view.input_number()
                film = self.model.delete_film(number)
                if film is None:
                    print("Такого фильма нет")
                else:
                    print("Фильм удален")
            elif choice == "q":
                break
            else:
                print("Неверный пункт меню")
            print("=" * 40)


app = Controller()
app.run()
