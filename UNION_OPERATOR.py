import mysql.connector

mydb = mysql.connector.connect(

  host="localhost",
  user="root",
  password="",
  database = 'Data'

)

mycursor = mydb.cursor()

sql ="SELECT title FROM castomars UNION SELECT price FROM prices ORDER BY title;"
mycursor.execute(sql)
result = mycursor.fetchall()

for x in result:
    print(x)