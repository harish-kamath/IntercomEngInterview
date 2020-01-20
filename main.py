import json
import math

# GLOBAL VARIABLES
input_file_path = "Customer List.txt" # relative or full path
output_file_path = "Found Customers.csv" # relative or full path
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
        Calculate distance from customer to given location (using first formula from https://en.wikipedia.org/wiki/Geographical_distance).

        Parameters:
            location (tuple(float)): Location to calculate the distance to (in radians)

        Returns:
            float: Distance between customer and given location
        """
        lat, long = location
        customer_lat, customer_long = self.location_radians

        dlat = customer_lat - lat
        dlong = customer_long - long
        mean_lat = (customer_lat + lat)/2.0

        # Earth's Radius (constant)
        R = 6731.009

        # Calculated using the formula D = R * sqrt(delta_lat^2 + (cos(mean_lat) * delta_long)^2)
        return R * math.sqrt(math.pow(dlat,2) + math.pow(math.cos(mean_lat) * dlong,2))



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
    with open(filepath) as json_file:
        try:
            customers_list = [json.loads(record) for record in json_file]
        except:
            raise ValueError('Your JSON input can\'t be read! Please refer to README for details on how to format the JSON input.')
        return [Customer(c["name"],c["user_id"],c["latitude"],c["longitude"]) for c in customers_list]
    return None

if __name__ == "__main__":
    # Read all customers into program
    print("Reading input from {}".format(input_file_path))
    customers = read_file(input_file_path)
    print("Total customers found: {}".format(len(customers)))

    # Find all customers within the given range
    in_range_customers = list(filter(lambda customer: customer.distance_to(base_location) <= distance_from_base_margin, customers))
    print("Found {} customers within a {}-km radius of the base!".format(len(in_range_customers), distance_from_base_margin))

    # Sort ranged customers by user ID
    in_range_customers.sort(key=lambda c: c.user_id)

    # Write to file
    with open(output_file_path,"w+") as output_file:
        output_file.write("User ID,Name\n")
        for customer in in_range_customers:
            output_file.write("{},{}\n".format(customer.user_id, customer.name))
    print("Results written to {}.".format(output_file_path))

    print("\nDone!")
