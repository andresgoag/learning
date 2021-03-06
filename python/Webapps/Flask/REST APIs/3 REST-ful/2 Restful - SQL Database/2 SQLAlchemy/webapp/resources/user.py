# Archivo para crear una clase Usuario
from flask_restful import Resource, reqparse
from models.user import UserModel



class UserRegister(Resource): #Se crea una subclase de resource para agregar a REST-ful

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type = str,
                        required=True,
                        help='username cannot be blank')

    parser.add_argument('password',
                        type = str,
                        required=True,
                        help='password cannot be blank')


    def post(self):

        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "Username already in use"}

        user = UserModel(**data)
        user.save_to_db()

        return {'message':'User created successfully'}, 201


class User(Resource):
    @classmethod
    def get(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message':'User not found'}, 404
        return user.json()

    @classmethod
    def delete(cls, user_id):
        user = UserModel.find_by_id(user_id)
        if not user:
            return {'message':'User not found'}, 404
        user.delete_from_db()
        return {'message':'User deleted.'}, 200
