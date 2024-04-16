import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "Master123$",
database = "Techone24"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT name FROM product")
myresult = mycursor.fetchall()


for x in myresult:
    print(x)