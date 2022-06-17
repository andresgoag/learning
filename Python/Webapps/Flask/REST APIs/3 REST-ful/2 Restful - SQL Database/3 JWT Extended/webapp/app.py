import os

from flask import Flask, jsonify
from flask_restful import Api
from flask_jwt_extended import JWTManager

from resources.user import UserRegister, User, UserLogin, UserLogout, TokenRefresh
from resources.item import Item, ItemList
from resources.store import Store, StoreList
from db import db
from blacklist import BLACKLIST



app = Flask(__name__)      # Se define la aplicacion de flask
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///data.db')   # Definir la ubicacion de la base de datos, si existe una variable de ambiente DATABASE_URL se conectara a esa, si no existe ejecutara la segunda opcion que es sqlite, sirve para desarrollar localmente
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False   # Para ahorrar recursos
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['JWT_BLACKLIST_ENABLED'] = True
app.config['JWT_BLACKLIST_TOKEN_CHECKS'] = ['access', 'refresh']

app.secret_key = 'andres'   # tambien se puede hacer con app.config['JWT_SECRET_KEY'], esta es la semilla que se usa para encriptar el jwt token
api = Api(app)      # Va a manejar la API


@app.before_first_request
def create_tables():
    db.create_all() # Crea todos los archivos necesarios asociados al objeto db, si no existen



jwt = JWTManager(app) # No crea el /auth endpoint



# JWT Claims
@jwt.user_claims_loader
def add_claims_to_jwt(identity):
    if identity == 1: # En lugar de hardcode, se debe buscar este valor en la base de datos
        return {'is_admin':True}
    return {'is_admin':False}


# Customizar el mensaje que se envia cuando se usa un token expirado
@jwt.expired_token_loader
def expired_token_callback():
    return jsonify({
        'description':'The token has expired.',
        'error':'token_expired'
    }), 401

# Cuando el token enviado no es JWT
@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({
        'description':'Signature verification failed.',
        'error': 'invalid_token'
    }), 401

# Cuando no se envia ningun JWT
@jwt.unauthorized_loader
def missing_token_callback(error):
    return jsonify({
        'description':'Request does not contain an access token.',
        'error': 'authorization_required'
    }), 401

# Cuando se envia un token que no es fresh, a un endpoint que requiere un fresh
@jwt.needs_fresh_token_loader
def token_not_fresh_callback():
    return jsonify({
        'description':'The token is not fresh',
        'error': 'fresh_token_required'
    }), 401

# Mensaje cuando se revoca un toke. por ejemplo cuando alguien se desloggea, el token se revoca y este mensaje se imprime si se intenta usar ese mismo token
@jwt.revoked_token_loader
def revoked_token_callback():
    return jsonify({
        'description':'The token has been revoked',
        'error': 'token_revoked'
    }), 401


# Blacklist loader
@jwt.token_in_blacklist_loader
def check_if_token_in_blacklist(decrypted_token):
    return decrypted_token['jti'] in BLACKLIST # Devuelve verdadero si esta en la blacklist


api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')
api.add_resource(Store, '/store/<string:name>')
api.add_resource(StoreList, '/stores')
api.add_resource(User, '/user/<int:user_id>')
api.add_resource(UserLogin, '/login')
api.add_resource(UserLogout, '/logout')
api.add_resource(TokenRefresh, '/refresh')



if __name__ == '__main__': #En caso de haber importado app.py en otro archivo, esto evitara que se inicie la aplicacion desde otro archivo
    db.init_app(app)
    app.run(port=5000, debug = True) # debug es para activar que flask muestre un html con el error
