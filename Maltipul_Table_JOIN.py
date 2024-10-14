import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database  ="Data"
)

mycursor = mydb.cursor()

sql = "SELECT orderTABLE.orderID,orderTABLE.orderTIME, castomars.title,castomars.sku, product.price,product.rating FROM orderTABLE INNER JOIN castomars ON orderTABLE.castomarid = castomars.id INNER JOIN product ON orderTABLE.productid = product.id ORDER BY orderTABLE.orderID "
mycursor.execute(sql)
myresult = mycursor.fetchall()
for x in myresult:
    print(x)