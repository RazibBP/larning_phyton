import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="RazibBP",
  password="3121"
)

print(mydb)