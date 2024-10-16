import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Data"
)

mycursor = mydb.cursor()

#sql = "SELECT title AS 'p_name' FROM castomars ;"
#mycursor.execute(sql)
#mycursor.execute("SELECT * FROM product")
sql = "SELECT CONCAT (stock,' ',sku) AS 'Available' FROM castomars;"
mycursor.execute(sql)
myresult = mycursor.fetchone()

print(myresult)