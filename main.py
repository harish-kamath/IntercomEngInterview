import json
import math

# GLOBAL VARIABLES
customer_file_path = "Customer List.txt" # relative or full path
distance_from_base_margin = 100 # In km
base_location = (37.788802 * (math.pi/180.0), -122.4025067 * (math.pi/180.0)) # In radians

class Customer:
    """
    Customer class to hold information about each customer given.

    Attributes:
        user_id (int): Unique User ID of customer
        name (str): Name of customer
        location (tuple(int)): Customer Location
    """

    def __init__(self, name, user_id, latitude, longitude):
        """
        Customer Constructor

        Parameters:
           name (str): Customer name
           user_id (int): Unique customer ID
           latitude (float): Customer latitudinal location (in degrees)
           longitude (float): Customer longitudinal location (in degrees)
        """
        self.name = str(name)
        self.user_id = int(user_id)
        self.location_degrees = (float(latitude), float(longitude))
        # Calculating location in radians using standard formula radians = degrees * pi/180
        self.location_radians = (float(latitude)*(math.pi/180.0), float(longitude)*(math.pi/180.0))

    def distance_to(self, location):
        """
        Calculate distance from customer to given location.

        Parameters:
            location (tuple(float)): Location to calculate the distance to (in radians)

        Returns:
            float: Distance between customer and given location
        """
        pass


def read_file(filepath):
    """
    Reads customer list file of all customers, ids, and locations.

    Parameters
    ----------
    filepath : string
        File path of Customer List JSON file with given format

    Returns
    -------
    list
        List of Customers
    """
    pass

if __name__ == "__main__":
    pass
