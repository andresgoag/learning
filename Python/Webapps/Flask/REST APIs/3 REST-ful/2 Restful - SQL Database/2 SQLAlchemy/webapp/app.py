import os

from flask import Flask
from flask_restful import Api
from flask_jwt import JWT

from security import authenticate, identity
from resources.user import UserRegister, User
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db



app = Flask(__name__)      # Se define la aplicacion de flask
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')   # Definir la ubicacion de la base de datos, si existe una variable de ambiente DATABASE_URL se conectara a esa, si no existe ejecutara la segunda opcion que es sqlite, sirve para desarrollar localmente
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # Para ahorrar recursos
app.config['PROPAGATE_EXCEPTIONS'] = True

app.secret_key = 'andres'   # Definir la secret key de la aplicacion                                           ########### JWT PASO 1 ############
api = Api(app)      # Va a manejar la API


@app.before_first_request
def create_tables():
    db.create_all() # Crea todos los archivos necesarios asociados al objeto db, si no existen



jwt = JWT(app, authenticate, identity)  # Importar las funciones del archivo security.py                        ########### JWT PASO 2 ############
# Este paso crea un nuevo endpoint /auth, cuando se llama este endpoint, se debe enviar un username y un password, y se los manda a la funcion authenticate y valida si si es el usuario y crea el JWToken
# El JWT es enviado como "access_token" en JSON



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User, '/user/<int:user_id>')



if __name__ == '__main__': #En caso de haber importado app.py en otro archivo, esto evitara que se inicie la aplicacion desde otro archivo
    db.init_app(app)
    app.run(port=5000, debug = True) # debug es para activar que flask muestre un html con el error
