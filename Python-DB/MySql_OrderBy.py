import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "Master123$",
database = "Techone24"
)

mycursor = mydb.cursor()
sql = "SELECT * FROM customers ORDER BY name "
mycursor.execute(sql)
myresult = mycursor.fetchall()


for x in myresult:
    print(x)
