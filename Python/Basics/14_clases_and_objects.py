# Referencias: Zenva - Learn python from making a game

# Parameter naming

class GameCharacter:

    # Fields
    # Declarar el valor de este parametro default, no requiere ser pasado en el constructor.
    speed = 5

    # Constructor
    # self se refiere a la clase, es requerida para todos los metodos de una clase
    def __init__(self, name, width, height, x_pos, y_pos):
        """Aqui se pondria el texto para mostrar en la ayuda"""
        self.name = name  # estamos asignando el valor name (argumento de la funcion __init__) a la variable name de la clase (self.name) la nomenclatura de estas variables es independiente
        self.width = width  # This is also a field
        self.height = height
        self.x_pos = x_pos
        self.y_pos = y_pos

    # Method
    def move(self, by_x_amount, by_y_amount):
        """Aqui se pondria el texto para mostrar en la ayuda"""
        self.x_pos += by_x_amount
        self.y_pos += by_y_amount


# Nueva instancia de clase GameCharacter
# Se crea el objeto de la clase GameCharacter, se deben pasar los valores requeridos por el constructor.
character_0 = GameCharacter("char_0", 50, 100, 100, 100)

print(character_0.name)
character_0.name = "Andres"
print(character_0.name)


print(character_0.x_pos, character_0.y_pos)
character_0.move(50, 100)
print(character_0.x_pos, character_0.y_pos)


# Check the class of an object
character_0.__class__


###############################
####     Magic Methods     ####

# Son funciones acompanadas por __ a cada lado, seran llamadas por python en alguna circunstancia que se requiera

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.cars = []

    # Len of a class it is used len(instance of Person)
    def __len__(self):
        return len(self.cars)

    # PAra devolver un item usando la notacion instance_Person[i]
    def __getitem__(self, i):
        return self.cars[i]

    # Si se definen el metodo getitem se puede usar for con la instancia
    # for car in instance_Person:

    # Se utiliza para dar informacion del objeto
    # User oriented description
    # se usa print(instance_Person)
    def __str__(self):
        return f"Person {self.name}, {self.age} years old"

    #  Code oriented description
    def __repr__(self):
        # Esta funcion se utiliza en el python debugger,
        # sirve para dar una pista de como reconstruir el objeto facilmente
        # Retorna un string que representa el objeto
        return f"<Person('{self.name}',{self.age})>"


# Cuando se crea un objeto, instancia de la clase, pyton llama automaticamente al constructor del objeto, la funcion __init__
bob = Person("Bob", 35)
print(bob)  # Cuando se intenta imprimir un objeto, python llamara la funcion __str__ e imprimir la informacion que esta devuelva. Se usa para imprimir un objeto de forma amigable con el usuario


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
