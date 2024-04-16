import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Master123$",
  database="mydatabase"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("SELECT * FROM customers LIMIT 5")
 
myresult = mycursor.fetchall()
 
for x in myresult:
  print(x)