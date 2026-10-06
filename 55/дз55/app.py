from datetime import datetime
import sqlite3
from pathlib import Path

from flask import Flask, render_template

app = Flask(__name__)
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "site.db"


def get_connection():
    con = sqlite3.connect(DB_PATH)
    con.row_factory = sqlite3.Row
    return con


def init_db():
    con = get_connection()
    cur = con.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS menu (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        endpoint TEXT,
        title TEXT,
        position INTEGER
    )
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS pages (
        endpoint TEXT PRIMARY KEY,
        title TEXT,
        heading TEXT,
        lead TEXT,
        body TEXT
    )
    """)

    cur.execute("SELECT COUNT(*) FROM menu")
    if cur.fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO menu (endpoint, title, position) VALUES (?, ?, ?)",
            [
                ("index", "Главная", 1),
                ("income", "Доходы", 2),
                ("costs", "Расходы", 3),
                ("contacts", "Контакты", 4),
            ],
        )

    cur.execute("SELECT COUNT(*) FROM pages")
    if cur.fetchone()[0] == 0:
        cur.executemany(
            "INSERT INTO pages (endpoint, title, heading, lead, body) VALUES (?, ?, ?, ?, ?)",
            [
                ("index", "Главная", "Учёт личных финансов", "Простой сайт для контроля денег.", "Тут можно смотреть доходы, расходы и понимать куда уходят деньги."),
                ("income", "Доходы", "Доходы за месяц", "Деньги которые приходят студенту.", "Стипендия, подработка и помощь семьи записываються отдельно."),
                ("costs", "Расходы", "Расходы за месяц", "Траты надо записывать каждый день.", "Если не следить за расходами, можно быстро уйти в минус."),
                ("contacts", "Контакты", "Связь", "Страница для связи с автором.", "Почта: student@example.com"),
            ],
        )

    con.commit()
    con.close()


def get_menu():
    con = get_connection()
    items = con.execute("SELECT endpoint, title FROM menu ORDER BY position").fetchall()
    con.close()
    return items


def get_page(endpoint):
    con = get_connection()
    page = con.execute("SELECT * FROM pages WHERE endpoint = ?", (endpoint,)).fetchone()
    con.close()
    return page


def render_page(endpoint):
    menu = get_menu()
    page = get_page(endpoint)
    if page is None:
        page = get_page("index")
    return render_template("page.html", menu=menu, page=page, active=endpoint, year=datetime.now().year)


@app.route("/")
def index():
    return render_page("index")


@app.route("/income/")
def income():
    return render_page("income")


@app.route("/costs/")
def costs():
    return render_page("costs")


@app.route("/contacts/")
def contacts():
    return render_page("contacts")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("404.html", menu=get_menu(), active="", year=datetime.now().year), 404


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
