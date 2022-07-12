#Flask apps are built around requests and responses
    #Cuando vamos a un website en el navegador, eso es un request


from flask import Flask


app = Flask(__name__) #__name__ es una variable especial de python, le da un nombre especial a cada archivo


@app.route('/') #home page, por defecto esto tiene como method = ['GET']
def home():
    return "Hello, World!"


app.run(port=5000)
