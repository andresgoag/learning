import sqlite3

from flask_restful import Resource, reqparse
from flask_jwt import jwt_required






class Item(Resource):      # Se define un resource (Es una subclase de Resource importada de flask_restful)


    parser = reqparse.RequestParser() #Crear el parser con los argumento a utilizar dentro de las funciones
    parser.add_argument('price',
                        type = float,
                        required=True,
                        help='cannot be blank')




    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query,(name,))
        row = result.fetchone()
        connection.close()

        if row:
            return {'item':{'name':row[0], 'price':row[1]}}


    @classmethod
    def insert(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "INSERT INTO items VALUES (?,?)"
        cursor.execute(query, (item['name'], item['price']))
        connection.commit()
        connection.close()


    @classmethod
    def update(cls, item):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "UPDATE items SET price=? WHERE name=?"
        cursor.execute(query, (item['price'], item['name']))
        connection.commit()
        connection.close()







    @jwt_required()     # Se requerira la autenticacion para llamar este endpoint                               ########### JWT PASO 3 ############
    def get(self, name):         # Para llamar un endopoint que requiere auth, se agrega un header al request con Key "Authorization" y value "el token que devuelve el request /auth"
        item = self.find_by_name(name)

        if item:
            return item
        else:
            return {"message":"Item not found"}, 404


    def post(self, name):
        if self.find_by_name(name):
            return {'message':f'An item with name {name} already exists.'}, 400 # devolver HTTP status 400, bad request
        data = Item.parser.parse_args() #Llamar los datos del request con las condiciones definidas en el parser del Objeto Item
        item = {'name':name, 'price':data['price']}
        try:
            self.insert(item)
        except:
            {"message":"An error occurred inserting the item."}, 500 # Internal Server Error
        return item, 201 # Status 201 para decir que se creo en la base de datos


    def delete(sel, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM items WHERE name=?"
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()
        return {'message': f"item {name} deleted"}


    def put(self, name):
        data = Item.parser.parse_args() #Llamar los datos del request con las condiciones definidas en el parser del Objeto Item
        item = self.find_by_name(name)
        updated_item = {'name': name, 'price':data['price']}
        if item is None:
            try:
                self.insert(updated_item)
            except:
                return {"message":"An error occurred inserting the item."}, 500 # Internal Server Error
        else:
            try:
                self.update(updated_item)
            except:
                return {"message":"An error occurred inserting the item."}, 500 # Internal Server Error
        return updated_item





class ItemList(Resource):
    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "SELECT * FROM items"
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'name': row[0], 'price':row[1]})
        connection.close()
        return {'items':items}
