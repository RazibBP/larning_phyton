import mysql.connector
import datetime
import json
with open("data.json") as jason:
    data = json.load(jason)

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = 'Data'

)
mycursor = mydb.cursor()

        
#mycursor.execute("CREATE TABLE castomars (id INT AUTO_INCREMENT PRIMARY KEY,title VARCHAR(255),description VARCHAR(255),category VARCHAR(255),stock INT(255),sku VARCHAR(255),warrantyInformation VARCHAR(255),shippingInformation VARCHAR(255),availabilityStatus VARCHAR(255),returnPolicy VARCHAR(255))")
#mycursor.execute("CREATE TABLE product(id INT AUTO_INCREMENT PRIMARY KEY,price DOUBLE(7,3),discountPercentage DOUBLE(4,2),rating DOUBLE(4,2),weight INT(20),minimumOrderQuantity INT(10),thumbnail VARCHAR(255))")
#sql = "INSERT INTO product(price,discountPercentage,rating,weight,minimumOrderQuantity,thumbnail) VALUES (%s,%s,%s,%s,%s,%s)"
#value = []
#for x in data['products']:

   # value.append(((x['price']),(x['discountPercentage']),(x['rating']),(x['weight']),(x['minimumOrderQuantity']),(x['thumbnail']))) == value

#print(value)
#print(type(value))
#mycursor.executemany(sql,value)
#mydb.commit()
#print(mycursor.rowcount,"row count")

#=================================================================================================================================================================================================================

#mycursor.execute("CREATE TABLE product(id INT AUTO_INCREMENT PRIMARY KEY,price DOUBLE(7,3),discountPercentage DOUBLE(4,2),rating DOUBLE(4,2),weight INT(20),minimumOrderQuantity INT(10),thumbnail VARCHAR(255))")
#sql = "INSERT INTO product(price,discountPercentage,rating,weight,minimumOrderQuantity,thumbnail) VALUES (%s,%s,%s,%s,%s,%s)"
#value = []
#for x in data['products']:

 #   value.append(((x['price']),(x['discountPercentage']),(x['rating']),(x['weight']),(x['minimumOrderQuantity']),(x['thumbnail']))) == value

#print(value)
#print(type(value))
#mycursor.executemany(sql,value)
#mydb.commit()
#print(mycursor.rowcount,"row count")

#===================================================================================================================================================================================================================

#mycursor.execute("CREATE TABLE orderTABLE(orderID INT AUTO_INCREMENT PRIMARY KEY,castomarid INT, FOREIGN KEY (castomarid) REFERENCES castomars(id),productid INT,FOREIGN KEY (productid) REFERENCES product(id),orderTIME DATETIME default CURRENT_TIMESTAMP  )")

#sql = "INSERT INTO orderTABLE (castomarid,productid) VALUES (%s,%s)"

#for x in data['products']:
   # print((x['images']))
#delet = "DROP TABLE orderTABLE "
#mycursor.execute(delet)

#mycursor.executemany(sql,val)
#mydb.commit()
#print(mycursor.rowcount,"row count")

#================================================================================================================================================================================================================================================================

#left join table 
sql = "SELECT castomars.title, castomars.category, castomars.sku, castomars.returnPolicy, orderTABLE.orderID, orderTABLE.orderTIME FROM castomars LEFT JOIN orderTABLE ON castomars.id = orderTABLE.castomarid ORDER BY castomars.title ;"

mycursor.execute(sql)
result = mycursor.fetchall()
for x in result:
    print(x)
