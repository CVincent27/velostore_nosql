from pymongo import MongoClient

class VelostoreDatabaseMongo():
    """Classe pour gérer la base de données Velostore."""

    def __init__(self):
        """Initialise la connexion à la base de données."""
        self.connection_db()
        self.create_schema_bike_item()
        self.create_collection()

    def connection_db(self) -> None:
        """Crée une connexion et un objet curseur pour la base de données."""
        client = MongoClient("mongodb://localhost:27017/")
        self.db = client["velostore_db"]

    #def create_collection(self):
    #    """Créer une collection avec le schéma défini."""
    #    if "User" not in self.db.list_collection_names():
    #        self.db.create_collection('User', validator=self.validator)
    #        print("Collection 'User' créée avec validation de schéma.")
    #    else:
    #        print("La collection 'User' existe déjà.")

velostore_db = VelostoreDatabaseMongo()
