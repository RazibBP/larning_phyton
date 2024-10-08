#import mysql.connector

#import json
#with open ('data.json') as f:
  #  data = json.load(f)

mydb = mysql.connector.Connect(
    host="localhost",
    user="root",
    password="",
    database = 'product'
 
)
print(mydb)
