from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)      # Se define la aplicacion de flask

api = Api(app)      # Va a manejar la API


class Student(Resource):      # Se define un resource (Es una subclase de Resource importada de flask_restful)
    def get(self, name):                # Se habilita el resource para ser accedido con un GET Request, se debe generar una funcion para cada tipo de request que se quiera recibir
        return {'student': name}



api.add_resource(Student, '/student/<string:name>')       # Decirle a la API que el resource Student es accesible, sera llamada por ejemplo: http://127.0.0.1:5000/student/Rolf


app.run()
