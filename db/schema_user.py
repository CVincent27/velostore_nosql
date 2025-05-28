from pymongo import MongoClient

# Connexion au serveur MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Récupération (ou création) d'une base de données
db = client["mangovelodatabase"]

# 2. Définition du schéma
schema = {
    "bsonType": "object",
    "required": ["username", "password"],
    "properties": {
        "user_type": {"bsonType": "string"},
        "username": {"bsonType": "string"},
        "status": {"bsonType": "string"},
        "mail": {"bsonType": "string"},
        "password": {"bsonType": "string"},
    }
}

validator = {"$jsonSchema": schema}

# 3. Création de la collection avec validation
db.create_collection(
    "user",
    validator=validator
)

print("Collection 'user' créée avec validation JSON Schema.")

