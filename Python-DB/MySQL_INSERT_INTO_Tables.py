import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Master123$",
  database="Techone24"
)
 
mycursor = mydb.cursor()
 
sql = "INSERT INTO product (name, address) VALUES (%s, %s)"
val = ("Mobile", "iran")
mycursor.execute(sql, val)
 
mydb.commit()
 
print(mycursor.rowcount, "record inserted.")