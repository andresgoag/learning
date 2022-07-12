from flask import Flask, render_template, redirect, request



from flask_login import LoginManager, UserMixin, login_user, login_required

usuarios = [
    {'user': 'andres', 'pass': '1234'},
    {'user': 'david', 'pass': '5678'},
    {'user': 'brian', 'pass': '1357'}
]



class Usuario(UserMixin):

    def __init__(self, user, password):
        self.id = user
        self.password = password

    @classmethod
    def get_user(cls, user):
        global usuarios
        user_obj = None
        for usuario in usuarios:
            if usuario['user'] == user:
                user_obj = cls(usuario['user'], usuario['pass'])
                break
        return user_obj







app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"
login_manager.login_message = "Por favor inicie sesion"
login_manager.login_message_category = "info"

app.secret_key = "appLogin"

@login_manager.user_loader
def load_user(user):
    return Usuario.get_user(user)


@app.route('/')
def index():
    return redirect('/login')


@app.route('/login', methods=["GET", "POST"])
def login():

    if request.method == "POST":
        input_usuario = request.form.get('usuario')
        input_password = request.form.get('password')

        for usuario in usuarios:
            if usuario['user'] == input_usuario:
                password = usuario['pass']
                break
        if password == input_password:

            user = Usuario(input_usuario, input_password)

            login_user(user)

        return redirect('/private')

    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')


@app.route('/private')
@login_required
def private():
    return render_template('private.html')
