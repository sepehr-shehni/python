import mysql.connector
mydb = mysql.connector.connect(host="localhost",
user="root",
password = "Master123$",
database = "Student"
)

mycursor = mydb.cursor()
sql = " DROP DATABASE Student "
mycursor.execute(sql)
