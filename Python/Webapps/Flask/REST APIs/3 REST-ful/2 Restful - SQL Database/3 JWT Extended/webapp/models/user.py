from db import db

class UserModel(db.Model): #Se extiende la clase para indicarle a SQLAlchemy que sera mapeada a una base de datos

    #Decirle a SQLAlchemy cual es la tabla
    __tablename__ = 'users'

    #Decirle a SQLAlchemy cuales son las columnas de la tabla
    id = db.Column(db.Integer, primary_key=True) #Campo de enteros, autoincremental
    username = db.Column(db.String(80)) #Campo de string, maximo 80 caracteres
    password = db.Column(db.String(80))


    def __init__(self, username, password):
        self.username = username # El nombre de la variable del objeto debe hacer match con el nombre de la columna de la base de datos, declarado arriba, para que haga efecto el mapeo de SQLAlchemy
        self.password = password
        #self.something = 'something' #El objeto puede tener mas atributos, simplemente estos no seran guardados en la base de datos

    def json(self):
        return {
            'id':self.id,
            'username':self.username
        }

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod # Es un class method porque al ser llamado, devuelve un objeto de la clase, es un contructor
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
