from datetime import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, DateTime, MetaData
from sqlalchemy.orm import sessionmaker
engine = create_engine(
    "postgresql://postgres:RouteUS-166@127.0.0.1:5432/sqlalchemy")
Base = declarative_base()
metadata_obj = MetaData()

#########################
# Crear modelo (tablas) #
#########################


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    email = Column(String(50), nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())

    def __str__(self):
        return self.username


Session = sessionmaker(engine)
session = Session()


def print_query_results(results):
    print("===============")
    for result in results:
        print(result)
    print("===============")


if __name__ == '__main__':
    # Borrar todo
    Base.metadata.drop_all(engine)
    # Crear todo
    Base.metadata.create_all(engine)

    #########################
    #   Anadir informacion  #
    #########################

    user1 = User(username='User1', email='user1@example.com')
    user2 = User(username='User2', email='user2@example.com')
    user3 = User(username='User3', email='user3@example.com')

    session.add(user1)
    session.add(user2)
    session.add(user3)

    session.commit()

    #########################
    #       Consultas       #
    #########################

    # https://www.tutorialspoint.com/sqlalchemy/sqlalchemy_orm_filter_operators.htm

    # SELECT * FROM users;
    # Returns User instances
    users = session.query(User).all()
    print_query_results(users)

    # SELECT * FROM users WHERE id >= 2
    # Returns and iterable
    users = session.query(User).filter(
        User.id >= 2
    )
    print_query_results(users)

    # SELECT * FROM users WHERE id >= 2 and username = 'User3'
    users = session.query(User).filter(
        User.id >= 2
    ).filter(
        User.username == 'User3'
    )
    print_query_results(users)

    # SELECT id, username FROM users
    # Return tuple (id, username)
    users = session.query(User.id, User.username).all()
    print_query_results(users)

    # Consultas unicas
    # Retornar el primer registro
    user = session.query(User).filter(User.id == 1).first()
    print(user)

    # Actualizar registros
    user = session.query(User).filter(User.id == 1).first()
    user.username = 'Nuevo user1'
    user.email = 'nuevouser1@gmail.com'
    session.add(user)
    session.commit()

    user = session.query(User).filter(User.id == 1).first()
    print(user)

    # Metodo update
    session.query(User).filter(
        User.id == 2
    ).update(
        {
            User.username: "Nuevo user 2",
            User.email: "nuevouser2@gmail.com"
        }
    )

    session.commit()

    user = session.query(User).filter(User.id == 2).first()
    print(user)

    # Borrar registros
    session.query(User).filter(
        User.id == 1
    ).delete()

    session.commit()
