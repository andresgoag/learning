import eel

eel.init('web_files') #nombre de la carpeta que contiene los archivos web

@eel.expose
def hello(name):
    return {"message":f"Hello, {name}"}


eel.start('index.html', size=(1000, 600))
