import pymongo
from pymongo import MongoClient


class VelostoreDatabaseMongo():
    """Classe pour gérer la base de données Velostore."""

    def __init__(self):
        """Initialise la connexion à la base de données."""
        self.connection_db()

    def connection_db(self) -> None:
        """Crée connexion pour la base de données."""
        client = MongoClient("mongodb://localhost:27017/")
        self.db = client["velostore_db"]

velostore_db = VelostoreDatabaseMongo()
