import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "Master123$",
database = "Techone24"
)

mycursor = mydb.cursor()
sql = " DROP TABLE customers "
mycursor.execute(sql)
