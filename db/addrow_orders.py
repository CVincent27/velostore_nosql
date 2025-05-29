from pymongo import MongoClient
from bson import ObjectId
from datetime import datetime

# Connexion au serveur MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Récupération (ou création) d'une base de données
db = client["mangovelodatabase"]


# Création (ou accès) de la collection "products"
collection = db["Orders"]

# 2. Insérer plusieurs documents à la fois (INSERT MANY)
sample_orders = [
    {
        "_id": ObjectId(),
        "user": {
            "id_user": ObjectId("665612a5cbe5f12c8a4f1234"),
            "Username": "jules100",
            "Mail": "jules@gmail.com"
        },
        "bikes": [
            {
                "id_bike": ObjectId("665613f1cbe5f12c8a4f1235"),
                "brand": {
                    "brand": "Giant",
                    "Description": "Mountain Bike with suspension",
                    "Price": 500
                },
                "config": {
                    "Size": "M",
                    "Color": "Red"
                },
                "nb_unit": 1,
                "price": 500
            }
        ],
        "Date": datetime(2025, 5, 1),
        "Total_price": 500,
        "Status": "payé"
    },
    {
        "_id": ObjectId(),
        "user": {
            "id_user": ObjectId("665612a5cbe5f12c8a4f1236"),
            "Username": "emma200",
            "Mail": "emma200@gmail.com"
        },
        "bikes": [
            {
                "id_bike": ObjectId("665613f1cbe5f12c8a4f1237"),
                "brand": {
                    "brand": "Trek",
                    "Description": "Road bike for long-distance riding",
                    "Price": 700
                },
                "config": {
                    "Size": "L",
                    "Color": "Blue"
                },
                "nb_unit": 2,
                "price": 1400
            }
        ],
        "Date": datetime(2025, 5, 3),
        "Total_price": 1400,
        "Status": "livré"
    },
    {
        "_id": ObjectId(),
        "user": {
            "id_user": ObjectId("665612a5cbe5f12c8a4f1238"),
            "Username": "lucas_dev",
            "Mail": "lucas.dev@mail.com"
        },
        "bikes": [
            {
                "id_bike": ObjectId("665613f1cbe5f12c8a4f1239"),
                "brand": {
                    "brand": "Decathlon",
                    "Description": "Urban bike for daily commutes",
                    "Price": 350
                },
                "config": {
                    "Size": "S",
                    "Color": "Black"
                },
                "nb_unit": 1,
                "price": 350
            },
            {
                "id_bike": ObjectId("665613f1cbe5f12c8a4f1240"),
                "brand": {
                    "brand": "Orbea",
                    "Description": "Electric bike with long battery life",
                    "Price": 1200
                },
                "config": {
                    "Size": "M",
                    "Color": "White"
                },
                "nb_unit": 1,
                "price": 1200
            }
        ],
        "Date": datetime(2025, 5, 5),
        "Total_price": 1550,
        "Status": "livré"
    },
    {
        "_id": ObjectId(),
        "user": {
            "id_user": ObjectId("665612a5cbe5f12c8a4f1239"),
            "Username": "sophie_x",
            "Mail": "sophie.x@example.com"
        },
        "bikes": [
            {
                "id_bike": ObjectId("665613f1cbe5f12c8a4f1241"),
                "brand": {
                    "brand": "BMC",
                    "Description": "Hybrid bike for trails and roads",
                    "Price": 600
                },
                "config": {
                    "Size": "M",
                    "Color": "Green"
                },
                "nb_unit": 1,
                "price": 600
            }
        ],
        "Date": datetime(2025, 5, 6),
        "Total_price": 600,
        "Status": "payé"
    },
    {
        "_id": ObjectId(),
        "user": {
            "id_user": ObjectId("665612a5cbe5f12c8a4f1242"),
            "Username": "maxime99",
            "Mail": "maxime99@hotmail.com"
        },
        "bikes": [
            {
                "id_bike": ObjectId("665613f1cbe5f12c8a4f1243"),
                "brand": {
                    "brand": "Scott",
                    "Description": "Sport BMX bike",
                    "Price": 450
                },
                "config": {
                    "Size": "S",
                    "Color": "Yellow"
                },
                "nb_unit": 2,
                "price": 900
            }
        ],
        "Date": datetime(2025, 5, 7),
        "Total_price": 900,
        "Status": "en attente"
    }
]



result_many = collection.insert_many(sample_orders)
print("IDs insérés pour les autres produits :", result_many.inserted_ids)