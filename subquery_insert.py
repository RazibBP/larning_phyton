import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Data"
)

mycursor = mydb.cursor()
#sql = "CREATE TABLE product_copy(id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255),description VARCHAR(255),category VARCHAR(255),stock INT(255),sku VARCHAR(255),warrantyInformation VARCHAR(255),shippingInformation VARCHAR(255),availabilityStatus VARCHAR(255),returnPolicy VARCHAR(255))"
inse = " INSERT INTO product_copy SELECT * FROM castomars  WHERE id IN(SELECT id FROM castomars)"
#mycursor.execute(sql)
#mydb.commit()
mycursor.execute(inse)
mydb.commit()
print(mycursor.rowcount,"")
#myresult = mycursor.fetchall()
##   print(s)
