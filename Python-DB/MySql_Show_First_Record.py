import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "Master123$",
database = "Arjang"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchone()

print(myresult)
