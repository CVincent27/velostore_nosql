from faker import Faker

fake = Faker()

class BikeItemEntity:
    """Classe pour gérer les entités de vélos."""

    def __init__(self, db):
        """Initialise BikeItemEntity avec une instance de la base de données."""
        self.db = db

    def create_schema_bike_item(self):
        """Définir le schéma pour la collection."""
        self.schema = {
            "bsonType": "object",
            "required": ["id_bike", "brand", "size", "color", "status"],
            "properties": {
                "id_bike": {"bsonType": "int"},
                "brand": {"bsonType": "string"},
                "size": {"bsonType": "string"},
                "color": {"bsonType": "string"},
                "status": {"bsonType": "string"}
            }
        }
        self.validator = {"$jsonSchema": self.schema}

    def create_collection(self):
        """Créer une collection pour les vélos."""
        if "BikeItem" not in self.db.list_collection_names():
            self.db.create_collection('BikeItem')
            print("Collection 'BikeItem' créée.")
        else:
            print("La collection 'BikeItem' existe déjà.")

    def insert_data(self):
        """Insère des données dynamiques dans la collection des vélos."""
        bike_data = {
            "name": fake.word(),
            "price": fake.random_number(digits=3),
            "brand": fake.company(),
            "quantity": fake.random_number(digits=2)
        }
        self.db.BikeItem.insert_one(bike_data)
        print("Données dynamiques insérées dans la collection des vélos.")
