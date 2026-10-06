from jinja2 import Environment, FileSystemLoader

users = ["Аня", "Петя", "Коля"]

env = Environment(loader=FileSystemLoader("templates"))
template = env.get_template("main.html")
page = template.render(title="Домашнее задание", users=users)

with open("result.html", "w", encoding="utf-8") as file:
    file.write(page)

print("Файл result.html создан")
