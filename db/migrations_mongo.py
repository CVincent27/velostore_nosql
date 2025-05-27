import json
from database_mongo import VelostoreDatabaseMongo

class Migration(VelostoreDatabaseMongo):
    """Classe pour gérer la migration des données dans la base de données Velostore."""

    def __init__(self):
        """Initialise Migration avec les entités nécessaires."""
        super().__init__()

    def load_json_data(self, file_path):
        """Charge les données depuis un fichier JSON."""
        with open(file_path, 'r') as file:
            return json.load(file)

    def insert_data(self, data):
        """Insère les données dans la base de données."""
        for collection_name, documents in data.items():
            collection = self.db[collection_name]
            collection.insert_many(documents)

def main():
    """Fonction principale pour la classe Migration."""
    initial_setup = Migration()
    data = initial_setup.load_json_data('data.json')
    initial_setup.insert_data(data)

if __name__ == "__main__":
    main()
