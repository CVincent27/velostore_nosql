from pymongo import MongoClient

# Connexion au serveur MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Récupération (ou création) d'une base de données
db = client["mangovelodatabase"]

# Création (ou accès) de la collection "products"
collection = db["bike_brand"]

# 2. Insérer plusieurs documents à la fois (INSERT MANY)
new_bike_brand = [
    {"brand": "Rockrider", "description": "Un vélo qui sert à grimper des montagnes", "price": 300,"destination":"VTT","img": "A21_blue_side_2.jpg"},
    {"brand": "B’Twin", "description": "Un vélo qui sert à grimper des montagnes", "price": 250,"destination":"route","img": "purist_orange_side.jpg"},
    {"brand": "Giant", "description": "Vélo de route léger et performant, parfait pour les longues distances", "price": 1200,"destination":"course","img": "velo-ville.jpg"},
    {"brand": "Cannondale", "description": "Vélo tout-terrain robuste conçu pour les pistes accidentées", "price": 850,"destination":"BMX","img": "velo-ville.jpg"},
    {"brand": "Electra", "description": "Vélo cruiser au design rétro pour des balades détendues", "price": 400,"destination":"course","img": "velo-de-route-pinarello.png"}
]
result_many = collection.insert_many(new_bike_brand)
print("IDs insérés pour les autres produits :", result_many.inserted_ids)

# GET BIKE BY BRAND
def get_bike_by_brand(brand: int) -> dict:
    one_product = collection.find_one({"brand": brand})
    return print("Un produit en Electronics :", one_product)

get_bike_by_brand("Rockrider")
