import mysql.connector

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password =  '',
    database  ='Data'
)
mycursor = mydb.cursor()

role = input("Enter your role")

sql = "SELECT title FROM castomars UNION ALL SELECT title FROM products ORDER BY title ; "

mycursor.execute(sql)
myresult = mycursor.fetchall()
for s in myresult:
    print(s)

