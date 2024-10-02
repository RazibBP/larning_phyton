import mysql.connector
import json

with open('data.json') as f:
    data = json.load(f)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",

)

mycursor = mydb.cursor()

mycursor.execute("show databases")

# print(data)

print (data)

for x in data['products']:
  print(x['title'], x['id'])


