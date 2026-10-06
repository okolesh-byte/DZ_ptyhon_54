import sqlite3

con = sqlite3.connect("shop.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS products")
cur.execute("""
CREATE TABLE products (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    price REAL,
    count INTEGER
)
""")

products = [
    ("Хлеб", 45, 20),
    ("Молоко", 80, 15),
    ("Сыр", 320, 8),
    ("Чай", 150, 12),
    ("Кофе", 500, 5),
    ("Сахар", 70, 30),
    ("Соль", 35, 25),
    ("Рис", 90, 18),
    ("Макароны", 75, 22),
    ("Яблоки", 110, 14),
    ("Бананы", 130, 10),
    ("Картофель", 40, 35),
    ("Морковь", 55, 21),
    ("Печенье", 95, 16),
    ("Шоколад", 120, 9)
]

cur.executemany("INSERT INTO products (name, price, count) VALUES (?, ?, ?)", products)
con.commit()

for row in cur.execute("SELECT * FROM products"):
    print(row)

con.close()
