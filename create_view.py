from basic import *

sql = "CREATE VIEW castomars_v AS SELECT id,title,stock,sku FROM castomars WHERE id IS NOT NULL ;"
mycursor.execute(sql)
mydb.commit()
#myresult = mycursor.fetchall()
#for s in myresult:
 #   print(s)

 