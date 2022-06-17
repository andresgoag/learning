from bson.json_util import dumps, ObjectId



db.carreras.insert_one({}).inserted_id # retorna el id insertado


dumps(db.carreras.find_one({'_id':ObjectId(carrera_id)})) # dumps es una funcion que convierte a json.



db.carreras.update_one(
    {
        '_id':ObjectId(carrera['_id'])
    },
    {
        '$set': {
            'nombre': carrera['nombre'], 
            'descripcion':carrera['carrera']
        }
    }
).modified_count # este es para retornar cuantas se modificaron



db.cursos.delete_one({'_id': ObjectId(curso_id)}).deleted_count