import mysql.connector
mydb = mysql.connector.connect(host="localhost", 
user="root", 
password = "Master123$",
database = "Arjang"
)

mycursor = mydb.cursor()
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
