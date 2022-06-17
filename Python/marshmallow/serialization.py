# 1. Importar libreria
from marshmallow import Schema, fields


# 2. Crear un schema
class BookSchema(Schema):

    """
    # Tell marshmallow if some field is only for receive (load) or return (dump)
    class Meta:
        load_only = ("title",)
        dump_only = ("author"),
    """
    
    # 3. Definir los campos que tendra
    title = fields.Str()
    author = fields.Str()
    



# 3. Crear una clase con la que el programa va a trabajar
class Book:

    def __init__(self, title, author, description):
        self.title = title
        self.author = author
        self.description = description




# instancia de Book
book = Book("Clean code", "Bob Martin", "A book about writing cleaner code")
# instancia de BookSchema
book_schema = BookSchema()
# se pasa la instancia de Book a BookSchema y el metodo dump retorna un diccionario con las propiedades definidas en BookSchema
book_dict = book_schema.dump(book)

print(book_dict)
