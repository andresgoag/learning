from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Creates local webserver and auto handles authentication.



# se debe crear un archivo yaml, y correr este archivo para crear un archivo que permita la autenticacion sin introducir la contrasena