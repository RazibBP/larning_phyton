from basic import *

sql = "SELECT c.title , c.category , o.orderID, orderTIME  FROM castomars AS c , orderTABLE AS o;"

mycursor.execute(sql)
my = mycursor.fetchall()
for x in my:
    print(x)