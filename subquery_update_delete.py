import mysql.connector

mydb  = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Data"

)
mycursor = mydb.cursor()
#sql = "UPDATE castomars SET stock=stock*3 WHERE category IN(SELECT category FROM product_copy WHERE category = 'fragrances')"

#mycursor.execute(sql)
#mydb.commit()


sql = "DELETE FROM product_copy WHERE stock IN (SELECT stock FROM castomars WHERE stock = 1);"
mycursor.execute(sql)
mydb.commit()

