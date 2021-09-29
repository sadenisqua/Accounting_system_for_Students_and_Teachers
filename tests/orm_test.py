import sqlalchemy
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import declarative_base, sessionmaker

print(sqlalchemy.__version__)

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:7910dk123@localhost:5432/testdb')

connection = engine.connect()

result = connection.execute("SELECT * FROM book")
for row in result:
    print('title', row['title'])

result.close()

trans = connection.begin()
try:
    connection.execute("INSERT INTO book(bood_id, title, isn, fk_publisher_id) VALUES (35, 'worst book', 12345, 2)")
    trans.commit()
except:
    trans.rollback()
    raise

with connection.begin() as trans:
    connection.execute("INSERT INTO book(bood_id, title, isn, fk_publisher_id) VALUES (65, 'best book', 12345, 1)")

Base = declarative_base()


class Author(Base):
    __table__name = 'author'

    author_id = Column(Integer, primary_key=True)
    full_name = Column(String)
    rating = Column(Float)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

session = Session()

author = Author(author_id=18, full_name='Dan Brown', rating=4.7)
session.add(author)

session.commit()
session.flush()

for item in session.query(Author).order_by(Author.rating):
    print(item.full_name, ' ', item.rationg)

for item in session.query(Author).filter(Author.rating > 4.5):
    print(item.full_name, ' ', item.rationg)