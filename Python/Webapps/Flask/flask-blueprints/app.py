from flask import Flask
from auth import auth

app = Flask(__name__)

app.register_blueprint(auth)

@app.route('/')
def index():
    return 'Pagina registrada directamente en app.py'