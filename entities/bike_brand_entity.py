import os
import sys

# Ajoutez le chemin du module à sys.path
sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/../db")

# Importez le module de la base de données
import mongodb_database as db

class VelostoreDatabase:
    """Classe de base pour gérer les opérations de base de données."""

    def __init__(self):
        """Initialise la connexion à la base de données."""
        self.db = db.client['votre_base_de_donnees'] 

class BikeBrandEntity(VelostoreDatabase):
    """Classe pour gérer les opérations de base de données liées aux marques de vélos."""

    def __init__(self):
        """Initialise BikeBrandEntity."""
        super().__init__()
        self.collection = self.db["Bike"] 

    def create_tables(self):
        """Crée les tables nécessaires dans la base de données."""
        self.create_bike_table()

    def create_bike_table(self):
        """Crée la table des vélos."""
        # La collection est déjà initialisée dans __init__
        pass

    def create_schema_bike(self):
        """Définition du schéma pour la collection Bike."""
        schema = {
            "bsonType": "object",
            "properties": {
                "brand": {
                    "bsonType": "object",
                    "properties": {
                        "Description": {"bsonType": "string"},
                        "Price": {"bsonType": "int"},
                        "Image": {"bsonType": "string"},
                        "Destination": {"bsonType": "string"}
                    }
                },
                "config": {
                    "bsonType": "object",
                    "properties": {
                        "Size": {"bsonType": "string"},
                        "Color": {"bsonType": "string"}
                    }
                },
                "Status": {"bsonType": "string"}
            }
        }

        validator = {"$jsonSchema": schema}

        # Appliquer le schéma
        self.db.command("collMod", "Bike", validator=validator)

    def create_collection(self):
        """Crée la collection BikeItem si elle n'existe pas."""
        if "BikeItem" not in self.db.list_collection_names():
            self.db.create_collection('BikeItem')
            print("Collection 'BikeItem' créée.")
        else:
            print("La collection 'BikeItem' existe déjà.")

    def insert_data_bike(self):
        """Insère un document de test dans la collection Bike."""
        bike_data_test = {
            "brand": {
                "Description": "Un vélo de montagne robuste",
                "Price": 500,
                "Image": "image_url",
                "Destination": "Montagne"
            },
            "config": {
                "Size": "M",
                "Color": "Bleu"
            },
            "Status": "Disponible"
        }

        # Insérer le document dans la collection
        self.collection.insert_one(bike_data_test)
        print("Document inséré avec succès.")

def main():
    """Fonction principale pour la classe BikeBrandEntity."""
    super_velo = BikeBrandEntity()
    super_velo.create_tables()
    super_velo.create_schema_bike()
    super_velo.create_collection()
    super_velo.insert_data_bike()

if __name__ == '__main__':
    main()
