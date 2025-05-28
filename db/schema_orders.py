from pymongo import MongoClient

# Connexion au serveur MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Récupération (ou création) d'une base de données
db = client["mangovelodatabase"]

# 2. Définition du schéma
schema = {
    "bsonType": "object",
    "required": ["id_order", "id_user", "user", "bikes", "Date", "Total_price", "Status"],
    "properties": {
        "id_user": {"bsonType": "string"},
        "user": {
            "bsonType": "object",
            "required": ["id_user", "Username", "Mail"],
            "properties": {
                "id_user": {"bsonType": "string"},
                "Username": {"bsonType": "string"},
                "Mail": {"bsonType": "string"}
            }
        },
        "bikes": {
            "bsonType": "array",
            "items": {
                "bsonType": "object",
                "required": ["brand", "config", "nb_unit", "price"],
                "properties": {
                    "brand": {
                        "bsonType": "object",
                        "required": ["Description", "Price"],
                        "properties": {
                            "Description": {"bsonType": "string"},
                            "Price": {"bsonType": "int"}
                        }
                    },
                    "config": {
                        "bsonType": "object",
                        "required": ["Size", "Color"],
                        "properties": {
                            "Size": {"bsonType": "string"},
                            "Color": {"bsonType": "string"}
                        }
                    },
                    "nb_unit": {"bsonType": "int"},
                    "price": {"bsonType": "int"}
                }
            }
        },

        "Date": {"bsonType": "date"},
        "Total_price": {"bsonType": "int"},
        "Status": {"bsonType": "string"}
    }
}

validator = {"$jsonSchema": schema}

# 3. Création de la collection avec validation
db.create_collection(
    "Orders",
    validator=validator
)

print("Collection 'orders' créée avec validation JSON Schema.")