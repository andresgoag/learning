# 1. Importar libreria
from marshmallow import Schema, fields


# 2. Crear un schema
class BookSchema(Schema):
    # 3. Definir los campos que tendra y cuales son obligatorios
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    description = fields.Str()

class Book:

    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description


incoming_book_data = {
    "title": "Clean code",
    "author": "Bob Martin",
    "description": "A book about writing cleaner code"
}

# La idea es pasar incoming_book_data a BookSchema y crear un objeto libro

book_schema = BookSchema()

# Si la informacion no tiene algun campo requerido se genera un error
# si se imprime book es un diccionario
book = book_schema.load(incoming_book_data)
# crear un objeto deestructurando el json en el init
book_object = Book(**book)









# Forma no recomendada: INCLUDE, EXCLUDE:
# Es mejor saber que data se requiere

from marshmallow import Schema, fields, INCLUDE, EXCLUDE


class BookSchema(Schema):
    title = fields.Str()
    author = fields.Str()


incoming_book_data = {
    "title": "Clean code",
    "author": "Bob Martin",
    "description": "A book about writing cleaner code"
}

# La idea es pasar incoming_book_data a BookSchema y crear un objeto libro

book_schema = BookSchema(unknown=EXCLUDE) # no permite elementos desconocidos
book_schema = BookSchema(unknown=INCLUDE) # permite elementos desconocidos

book = book_schema.load(incoming_book_data)