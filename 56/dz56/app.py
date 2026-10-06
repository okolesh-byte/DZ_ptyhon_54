import sqlite3
from flask import Flask, render_template

app = Flask(__name__)


def create_db():
    con = sqlite3.connect("site.db")
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS pages")
    cur.execute("""
    CREATE TABLE pages (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        url TEXT,
        menu TEXT,
        title TEXT,
        content TEXT
    )
    """)
    data = [
        ("home", "Главная", "Главная", "Добро пожаловать на мой сайт."),
        ("about", "О сайте", "О сайте", "Это сайт для домашнего задания."),
        ("python", "Python", "Python", "Python простой и удобный язык."),
        ("contacts", "Контакты", "Контакты", "Связь: student@example.com")
    ]
    cur.executemany("INSERT INTO pages (url, menu, title, content) VALUES (?, ?, ?, ?)", data)
    con.commit()
    con.close()


def get_pages():
    con = sqlite3.connect("site.db")
    cur = con.cursor()
    cur.execute("SELECT url, menu, title, content FROM pages")
    pages = cur.fetchall()
    con.close()
    return pages


def get_page(url):
    con = sqlite3.connect("site.db")
    cur = con.cursor()
    cur.execute("SELECT url, menu, title, content FROM pages WHERE url = ?", (url,))
    page = cur.fetchone()
    con.close()
    return page


@app.route("/")
def home():
    pages = get_pages()
    page = get_page("home")
    return render_template("page.html", pages=pages, page=page)


@app.route("/<url>")
def page(url):
    pages = get_pages()
    item = get_page(url)
    if item is None:
        item = get_page("home")
    return render_template("page.html", pages=pages, page=item)


if __name__ == "__main__":
    create_db()
    app.run(debug=True)
