import db.mongodb_database as dbm
import os
import sys
from faker import Faker

fake = Faker()
num_records = 20

sys.path.insert(1, "/".join(os.path.realpath(__file__).split("/")[0:-2]) + "/entities")
import bike_item_entity as be

#import bike_brand_entity as bbe
#import order_entity as oe
#import user_entity as ue
#import stat_bike_entity as sbe
#import internal_parameters_entity as ipe

class Migration(dbm.VelostoreDatabaseMongo):
    """Classe pour gérer la migration des données dans la base de données Velostore."""

    def __init__(self):
        """Initialise Migration avec les entités nécessaires."""
        super().__init__()
        self.bike_item_entity = be.BikeItemEntity(self.db)

    def setup(self):
        """Configure les collections."""
        self.bike_item_entity.create_collection()


    def add_dynamics_data(self):
        """Ajoute des données dynamiques aux collections."""
        self.bike_item_entity.insert_data()


def main():
    """Fonction principale pour la classe Migration."""
    initial_setup = Migration()
    initial_setup.setup()
    initial_setup.add_dynamics_data()

if __name__ == "__main__":
    main()
