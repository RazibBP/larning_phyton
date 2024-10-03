import mysql.connector
import json

with open ("data.json") as jason:
    data = json.load(jason)


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = 'product'

)


mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE products (id int(255),title VARCHAR(255), description VARCHAR(255))")

mycursor.execute("CREATE TABLE product_LIST (id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255),description VARCHAR(255),category VARCHAR(255),price DOUBLE(7,2))")

sql = "INSERT INTO product_LIST (id,title,description,category,price) VALUES(%s,%s,%s,%s,%s)"

val = []
#for x in data["products"]:
   # print((x["id"]),(x["title"]),x[("description")])

for x in data['products']:
  #  print((x['id']),",",(x['title']))
    val.append(((x['id']),(x['title']),(x['description']),(x['category']),(x['price']))) == val

#print(type(val))
#mycursor.execute(sql,val)


mycursor.executemany(sql, val)
mydb.commit()
print(mycursor.rowcount, "was inserted.")

#print(val)


#sql = "DROP TABLE product_LIST"
#mycursor.execute(sql)
