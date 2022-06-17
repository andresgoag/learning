from flask import Flask, render_template

app = Flask(__name__)


class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


@app.route("/expressions/")
def expressions():

    # interpolation
    color = "brown"
    animal_one = "fox"
    animal_two = "dog"

    # addition and substraction
    orange_amount = 10
    apple_amount = 20
    donate_amount = 15

    #string concatenation
    first_name = "Captain"
    last_name = "Marvel"

    # Se deben pasar todos los argumentos a la funcion, como keyword arguments

    kwargs = {
        "color": color,
        "animal_one": animal_one,
        "animal_two": animal_two,
        "orange_amount": orange_amount,
        "apple_amount": apple_amount,
        "donate_amount": donate_amount,
        "first_name": first_name,
        "last_name": last_name
    }

    return render_template("1_expressions.html", **kwargs)

@app.route("/data-structures/")
def data():
    movies = [
        "Pelicula 1",
        "Pelicula 2",
        "Pelicula 3"
    ]

    car = {
        "brand":"Tesla",
        "model":"Roadster",
        "year":"2020"
    }

    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")

    kwargs = {
        "movies":movies,
        "car":car,
        "moons": moons
    }

    return render_template("2_data_structures.html", **kwargs)

@app.route("/conditionals/")
def conditionals():
    company = "Microsoft"
    return render_template("3_conditionals_basics.html", company=company)

@app.route("/for-loop/")
def for_loop():
    planets = [
        "Mercurio",
        "Venus",
        "Tierra",
        "Marte",
        "Jupiter",
        "Saturn",
        "Uranus",
        "Neptune"
    ]

    plantas = {
        "tallo":"verde",
        "flor":"amarilla"
    }

    return render_template("4_for_loop.html", planets = planets, plantas=plantas)

@app.route("/loop-conditional")
def loop_conditional():

    user_os = {
        "Bob Smith": "Windows",
        "Anne Pun": "MacOS",
        "Adam Lee": "Linux",
        "Jose Salvatierra": "Windows"
    }

    return render_template("5_loops_and_conditionals.html", user_os=user_os)

if __name__ == "__main__":
    app.run(debug=True)