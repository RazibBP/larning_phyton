import mysql.connector

mydb = mysql.connector.connect(

  host="localhost",
  user="root",
  password="",
  database = 'Data'

)
mycursor = mydb.cursor()

sql = "SELECT prices.productID,prices.price,prices.discountPercentage, order_LIST.orderID FROM prices INNER JOIN order_LIST ON prices.productID = order_list.c_ID ORDER BY order_LIST.orderID"

mycursor.execute(sql)
result = mycursor.fetchall()
for x in result:
    print(x)