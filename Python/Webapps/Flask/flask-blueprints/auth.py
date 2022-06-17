from flask import Blueprint

auth = Blueprint('auth', __name__) # opcional url_prefix='/auth' si se quiere que todos los endpoints tengan esto como prefijo en la url

@auth.route('/login', methods=["GET", "POST"])
def login():
    return 'Pagina de login'