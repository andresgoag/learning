# Es un archivo creado para hacer JWT, tendra las funciones requeridas

from werkzeug.security import safe_str_cmp
from user import User


# Users table - Ejemplo de Database
users = [
    User(1, 'andres', '1234')
]



username_mapping = {u.username:u for u in users}
userid_mapping = {u.id:u for u in users}

''' El dictionary comprehension de arriba esta haciendo lo mismo que este codigo:

userid_mapping = { 1: {
    'id': 1,
    'name': 'Andres',
    'password':'1234'
    }
}
'''




def authenticate(username, password):
    user = username_mapping.get(username, None) # username_mapping.get(username) es lo mismo que username_mapping['username'], la ventaja es que se puede devolver None si no se encuentra nada
    if user and safe_str_cmp(user.password,password): # es la version segura de comparar strings => user.password == password
        return user


def identity(payload): # Es una funcion unica de JWT, sirve para sacar el user id del JWT "Token"
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
