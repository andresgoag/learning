# Archivo para crear una clase Usuario
import sqlite3
from flask_restful import Resource, reqparse




class User:
    def __init__(self, _id, username, password):
        self.id = _id
        self.username = username
        self.password = password


    @classmethod
    def find_by_username(cls, username):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE username=?"
        result = cursor.execute(query, (username,))    #Crear tupla con un solo valor (username,)
        row = result.fetchone() #Devuelve solo el primer elemento de la seleccion, si no encontro nada devuelve None
        if row:
            user = cls(*row)   # Crear el user object, como row esta en el mismo orden que la funcion init, se puede pasar como un set de argumentos *row esto sera igual que row[0], row[1], row[2]
        else:
            user = None

        connection.close()
        return user


    @classmethod
    def find_by_id(cls, _id):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM users WHERE id=?"
        result = cursor.execute(query, (_id,))
        row = result.fetchone()
        if row:
            user = cls(*row)
        else:
            user = None

        connection.close()
        return user








class UserRegister(Resource): #Se crea una subclase de resource para agregar a REST-ful

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type = str,
                        required=True,
                        help='username cannot be blank')

    parser.add_argument('password',
                        type = str,
                        required=True,
                        help='password cannot be blank')


    def post(self):

        data = UserRegister.parser.parse_args()

        if User.find_by_username(data['username']):
            return {"message": "Username already in use"}

        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO users VALUES (NULL, ?, ?)" # Se pasa Null en el primer argumento ya que es el id y se incrementara automaticamente
        values = (data['username'], data['password'])

        cursor.execute(query, values)

        connection.commit()
        connection.close()

        return {'message':'User created successfully'}, 201
