import mysql.connector
mydb = mysql.connector.connect(host="localhost", user="root", password = "Master123$")

# Creat Database 
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE Techone24")
