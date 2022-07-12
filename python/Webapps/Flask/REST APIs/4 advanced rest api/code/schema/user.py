from ma import ma
from models.user import UserModel

class UserSchema(ma.SQLAlchemyAutoSchema):

    # Tell marshmallow that password is only for receive it, not return it (dump)
    class Meta:
        model = UserModel
        load_only = ("password",)
        dump_only = ("id", "activated")
        load_instance = True