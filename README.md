# Harish Kamath's Intercom Engineering Internship Take-Home

This repository contains all files pertaining to Harish Kamath's Intercom Engineering Internship Take-Home Test. Code is written and tested in Python 3+.

## Problem Statement

We have some customer records in a text file (customers.txt) -- one customer per line, JSON lines formatted. We want to invite any customer within 100km of our San Francisco office for some food and drinks on us. Write a program that will read the full list of customers and output the names and user ids of matching customers (within 100km), sorted by User ID (ascending). You must use the first formula from this [Wikipedia article](https://en.wikipedia.org/wiki/Geographical_distance) to calculate distance. Don't forget, you'll need to convert degrees to radians. The GPS coordinates for our SF office are 37.788802,-122.4025067.

## Design Principles/Requirements

- Produce working code, with enough room to demonstrate how to structure components in a small program.
- Submit code as if you intended to ship it to production.
- Code must be tested. Test cases cover likely problems.
- Include the output of your program with your submission in a separate file, e.g., output.txt.
- Include a file explaining how to install, how to execute the code and how to run tests.
- Provide sample output.

For more, visit: [Take-Home Assessment Blog Post](https://www.intercom.com/blog/engineer-interview-assignments/)

## Code Requirements

- Python 3+
- Packages (all packages come default with Python 3+):
    - unittest
    - os
    - math
    - json

Input file must be in JSON format. Additionally, each customer must have at least `latitude`,`longitude`,`user_id`, and `name` attributes. Each customer record must be on a separate line. Example formatting is shown in `Customer List.txt`.

## To Install and Run

Navigate to the home directory. Run `python main.py` to execute the program. Run `python test.py -bv` to execute tests. In order to change the input file, output file, maximum distance allowed from base, or base location, edit the global variables located at the top of `main.py`. By default, results are written to `Found Customers.csv`. Test results can be found in the `test_files/` folder.
