# Flask
Final Hands on

Code Readme:
This repository contains a Python code file api.py and a test file tests.py for testing the functionality of the API implemented in api.py. The code is written using the Flask framework and provides basic CRUD operations for managing actors in a database.

Setup and Dependencies:
Before running the code and tests, make sure you have the following dependencies installed:

Python 3.x
Flask
Flask-MySQLdb
Flask-HTTPAuth
unittest (built-in Python library)
black(optional)

(pip install for flask and needed libraries)
pip install flask flask-mysqldb flask-httpauth

Running the Code:
To run the API code, execute the following command in your terminal or command prompt:
python api.py

The API will start running on http://localhost:5000/.

Running the Tests:
The test file tests.py contains unit tests for the API endpoints. To run the tests, execute the following command in your terminal or command prompt:
python tests.py

The tests will be executed, and the results will be displayed in the console.

Description of Files:
api.py: This file contains the implementation of the API endpoints and database connection using Flask and MySQL. It provides CRUD operations for managing actors.

tests.py: This file contains the unit tests for testing the functionality of the API endpoints. It uses the unittest framework to define and run the tests.

Test Cases
The test cases in tests.py cover the following scenarios:

Test the index page ("/") to ensure it returns a status code of 200 and the expected response.
Test the "/actors" endpoint to ensure it returns a status code of 200 and contains the expected actor data.
Test the "/actors/<id>" endpoint with a specific actor ID to ensure it returns a status code of 200 and contains the expected actor data.

Tips:
  
It is recommended to create a virtual environment for this project to isolate its dependencies. This ensures that the project's dependencies do not conflict with other Python projects or the global Python environment on your system.
By using a virtual environment, you can easily manage and install project-specific dependencies without affecting your system-wide Python installation.
Activating the virtual environment before running the code or tests ensures that the correct dependencies are used.
Remember to keep your virtual environment and project dependencies up to date by periodically checking for updates and upgrading packages as needed. You can use the pip package manager to handle package installations and updates within the virtual environment.

 Feel free to explore and modify the code to suit your needs.
