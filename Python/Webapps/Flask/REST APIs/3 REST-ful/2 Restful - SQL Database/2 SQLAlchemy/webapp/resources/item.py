from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel






class Item(Resource):      # Se define un resource (Es una subclase de Resource importada de flask_restful)


    parser = reqparse.RequestParser() #Crear el parser con los argumento a utilizar dentro de las funciones
    parser.add_argument('price',
                        type = float,
                        required=True,
                        help='cannot be blank')

    parser.add_argument('store_id',
                        type = int,
                        required=True,
                        help='Every items needs a store id')

    @jwt_required()     # Se requerira la autenticacion para llamar este endpoint                               ########### JWT PASO 3 ############
    def get(self, name):         # Para llamar un endopoint que requiere auth, se agrega un header al request con Key "Authorization" y value "el token que devuelve el request /auth"
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        else:
            return {"message":"Item not found"}, 404


    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message':f'An item with name {name} already exists.'}, 400 # devolver HTTP status 400, bad request
        data = Item.parser.parse_args() #Llamar los datos del request con las condiciones definidas en el parser del Objeto Item
        item = ItemModel(name, **data)
        try:
            item.save_to_db()
        except:
            {"message":"An error occurred inserting the item."}, 500 # Internal Server Error
        return item.json(), 201 # Status 201 para decir que se creo en la base de datos


    def delete(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            item.delete_from_db()

        return {"message":f"Item {item.name} deleted"}


    def put(self, name):
        data = Item.parser.parse_args() #Llamar los datos del request con las condiciones definidas en el parser del Objeto Item
        item = ItemModel.find_by_name(name)

        if item is None:
            item = ItemModel(name, **data)
        else:
            item.price = data['price']

        item.save_to_db()

        return item.json()





class ItemList(Resource):
    def get(self):
        return {'items': [item.json() for item in ItemModel.find_all()]}
