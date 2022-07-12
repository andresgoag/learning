from pymongo import MongoClient

client = MongoClient("mongodb+srv://admin:1234@learn-microblog.ipcgl.mongodb.net/test")  # connection string

db = client.microblog       # acceder a la base de datos microblog

db.entries                  # acceder a la collection entries

db.entries.find({})         # buscar todos los elementos en entries

db.entries.insert({         # insertar un documento nuevo a la colleccion entries. el documento es un diccionario de python
    "content": entry_content,
    "date":formatted_date
})