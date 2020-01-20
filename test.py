import unittest
import os
import main
from main import *

def make_test_files():
    os.makedirs('test_files',exist_ok=True)

    f = open("test_files/test_multiline.txt","w+")
    f.write('''{ "latitude": "36.0", "user_id": 1, "name": "Chris", "longitude": "40.0" }{ "latitude": "37.0", "user_id": 2, "name": "Dave", "longitude": "-10.0" }''')
    f.close()

    f = open("test_files/test_missing_attribute.txt","w+")
    f.write('''{ "latitude": "36.0", "name": "Chris", "longitude": "40.0" }''')
    f.close()

    f = open("test_files/test_correct.txt","w+")
    f.write('''{ "latitude": "37.0", "user_id": 5, "name": "Chris", "longitude": "-122.0" }
    { "latitude": "36.0", "user_id": 2, "name": "Dave", "longitude": "-120.0" }
    { "latitude": "37.05", "user_id": 1, "name": "Alice", "longitude": "-121.95" }''')
    f.close()

class TestCustomerClass(unittest.TestCase):
    """
    Testing Customer class.
    """

    def test_constructor(self):
        customer = Customer("Alice", "10", "5.0", "-5.0")

        self.assertEqual("Alice",customer.name)
        self.assertEqual(10,customer.user_id)
        self.assertEqual((5.0,-5.0),customer.location_degrees)
        # Hand-calculated check
        self.assertTrue(customer.location_radians[0] - 0.087266 < 0.001)
        self.assertTrue(customer.location_radians[1] + 0.087266 < 0.001)

        # Fake user ID
        with self.assertRaises(ValueError):
            customer = Customer("Alice", "12A", 5.0, -5.0)

        # Fake location
        with self.assertRaises(ValueError):
            customer = Customer("Alice", "10", "A1", "B1")

    def test_distance_calculation(self):
        customer1 = Customer("Alice", "10", "5.0", "-5.0")
        customer2 = Customer("Bob", "11", "6.0", "-5.0")
        customer3 = Customer("Charlie", "100", "5.0", "-6.0")
        customer4 = Customer("Dave", "101", "6.0", "-6.0")

        # Hand-calculated checks (Matches intuition that 1 degree of lat/long is ~ 111 km)
        self.assertTrue(customer1.distance_to(customer1.location_radians) < 0.001)
        self.assertTrue(customer1.distance_to(customer2.location_radians) - 117.47827 < 0.001)
        self.assertTrue(customer1.distance_to(customer3.location_radians) - 117.03123 < 0.001)
        self.assertTrue(customer1.distance_to(customer4.location_radians) - 165.75737 < 0.001)

class ReadFileMethod(unittest.TestCase):
    """
    Testing the read of JSON input files
    """

    def test_valid_file(self):
        # File should exist
        with self.assertRaises(FileNotFoundError):
            read_file("Fake_file.txt")

        # File should be in proper format
        with self.assertRaises(ValueError):
            read_file("test_files/test_multiline.txt")
        with self.assertRaises(ValueError):
            read_file("test_files/test_missing_attribute.txt")

        customer_list = read_file("test_files/test_correct.txt")

        self.assertTrue(customer_list[0].user_id == 5 and customer_list[0].name == "Chris")
        self.assertTrue(customer_list[1].user_id == 2 and customer_list[1].name == "Dave")
        self.assertTrue(customer_list[2].user_id == 1 and customer_list[2].name == "Alice")

class FindCorrectUsersMethod(unittest.TestCase):
    """
    Testing full program logic.
    """
    def test_program(self):
        input_file_path = "test_files/test_correct.txt"
        output_file_path = "test_files/test_output.csv"
        distance_from_base_margin = 100.0
        base_location = (37.788802 * (math.pi/180.0), -122.4025067 * (math.pi/180.0))

        read_and_write(input_file_path,output_file_path,distance_from_base_margin,base_location)
        f = open(output_file_path,"r")
        lines = f.readlines()
        f.close()

        # Only one valid customer found
        self.assertEqual(len(lines),3)

        # Customer is the correct customer (and lines are in order)
        user_id,name = lines[1].split(",")
        self.assertEqual(user_id,"1")
        self.assertEqual(name,"Alice\n")

        user_id,name = lines[2].split(",")
        self.assertEqual(user_id,"5")
        self.assertEqual(name,"Chris\n")


if __name__ == '__main__':
    make_test_files()
    unittest.main()
