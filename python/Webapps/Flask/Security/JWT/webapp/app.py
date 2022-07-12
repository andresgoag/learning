from flask import Flask, request
from flask_restful import Resource, Api,reqparse
from flask_jwt import JWT, jwt_required

from security import authenticate, identity


app = Flask(__name__)      # Se define la aplicacion de flask
app.secret_key = 'andres'   # Definir la secret key de la aplicacion                                           ########### JWT PASO 1 ############
api = Api(app)      # Va a manejar la API



jwt = JWT(app, authenticate, identity)  # Importar las funciones del archivo security.py                        ########### JWT PASO 2 ############
# Este paso crea un nuevo endpoint /auth, cuando se llama este endpoint, se debe enviar un username y un password, y se los manda a la funcion authenticate y valida si si es el usuario y crea el JWToken
# El JWT es enviado como "access_token" en JSON


items = []  # lista para guardar los items


class Item(Resource):      # Se define un resource (Es una subclase de Resource importada de flask_restful)

    parser = reqparse.RequestParser() #Crear el parser con los argumento a utilizar dentro de las funciones
    parser.add_argument('price',
                        type = float,
                        required=True,
                        help='cannot be blank')


    @jwt_required()     # Se requerira la autenticacion para llamar este endpoint                               ########### JWT PASO 3 ############
    def get(self, name):         # Para llamar un endopoint que requiere auth, se agrega un header al request con Key "Authorization" y value "el token que devuelve el request /auth"
        '''
        for item in items:
            if item['name'] == name:
                return item             # Se pueden devolver diccionarios en flask_restful porque el los convierte a json
        return {'item': None}, 404      # Si no se encuentra el item, se devuelve una representacion valida de json con None y se devuelve el codigo 404 Not Found
        '''
        #Expresion equivalente al "for", se va a iterar a traves de items, y se compara el value del key name de cada elemento con el name recibido en la URL:

        item = next(filter(lambda x: x['name'] == name, items), None) # None: Si no encuentra un resultado, devolvera None
        # Se poodria usar tambien list(filter(lambda x: x['name'] == name, items)) ----->  El list, se aplica al objeto filter para obtener una lista de todas las coincidencias de la funcion
        return {'item': item}, 200 if item else 404 # Retornar HTTP status, 200 si fue exitoso o 404 si no se encontro nada



    def post(self, name):
        if next(filter(lambda x: x['name'] == name, items), None) is not None:
            return {'message':f'An item with name {name} already exists.'}, 400 # devolver HTTP status 400, bad request

        data = Item.parser.parse_args() #Llamar los datos del request con las condiciones definidas en el parser del Objeto Item

        item = {'name':name, 'price':data['price']}
        items.append(item)
        return item, 201 # Status 201 para decir que se creo en la base de datos


    def delete(sel, name):
        global items
        items = list(filter(lambda x: x['name'] != name, items))  # Reemplazar la lista original con una lista filtrada en la cual se quito el item a borrar
        return {'message': f"item {name} deleted"}


    def put(self, name):


        ''' Asi se haria si solo este metodo fuera a tener el parser, pero para reutilizar, se lleva el codigo al Objeto para usarlo al interior de los metodos
        #Con este parser, se asegura que el request trae la informacion que el endpoint de la api necesita
        parser = reqparse.RequestParser()
        parser.add_argument('price',
                            type = float,
                            required=True,
                            help='cannot be blank') #help es el mensaje que devolvera la api si el request no cuenta con esta informacion

        data = parser.parse_args()  # Solo pasara los argumentos que cumplan la funcion descrita en las dos lineas anteriores, como solo se definio price, es el unico que entrara, el resto de informacion que traiga el JSON sera borrada.
        '''

        data = Item.parser.parse_args() #Llamar los datos del request con las condiciones definidas en el parser del Objeto Item

        item = next(filter(lambda x: x['name'] == name, items), None)
        if item is None:
            item = {'name': name, 'price':data['price']}
            items.append(item)
        else:
            item.update(data)
        return item





class ItemList(Resource):
    def get(self):
        return {'items':items}



api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')



app.run(port=5000, debug = True) # debug es para activar que flask muestre un html con el error
