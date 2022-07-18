import sqlalchemy
import sqlalchemy as sq
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale

Base = declarative_base()

DSN = "postgresql://postgres:49@localhost:5432/netology_db"
engine = sqlalchemy.create_engine(DSN)
create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

input_name = input("Введите имя автора или id").lower()
for author in session.query(Publisher).filter(Publisher.name == input_name or Publisher.id == input_name).all():
    print(author)

<<<<<<< HEAD
for c in session.query(Shop).filter(Publisher.name == input_name or Publisher.id == input_name).all():
    print(Shop)

    # Надеюсь, я правильно поняла, что имелось ввиду под целевым издателем


session.close()
