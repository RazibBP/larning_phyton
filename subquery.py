import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "Data"
)
mycursor = mydb.cursor()

sql = "SELECT * FROM product WHERE id IN ( SELECT id FROM product  WHERE weight > 9 );"

mycursor.execute(sql)
myresult = mycursor.fetchall()
for s in myresult:
    print(s)
