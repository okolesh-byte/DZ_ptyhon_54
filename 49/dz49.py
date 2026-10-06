from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    books = relationship("Book", back_populates="author")


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    year = Column(Integer)
    author_id = Column(Integer, ForeignKey("authors.id"))
    author = relationship("Author", back_populates="books")


engine = create_engine("sqlite:///library.db")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

names = ["Пушкин", "Толстой", "Гоголь", "Булгаков", "Тургенев"]
authors = []
for name in names:
    author = Author(name=name)
    session.add(author)
    authors.append(author)

session.commit()

books = [
    ("Капитанская дочка", 1836, authors[0]),
    ("Евгений Онегин", 1833, authors[0]),
    ("Война и мир", 1869, authors[1]),
    ("Анна Каренина", 1877, authors[1]),
    ("Мертвые души", 1842, authors[2]),
    ("Ревизор", 1836, authors[2]),
    ("Мастер и Маргарита", 1967, authors[3]),
    ("Собачье сердце", 1925, authors[3]),
    ("Отцы и дети", 1862, authors[4]),
    ("Ася", 1858, authors[4])
]

for title, year, author in books:
    session.add(Book(title=title, year=year, author=author))

session.commit()

for book in session.query(Book).all():
    print(book.id, book.title, book.year, book.author.name)

session.close()
