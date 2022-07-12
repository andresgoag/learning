# Es un archivo creado para hacer JWT, tendra las funciones requeridas

from werkzeug.security import safe_str_cmp
from models.user import UserModel


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and safe_str_cmp(user.password,password): # es la version segura de comparar strings => user.password == password
        return user


def identity(payload): # Es una funcion unica de JWT, sirve para sacar el user id del JWT "Token"
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
