from geopy.geocoders import ArcGIS

import pandas


nom = ArcGIS()

location = nom.geocode("3995 23rd St, San francisco, CA")

location.latitude
location.longitud

df = pandas.read_json("supermarkets/supermarkets.json")

# modificar la columna address para que tenga el formato necesario para geocode
# con pandas no hay necesidad de iterar
df["Address"] = df["Address"] + ", " + df["City"] + ", " + df["State"] + ", " + df["Country"]

#metodo para aplicar algo a toda una columna
df["Coordinates"] = df["Address"].apply(nom.geocode)

df["Latitude"] = df["Coordinates"].apply(lambda x: x.latitude if x != None else None)
df["Longitude"] = df["Coordinates"].apply(lambda x: x.longitude if x != None else None)


