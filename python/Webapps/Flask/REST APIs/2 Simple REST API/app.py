#Online Store
from flask import Flask, jsonify, request, render_template


app = Flask(__name__)

stores = [ #Posteriormente esta informacion sera utilizada como Object Oriented Programming y guardada en bases de datos
    {
        "name": "My Wonderful Store",
        "items": [
            {
                "name":"My Item",
                "price": 15.99
            },
            {
                "name":"Cuchillo",
                "price": 7.49
            }
        ]
    }
]

@app.route('/')
def home():
    return render_template('index.html') #NOTA: una rest API no debe renderizar html, la pagina web y la rest API deben ser servicios separados



#POST - used to receive data
#GET - used to send data back only

#Endpoints
# POST /store data: {name:}                         # Create a store with a given name
@app.route('/store', methods=['POST']) #Se define que solo puede ser accesible por un post request
def create_store():
    request_data = request.get_json() #Convierte el json que envia el navegador en un diccionario de python
    new_store = {'name':request_data['name'], 'items':[]}
    stores.append(new_store)
    return jsonify(new_store)




# GET /store/<string:name>                          # Get a store for a given name, and return data about it
@app.route('/store/<string:name>')  #<string:name> es una sintaxis especial de flask, sirve para enviar un parametro a la funcion asociada. el argumento de la funcion tiene que coincidir con name. Ej: http://127.0.0.1:5000/store/some_name -> some_name sera pasado como argumento a la funcion.
def get_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message': 'store not found'})




# GET /store                                        # Return a list of all stores
@app.route('/store')
def get_stores():
    return jsonify({'stores':stores}) #Convierte un diccionario de python en json, requiere ser importado
    #Esta funcion devuelve un texto en formato JSON, javascript debe jugar con este texto para obtener la informacion




# POST /store/<string:name>/item  {name:price}      # Create an item inside a specific store
@app.route('/store/<string:name>/item', methods=['POST'])
def create_item_in_store(name):
    request_data = request.get_json()
    for store in stores:
        if store['name'] == name:
            new_item = {'name': request_data['name'], 'price': request_data['price']}
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})






# GET /store/<string:name>/item                     # Get all the items in a specific store
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items':store['items']})
    return jsonify({'message':'store not found'})




app.run(port=5000)
