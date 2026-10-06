from flask import Flask, render_template

app = Flask(__name__)

pages = {
    "home": {"title": "Главная", "text": "Это главная страница моего сайта."},
    "about": {"title": "О сайте", "text": "Сайт сделан для домашнего задания по Flask."},
    "python": {"title": "Python", "text": "Python нужен для создания программ и сайтов."},
    "contacts": {"title": "Контакты", "text": "Моя почта: student@example.com"}
}


@app.route("/")
def home():
    return render_template("page.html", page=pages["home"], pages=pages)


@app.route("/<name>")
def page(name):
    if name not in pages:
        name = "home"
    return render_template("page.html", page=pages[name], pages=pages)


if __name__ == "__main__":
    app.run(debug=True)
