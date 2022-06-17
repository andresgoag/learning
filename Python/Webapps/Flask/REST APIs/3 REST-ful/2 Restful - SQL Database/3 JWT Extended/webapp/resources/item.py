from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_claims, jwt_optional, get_jwt_identity, fresh_jwt_required 
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

    @jwt_required     #con jwt_extended ya no se requiere los () para este decorator
    def get(self, name):         # Para llamar un endopoint que requiere auth, se agrega un header al request con Key "Authorization" y value "el token que devuelve el request /auth"
        item = ItemModel.find_by_name(name)

        if item:
            return item.json()
        else:
            return {"message":"Item not found"}, 404

    @fresh_jwt_required #Requerir un fresh token
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

    @jwt_required
    def delete(sel, name):
        claims = get_jwt_claims()
        if not claims['is_admin']:
            return {'message':'Admin privilege required'}, 401

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
    @jwt_optional
    def get(self):
        user_id = get_jwt_identity() # Devuelve lo que se haya puesto como identidad en el JWT
        items = [item.json() for item in ItemModel.find_all()]
        if user_id:
            return {'items':items}, 200
        return {
            'items': [item['name'] for item in items],
            'message':'More data available if logged.'
            }, 200
