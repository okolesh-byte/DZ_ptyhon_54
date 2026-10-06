import sqlite3

con = sqlite3.connect("library.db")
cur = con.cursor()

queries = [
    "SELECT * FROM authors",
    "SELECT * FROM books",
    "SELECT title, year FROM books ORDER BY year",
    "SELECT title FROM books WHERE year > 1900",
    "SELECT title FROM books WHERE title LIKE '%а%'",
    "SELECT authors.name, books.title FROM authors, books WHERE authors.id = books.author_id",
    "SELECT authors.name, COUNT(books.id) FROM authors, books WHERE authors.id = books.author_id GROUP BY authors.name",
    "SELECT AVG(year) FROM books",
    "SELECT title FROM books WHERE year = (SELECT MIN(year) FROM books)",
    "SELECT title FROM books WHERE year = (SELECT MAX(year) FROM books)"
]

for i, query in enumerate(queries, 1):
    print("Запрос", i)
    print(query)
    for row in cur.execute(query):
        print(row)
    print("-" * 30)

con.close()
