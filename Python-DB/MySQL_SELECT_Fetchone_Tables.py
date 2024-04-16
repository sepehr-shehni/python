import mysql.connector
 
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Master123$",
  database="Techone24"
)
 
mycursor = mydb.cursor()
 
mycursor.execute("SELECT * FROM customers")
 
myresult = mycursor.fetchone()
 
print(myresult)