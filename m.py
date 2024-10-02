import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='student_fill'

)

print(mydb)
mycursor = mydb.cursor()


#mycursor.execute("show databases")
#mycursor.execute("SHOW TABLES")
#mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
#mycursor.execute("SHOW TABLES")



#insert single data in table

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = ("Michelle", "Blue Village")
#mycursor.execute(sql,val)



#insert into table value manay data 

#sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
#val = [
 # ('Richard', 'Sky st 331'),
 # ('Susan', 'One way 98'),
 # ('Vicky', 'Yellow Garden 2'),
 # ('Ben', 'Park Lane 38'),
 # ('William', 'Central st 954'),
 # ('Chuck', 'Main Road 989'),
 # ('Viola', 'Sideway 1633')
#]

##mycursor.executemany(sql, val)
#mydb.commit()
#for x in mycursor:
   # print(x)
#print(mycursor.rowcount, "record inserted.")



#Table show comand 

#mycursor.execute("SELECT * FROM Result_Sheet")
#myresult = mycursor.fetchall()
#for x in myresult:
 # print(x)


#use Where statemant delete row

#sql = "DELETE FROM customers WHERE address = 'Mountain 21'"
#mycursor.execute(sql)
#mydb.commit()
#print(mycursor.rowcount, "record(s) deleted")


#Table delete comand

#sql = "DROP TABLE customers"
#mycursor.execute(sql)



#racoude updater comand

#sql = "UPDATE customers SET address = 'Valley 345' WHERE address = 'Canyon 123'"
#mycursor.execute(sql)
#mydb.commit()
#print(mycursor.rowcount, "record(s) ")


#Limit use for mysql in python code

#mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
#myresult = mycursor.fetchall()
#for x in myresult:
#  print(x)





