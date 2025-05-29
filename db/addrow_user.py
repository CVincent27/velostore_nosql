from pymongo import MongoClient

# Connexion au serveur MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Récupération (ou création) d'une base de données
db = client["mangovelodatabase"]


# Création (ou accès) de la collection "products"
collection = db["user"]

# 2. Insérer plusieurs documents à la fois (INSERT MANY)
new_user = [
    {
        "user_type": "utilisateur",
        "username": "jules100",
        "status": "actif",
        "mail": "jules@gmail.com",
        "password": "vl4e5swer5@"
    },
    {
        "user_type": "utilisateur",
        "username": "emma200",
        "status": "actif",
        "mail": "emma200@gmail.com",
        "password": "P@ssword2024"
    },
    {
        "user_type": "utilisateur",
        "username": "lucas_dev",
        "status": "inactif",
        "mail": "lucas.dev@mail.com",
        "password": "devL1234@"
    },
    {
        "user_type": "utilisateur",
        "username": "sophie_x",
        "status": "actif",
        "mail": "sophie.x@example.com",
        "password": "s0Ph!e456"
    },
    {
        "user_type": "utilisateur",
        "username": "maxime99",
        "status": "suspendu",
        "mail": "maxime99@hotmail.com",
        "password": "MaX_789$"
    },
    {
        "user_type": "utilisateur",
        "username": "lea_moon",
        "status": "actif",
        "mail": "lea.moon@outlook.fr",
        "password": "leaMoon#1"
    },
    {
        "user_type": "utilisateur",
        "username": "tommy_t",
        "status": "actif",
        "mail": "tommy_t@gmail.com",
        "password": "TomT123@"
    },
    {
        "user_type": "utilisateur",
        "username": "noemie_45",
        "status": "inactif",
        "mail": "noemie45@yahoo.fr",
        "password": "NoeMIE_98%"
    },
    {
        "user_type": "utilisateur",
        "username": "adrien.k",
        "status": "actif",
        "mail": "adrien.k@protonmail.com",
        "password": "adr1enK#56"
    },
    {
        "user_type": "utilisateur",
        "username": "claire.z",
        "status": "actif",
        "mail": "claire.z@gmail.com",
        "password": "cl@ireZ2025"
    }
]
result_many = collection.insert_many(new_user)
print("IDs insérés pour les autres produits :", result_many.inserted_ids)

# # GET BIKE BY BRAND
# def get_bike_by_brand(brand: int) -> dict:
#     one_product = collection.find_one({"brand": brand})
#     return print("Un produit en Electronics :", one_product)

# get_bike_by_brand("Rockrider")
