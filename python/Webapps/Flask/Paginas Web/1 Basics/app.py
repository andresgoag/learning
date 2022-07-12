# Referencias: Build 10 Real World Applications(Udemy)

from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html") #el html debe estar guardado en una carpeta llamada templates


@app.route('/about/')
def about():
    return render_template("about.html")



if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0')
