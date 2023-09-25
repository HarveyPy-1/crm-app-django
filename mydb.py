import os
import mysql.connector
from dotenv import load_dotenv

load_dotenv()

dataBase = mysql.connector.connect(
    host='localhost',
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD')
)

# Prepare a cursor object
cursorObject = dataBase.cursor()

# Create a database or do it manually in the terminal or workbench
cursorObject.execute("CREATE DATABASE crm_database")
print("Database created!")
