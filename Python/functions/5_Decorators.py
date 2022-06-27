

#############################
###   Simple Decorators   ###

user = {"username": "jose", "access_level": "guest"}


def get_admin_password():
    return "1234"

def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function



get_admin_password = make_secure(get_admin_password) #Se reescribe la funcion get_admin_password, para que sea reemplazada por secure_function
print(get_admin_password())







###################################
###   @ Syntax for Decorators   ###

import functools


def make_secure(func):
    @functools.wraps(func) #Previene que internamente se cambie el nombre de la funcion a ser reemplazada, esto sirve para conservar la documentacion de la anterior funcion
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function


@make_secure # Este decorador hace esta linea de codigo: <get_admin_password = make_secure(get_admin_password)>
def get_admin_password():
    return "1234"

print(get_admin_password())




################################################
###   Decorating Functions with Parameters   ###

user = {"username": "jose", "access_level": "admin"}

def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs): #Se agrega los argumnetos *args & **kwargs para asegurarse que la funcion que reemplazara la original, reciba cantidad ilimitada de decoradores
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            return f"No admin permissions for {user['username']}"

    return secure_function



@make_secure
def get_password(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"

print(get_password("billing"))





######################################
###   Decorators with Parameters   ###

user = {"username": "jose", "access_level": "guest"}

def make_secure(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs): #Se agrega los argumnetos *args & **kwargs para asegurarse que la funcion que reemplazara la original, reciba cantidad ilimitada de decoradores
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permissions for {user['username']}"

        return secure_function
    return decorator




@make_secure("admin")
def get_admin_password():
    return "admin: 1234"


@make_secure("user")
def get_dashboard_password():
    return "user_password"


print(get_admin_password())
print(get_dashboard_password())


user = {"username": "jose", "access_level": "admin"}

print(get_admin_password())
print(get_dashboard_password())
