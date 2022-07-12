from flask import Flask, render_template, request , flash, redirect, url_for, session
import bcrypt                                                                  # libreria para codificar las contrasenas

from database import db
from models.user import UserModel



app = Flask(__name__)

app.secret_key = "appLogin"                                                     # Crear llave secreta

# Configuracion de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False



salt = bcrypt.gensalt()


@app.before_first_request
def create_tables():
    db.create_all()                                                             # Crea todos los archivos necesarios asociados al objeto db, si no existen


@app.route('/')
def main():
    return render_template('index.html')





@app.route('/signup', methods=["POST", "GET"])
def signup():
    if 'user' in session:
        return redirect(url_for('aplicativo'))
    else:
        if request.method == "POST":
            input_name = request.form['name']
            input_email = request.form['email']
            input_password = request.form['password'].encode("utf-8")
            password_encrypted = bcrypt.hashpw(input_password, salt)

            if UserModel.find_by_email(input_email):
                flash("El email se encuentra registrado", "info")
                return render_template('signup.html')

            else:
                user = UserModel(input_name, input_email, password_encrypted)
                user.save()
                session['user'] = user.name
                return redirect(url_for('aplicativo'))

        else:
            return render_template('signup.html')






@app.route('/login', methods=["POST", "GET"])
def login():
    if 'user' in session:
        return redirect(url_for('aplicativo'))
    else:
        if request.method == "POST":
            input_email = request.form['email']
            input_password = request.form['password'].encode('utf-8')

            user = UserModel.find_by_email(input_email)

            if user:
                if bcrypt.checkpw(input_password, user.password):
                    session['user'] = user.name
                    return redirect(url_for('aplicativo'))
                else:
                    flash("Email o contraseña incorrecta", "info")
                    return render_template('login.html')

            else:
                flash("Email o contraseña incorrecta", "info")
                return render_template('login.html')

        else:
            return render_template('login.html')





@app.route('/aplicativo')
def aplicativo():
    if 'user' in session:
        return render_template('aplicativo.html')
    else:
        return redirect(url_for('login'))




@app.route("/logout")
def logout():
    session.pop('user', None)
    return redirect(url_for("login"))



if __name__ == '__main__':
    db.init_app(app)                                                            # Relacionar el objeto db con la aplicacion
    app.run(debug=True)
