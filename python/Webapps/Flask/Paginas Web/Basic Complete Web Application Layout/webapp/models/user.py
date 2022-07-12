from database import db

class UserModel(db.Model):

    # Tabla a la que esta relacionada el objeto UserModel
    __tablename__ = "users"

    # Definir columnas de la tabla
    id = db.Column(db.Integer, primary_key=True)                                # Campo autoinremental
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    password = db.Column(db.String(100))


    # Funcion constructora del objeto
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    # Funcion para guardar en la pagina web
    def save(self):
        db.session.add(self)
        db.session.commit()

    # Funcion para devolver un objeto identificado por email de la base de datos
    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
