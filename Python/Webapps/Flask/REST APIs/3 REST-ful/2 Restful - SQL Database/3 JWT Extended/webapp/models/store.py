from db import db


class StoreModel(db.Model): #Se extiende la clase para indicarle a SQLAlchemy que sera mapeada a una base de datos

    #Decirle a SQLAlchemy cual es la tabla
    __tablename__ = 'stores'

    #Decirle a SQLAlchemy cuales son las columnas de la tabla
    id = db.Column(db.Integer, primary_key=True) #Campo de enteros, autoincremental
    name = db.Column(db.String(80)) #Campo de string, maximo 80 caracteres


    items = db.relationship('ItemModel', lazy='dynamic') #Query builder para devolver una lista de todos los items, de una tienda cuando sea llamado


    def __init__(self, name):
        self.name = name

    def json(self):
        return {
            'id':self.id,
            'name':self.name,
            'items':[item.json() for item in self.items.all()]  #se le pone el .all() al query builder para construir la lista de items
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
