from db import db


class ItemModel(db.Model): #Se extiende la clase para indicarle a SQLAlchemy que sera mapeada a una base de datos

    #Decirle a SQLAlchemy cual es la tabla
    __tablename__ = 'items'

    #Decirle a SQLAlchemy cuales son las columnas de la tabla
    id = db.Column(db.Integer, primary_key=True) #Campo de enteros, autoincremental
    name = db.Column(db.String(80)) #Campo de string, maximo 80 caracteres
    price = db.Column(db.Float(precision=2)) #Campo flotante, con 2 decimales

    store_id = db.Column(db.Integer, db.ForeignKey('stores.id'))    #DB relacionales, tabla.columna con la que va a hacer el match
    store = db.relationship('StoreModel')


    def __init__(self, name, price, store_id):
        self.name = name
        self.price = price
        self.store_id = store_id

    def json(self):
        return {
            'id':self.id,
            'name':self.name,
            'price':self.price,
            'store_id': self.store_id
        }

    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first() # query es un metodo de SQLAlchemy. se crea el siguiente query SELECT * FROM items WHERE name=name, limit 1, devuelve el primer resultado
        #Esta funcion retornara un objeto class ItemModel

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self) # Es una instancia que guarda los objetos antes de escribirlos en la DB (commit)
        db.session.commit() # Escribir en la base de datos lo que tenga session

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
