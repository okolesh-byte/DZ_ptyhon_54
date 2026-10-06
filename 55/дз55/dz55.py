from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    products = relationship("Product", back_populates="category")


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Float)
    count = Column(Integer)
    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship("Category", back_populates="products")


engine = create_engine("sqlite:///shop_sqlalchemy.db")
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

food = Category(name="Еда")
drink = Category(name="Напитки")
session.add(food)
session.add(drink)
session.commit()

data = [
    ("Хлеб", 45, 20, food),
    ("Сыр", 320, 8, food),
    ("Рис", 90, 18, food),
    ("Печенье", 95, 16, food),
    ("Шоколад", 120, 9, food),
    ("Молоко", 80, 15, drink),
    ("Чай", 150, 12, drink),
    ("Кофе", 500, 5, drink),
    ("Сок", 100, 11, drink),
    ("Вода", 50, 30, drink)
]

for name, price, count, category in data:
    session.add(Product(name=name, price=price, count=count, category=category))

session.commit()

for product in session.query(Product).all():
    print(product.name, product.price, product.count, product.category.name)

session.close()
