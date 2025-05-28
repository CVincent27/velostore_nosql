from pymongo import MongoClient

# Connexion au serveur MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Récupération (ou création) d'une base de données
db = client["mangovelodatabase"]


# Création (ou accès) de la collection "products"
collection = db["user3"]

# 2. Insérer plusieurs documents à la fois (INSERT MANY)
new_user = [
    {"user_type": "Utilisateur", "username": "jules100", "status": "actif", "mail": "jules@gmail.com","password": "vl4e5swer5@"}
]
result_many = collection.insert_many(new_user)
print("IDs insérés pour les autres produits :", result_many.inserted_ids)

# # GET BIKE BY BRAND
# def get_bike_by_brand(brand: int) -> dict:
#     one_product = collection.find_one({"brand": brand})
#     return print("Un produit en Electronics :", one_product)

# get_bike_by_brand("Rockrider")
