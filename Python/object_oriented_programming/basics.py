class GameCharacter:

    # Fields
    # Default params
    speed = 5

    # Constructor
    # self refers to the instance of the class. It is automatically passed as an
    # argument when the method is called with dot notation. i.e: instance.method 
    def __init__(self, name, width, height, x_pos, y_pos):
        """help text"""
        # self.name refers to the field name of the object.
        # name is the argument passed to the constructor.
        self.name = name
        self.width = width
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    # Method
    def move(self, by_x_amount, by_y_amount):
        """help text"""
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount


# New instance of the class, must pass the values required by constructor
character_0 = GameCharacter("char_0", 50, 100, 100, 100)

# Reassign values to object fields
character_0.name = "Andres"

# Call a method of the object
character_0.move(50, 100)

# Check the class of an object
character_0.__class__

# Class name as a string
character_0.__class__.__name__








################################################
####     Class Methods & Static Methods     ####


class ClassTest:
    def instance_method(self):
        # Una funcion normal de una clase se llama instance method, que como parametro recibe la instancia
        print(f"Called instance_method of {self}")
        # Estos metodos son los mas usados, se usan para operar o alterar los campos del objeto

    @classmethod
    def class_method(cls):
        # Es una funcion que recibe como parametro una clase.
        print(f"Called class_method of {cls}")
        # Se utilizan como una "Factory"

    @staticmethod
    def static_method():
        # Es una funcion que no recibe nada como parametro
        print("Called static_method.")
        # Se utiliza cuando una funcion pertenece a una clasee, y que por organizacion se debe escriir ahi.


test = ClassTest()
# Para llamar un instance_method se debe crear un objeto de la clase
test.instance_method()

ClassTest.class_method()  # Ejecutar la class_method

# Ejecutar el static_method, es simplemente una funcion que fue escrita dentro de una clase, pero al ejecutarla esta no tendra ninguna informacion de la clase u objeto.
ClassTest.static_method()


# Ejemplo:

class Book:
    TYPES = ("hardcover", "paperback")

    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<Book {self.name}, {self.book_type}, weighing {self.weight}g>"

    # Quiero asegurarme que como parametro de book_type solo se pueda usar "hardcover" o "paperback", para esto creo una classmethod
    @classmethod
    def hardcover(cls, name, page_weight):
        # cls representa la clase que se paso como argumento al momento de crear. en este caso representa Book
        return cls(name, cls.TYPES[0], page_weight+100)


# Crear un objeto usando todos los parametros
book = Book("Harry Potter", "comic_book", 1500)
print(book)

# Objeto creado con un class_method
book = Book.hardcover("Harry Potter", 1500)
print(book)


################################################
###   Subclass, Superclass and inheritance   ###


# Una subclase puede utilizar todos los field y methods de una Superclase

# GameCharacter es Superclase
# Subclase de GameCharacter:
class PlayerCharacter(GameCharacter):

    speed = 10

    # Siempre se debe tener un constructor/initializer
    # Se decide dejar como default los valores de width and height
    def __init__(self, name, x_pos, y_pos):
        # Esta funcion cogera los valores pasados en la cracion de la instalcio de la subclase y los pasara como argumentos a la funcion __init__ de la super clase.
        super().__init__(name, 100, 100, x_pos, y_pos)

    def move(self, by_y_amount):
        # Keyword "super()" sirve para llamar una funcion de la super clase, ej:
        # Se modifica la funcion move de la subclase player_character, haciendo que solo se pueda mover en la coordenada y:
        # Se llama a la funcion move de la superclase y se pasa by_x_amount = 0, solo se recibe como parametro by_y_amount
        super().move(0, by_y_amount)


# Nueva instancia de PlayerCharacter:
player_character = PlayerCharacter("P_character", 500, 500)

print(player_character.name)
print(player_character.x_pos)
print(player_character.y_pos)
player_character.move(77)
print(player_character.x_pos)
print(player_character.y_pos)


#############################
###   Class Composition   ###

# Componer clases que sean relacionadas unas con otras para reducir la complejidad del codigo

class BookShelf:
    def __init__(self, *books):
        self.books = books

    def __str__(self):
        return f"BookShelf with {len(self.books)} books."


class Book:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return f"Book {self.name}"


book = Book("Harry Potter")
book2 = Book("Python 101")
shelf = BookShelf(book, book2)

print(shelf)
print(shelf.books[0].name)


#####################################
###           @property           ###


class WorkingStudent:
    def __init__(self, name, school, salary) -> None:
        self.name = name
        self.school = school
        self.salary = salary

    @property
    def weekly_salary(self):
        return self.salary * 37.5

    @weekly_salary.setter
    def weekly_salary(self, value):
        # function to recalculate and set the weekly salary
        self.salary = value/37.5


# Ahora se puede utilizar de la siguiente manera
rolf = WorkingStudent("Rolf", "MIT", 15.50)
print(rolf.weekly_salary)
# Como se definio un setter:
rolf.weekly_salary = 3000 # Esto ejecutara la funcion definida como setter para ese atrubuto.




# Boolean to check attribute in object
name = "attribute"
hasattr(object, name)
