from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

# Connexion au serveur MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Récupération (ou création) d'une base de données
db = client["mangovelodatabase"]


# Création (ou accès) de la collection "products"
order_collection = db["Orders"]
user_collection = db["user"]



# Requête CRUD

def get_user_by_id(user_collection, user_id):
    return user_collection.find_one({"_id": ObjectId(user_id)})

print(get_user_by_id(user_collection, "683865363b2119ed7fac17c1"))

















