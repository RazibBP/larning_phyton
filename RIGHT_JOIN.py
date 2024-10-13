import mysql.connector
import datetime
  
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database = 'Data'

)
mycursor = mydb.cursor()

sql = "SELECT orderTABLE.orderID, orderTABLE.castomarid, orderTABLE.orderTIME, castomars.title, castomars.sku, castomars.shippingInformation FROM orderTABLE RIGHT JOIN castomars ON orderTABLE.castomarid = castomars.id ORDER BY orderTABLE.orderID"
mycursor.execute(sql)
result  = mycursor.fetchall()

for s in result:
    print(s)