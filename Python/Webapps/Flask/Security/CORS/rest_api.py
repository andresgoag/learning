from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)

api = Api(app)
#CORS(app) # Permite el acceso desde cualquier URL a cualquier endpoint

cors = CORS(app, resources={r"/usuarios": {"origins": "http://localhost:5000"}})


usuarios = ["Andres, Juan, Pablo"]
barrios = ["Porvenir", "Llanogrande", "Cartagena"]


class listaUsuarios(Resource):
    def get(self):
        return {'usuarios': usuarios}

class listaCasas(Resource):
    def get(self):
        return {'barrios': barrios}

class Usuario(Resource):
    def post(self):
        data = request.get_json()
        usuarios.append(data["nombre1"])
        return{"message":f"usuario {data['nombre1']} anadido exitosamente"}




api.add_resource(listaUsuarios, '/usuarios')
api.add_resource(Usuario, '/usuario')
api.add_resource(listaCasas, '/casas')





if __name__ == "__main__":
    app.run(port=4999)
