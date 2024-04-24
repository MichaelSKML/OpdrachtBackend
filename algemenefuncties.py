import mysql.connector
import os
import dotenv
from dotenv import load_dotenv

def verbindingdb():
    mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

    return mydb