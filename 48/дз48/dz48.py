import sqlite3

con = sqlite3.connect("students.db")
cur = con.cursor()

cur.execute("DROP TABLE IF EXISTS students")
cur.execute("""
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    group_name TEXT,
    mark INTEGER
)
""")

data = [
    ("Иванов", "П-11", 5),
    ("Петров", "П-11", 4),
    ("Сидоров", "П-11", 3),
    ("Кузнецов", "П-12", 5),
    ("Смирнов", "П-12", 4),
    ("Васильев", "П-12", 3),
    ("Федоров", "П-13", 5),
    ("Морозов", "П-13", 4),
    ("Новиков", "П-13", 3),
    ("Соколов", "П-14", 5),
    ("Попов", "П-14", 4),
    ("Лебедев", "П-14", 3),
    ("Козлов", "П-15", 5),
    ("Зайцев", "П-15", 4),
    ("Павлов", "П-15", 3)
]

cur.executemany("INSERT INTO students (name, group_name, mark) VALUES (?, ?, ?)", data)
con.commit()

for row in cur.execute("SELECT * FROM students"):
    print(row)

con.close()
