import mysql.connector
import json

#with open('data.json') as f:
 #   data = json.load(f)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",

)

mycursor = mydb.cursor()

mycursor.execute("show databases")

# print(data)

#print (data)
#val = []

for x in data['products']:
  print(x['title'], x['id'])


val = [
  ('Peter', 'Lowstreet 4'),
  ('Amy', 'Apple st 652'),
  ('Hannah', 'Mountain 21'),
  ('Michael', 'Valley 345'),
  ('Sandy', 'Ocean blvd 2'),
  ('Betty', 'Green Grass 1'),
  ('Richard', 'Sky st 331'),
  ('Susan', 'One way 98'),
  ('Vicky', 'Yellow Garden 2'),
  ('Ben', 'Park Lane 38'),
  ('William', 'Central st 954'),
  ('Chuck', 'Main Road 989'),
  ('Viola', 'Sideway 1633')
]

print(type(val))

