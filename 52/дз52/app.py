from datetime import datetime

from flask import Flask, render_template

app = Flask(__name__)

menu = [
    {"endpoint": "index", "title": "Главная"},
    {"endpoint": "income", "title": "Доходы"},
    {"endpoint": "costs", "title": "Расходы"},
    {"endpoint": "contacts", "title": "Контакты"},
]

income_items = [
    {"name": "Стипендия", "value": "7 500 руб", "text": "Постоянный доход студента."},
    {"name": "Подработка", "value": "12 000 руб", "text": "Деньги которые можно откладывать."},
    {"name": "Помощь семьи", "value": "5 000 руб", "text": "Лучше записывать отдельно."},
]

cost_items = [
    {"name": "Еда", "value": "9 000 руб", "text": "Главная трата в месяц."},
    {"name": "Транспорт", "value": "2 000 руб", "text": "Проезд и поездки."},
    {"name": "Связь", "value": "800 руб", "text": "Телефон и интернет."},
]


def context(active, title):
    return {
        "menu": menu,
        "active": active,
        "title": title,
        "year": datetime.now().year,
    }


@app.route("/")
def index():
    return render_template("index.html", **context("index", "Главная"))


@app.route("/income/")
def income():
    return render_template("income.html", items=income_items, **context("income", "Доходы"))


@app.route("/costs/")
def costs():
    return render_template("costs.html", items=cost_items, **context("costs", "Расходы"))


@app.route("/contacts/")
def contacts():
    return render_template("contacts.html", **context("contacts", "Контакты"))


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", **context("", "Ошибка")), 404


if __name__ == "__main__":
    app.run(debug=True)
