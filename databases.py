import mysql.connector

import json
with open ("data.json") as jason:
    data = json.load(jason)

mydb = mysql.connector.connect(

  host="localhost",
  user="root",
  password="",
  database = 'Data'

)
mycursor = mydb.cursor()
#mycursor.execute("CREATE TABLE products(id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255),description VARCHAR(255),category VARCHAR(255),brand VARCHAR(255),sku VARCHAR(255),warrantyInformation VARCHAR(255),shippingInformation VARCHAR(255),availabilityStatus VARCHAR(255),returnPolicy VARCHAR(255))")
#mycursor.execute("CREATE TABLE products(id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255),description VARCHAR(255),category VARCHAR(255),sku VARCHAR(255),warrantyInformation VARCHAR(255),shippingInformation VARCHAR(255),availabilityStatus VARCHAR(255),returnPolicy VARCHAR(255))")
#sql = "INSERT INTO products (title,description,category,sku,warrantyInformation,shippingInformation,availabilityStatus,returnPolicy) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)"

#val = []

#for x in data['products']:
  #  val.append(((x['title']),(x['description']),(x['category']),(x['sku']),(x['warrantyInformation']),(x['shippingInformation']),(x['availabilityStatus']),(x['returnPolicy']))) == val

#print(val)
#mycursor.executemany(sql,val)
#mydb.commit()
#print(mycursor.rowcount, "was inserted.")

#mycursor.execute("DROP TABLE price")

#mycursor.execute("CREATE TABLE prices (productID INT AUTO_INCREMENT PRIMARY KEY,price DOUBLE(11,4),discountPercentage DOUBLE(5,3),rating DOUBLE(4,2),stock INT(255),weight INT(255),minimumOrderQuantity INT(255))")

#sql = "INSERT INTO prices (price,discountPercentage,rating,stock,weight,minimumOrderQuantity) VALUES (%s,%s,%s,%s,%s,%s)"

#valu = []
#for x in data['products']:
 #   valu.append(((x['price']),(x['discountPercentage']),(x['rating']),(x['stock']),(x['weight']),(x['minimumOrderQuantity']))) == valu

#print (valu)
#print(type(valu))

#mycursor.executemany(sql,valu)
#mydb.commit()
#print(mycursor.rowcount,"row count")

#mycursor.execute("CREATE TABLE order_LIST (orderID INT AUTO_INCREMENT PRIMARY KEY,p_ID INT,FOREIGN KEY (p_ID) REFERENCES prices(productID),c_ID INT,FOREIGN KEY(c_id) REFERENCES products(id))")

#sql = "INSERT INTO order_LIST (p_ID,c_ID) VALUES (%s,%s)"
#valu = [

#]
#mycursor.executemany(sql,valu)

#mydb.commit()
#print(mycursor.rowcount,"row count")

#sql = "SELECT products.title,products.category,products.sku, order_LIST.orderID FROM products INNER JOIN order_LIST ON products.id = order_LIST.p_ID ORDER BY products.category ; "

#mycursor.execute(sql)

#myresult = mycursor.fetchall()

#for x in myresult:
 # print(x)
