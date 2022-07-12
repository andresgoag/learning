# Una sesion es para guardar informacion temporal en el servidor, ej: cuando se inicia sesion en facebook se crea una sesion con el nombre de usuario y contrasena para recordar que esta loggeado


from flask import Flask, redirect, url_for, render_template, request, session

from datetime import timedelta




app = Flask(__name__)

app.permanent_session_lifetime = timedelta(days=5) # Guardar los datos de session un tiempo, para que al tiempo uno vuelve a la pagina y siga loggeado

app.secret_key = "hola" # Se requiere para encriptar y decriptar

@app.route('/')
def home():
    return render_template("index.html")


@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True # declarar que la sesion sera permanente y durara lo que se haya especificado al iniciar
        user = request.form["nm"]
        session["user"] = user    # Session es un diccionario, por lo tanto para agregar informacion debemos especificar el key al cual le vamos a asignar el valor
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for('user'))
        return render_template("login.html")



@app.route('/user')
def user():
    if "user" in session: # Verificar que session tenga el key user
        user = session["user"]
        return f"<h1>{user}</h1>"
    else:
        return redirect(url_for("login"))




@app.route("logout")
def logout():
    session.pop("user", None) # Borrar el key user de session
    return redirect(url_for("login"))



if __name__ == "__main__":
    app.run(debug=True)














from flask import flash

flash("you have been logged out", "info")  # se pasa el mensaje y la categoria como argumentos, la categoria es opcional


en HTML
{% with messages = get_flashed_messages() %}
    {% if messages %}
        {% for msg in messages %}
            <p>{{msg}}</p>
        {% endfor %}
    {% endif %}
{% endwith %}







Referencia:





password = #tomar los datos enviados desde la web
password_encode = password.encode("utf-8")
password_encryptado = bcrypt.hashpw(password_encode, semilla) # Encriptar con la semilla, esta es la que se guarda en la base de datos


# Para compara los passwords con bcrypt

#operacion al password guardado en la base de datos
password_base_de_datos_encode = usuario[1].encode()   #usuario[1] es la representacion de obtener el valor de la base de datos y hay que encode para poder comparar

# operacion al password ingresado por el usuario
password = request.form['name del campo html de password']
password_encode = password.encode('utf-8')
if bcrypt.checkpw(password_encode, password_base_de_datos_encode):

    session['nombre'] = usuario




return redirect(url_for('inicio'))      # para devolver en una funcion de flask para que se vaya a otra pagina
