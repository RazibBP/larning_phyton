from basic import *

sql = "SELECT AVG(price) FROM prices;"
srl = "SELECT MIN(price) FROM prices;"
sxl = "SELECT max(price) FROM prices;"
scl = "SELECT sum(stock) FROM prices;"

mycursor.execute(sql)
my = mycursor.fetchall()
for x in my:
    print(x)

mycursor.execute(srl)
my  = mycursor.fetchall()
for x in my:
    print(x)

mycursor.execute(sxl)
my = mycursor.fetchall()
for s in my:
    print(s)

mycursor.execute(scl)
my = mycursor.fetchall()
for x in my:
    print(x)

