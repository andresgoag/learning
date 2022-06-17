from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)      # Se define la aplicacion de flask
app.secret_key = 'andres'   # Definir la secret key de la aplicacion                                           ########### JWT PASO 1 ############
api = Api(app)      # Va a manejar la API



jwt = JWT(app, authenticate, identity)  # Importar las funciones del archivo security.py                        ########### JWT PASO 2 ############
# Este paso crea un nuevo endpoint /auth, cuando se llama este endpoint, se debe enviar un username y un password, y se los manda a la funcion authenticate y valida si si es el usuario y crea el JWToken
# El JWT es enviado como "access_token" en JSON



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')


if __name__ == '__main__': #En caso de haber importado app.py en otro archivo, esto evitara que se inicie la aplicacion desde otro archivo
    app.run(port=5000, debug = True) # debug es para activar que flask muestre un html con el error
