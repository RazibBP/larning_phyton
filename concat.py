from basic import *
mycursor = mydb.cursor()
sql = "SELECT CONCAT (stock,' ',sku) AS 'Available' FROM castomars;"
mycursor.execute(sql)
myresult = mycursor.fetchone()
print(myresult)



