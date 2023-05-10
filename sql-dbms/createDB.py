import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

dbUser = os.environ.get("DB_USER")
dbPwd = os.environ.get("DB_PWD")

mydb = mysql.connector.connect(
  host="localhost",
  user=dbUser,
  password=dbPwd,
)

mycursor = mydb.cursor()

try:
    mycursor.execute("DROP DATABASE MAC")
except:
    print("No need to delete any database as it doesn't exists")

mycursor.execute("CREATE DATABASE MAC")

