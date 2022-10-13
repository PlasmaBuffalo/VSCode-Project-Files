#Are we using SQL Workbench?

import pymysql

mydb = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    database ="testdb"
)
mycursor = mydb.cursor()

#Create table
mycursor.execute("CREATE TABLE chat (LogID INTEGER(),Sender VARCHAR(), Receiver VARCHAR(), Message VARCHAR(), Timestamp INTEGER(), WasSuccess BOOLEAN())")

#Pass data into database, %s=placeholders
#Populating the database
sqlFormula = "INSERT INTO chat (LogID,Sender,Receiver,Message,Timestamp,WasSuccess) VALUES (%s,%s,%s,%s,%s,%s)"

#To check if table exists
mycursor.execute("SHOW TABLES")
for tb in mycursor:
    print(tb)

mycursor.execute("CREATE DATABASE chatdb") #name of db = chatdb, SQL command
mycursor.execute("SHOW DATABASES")
for db in mycursor:
    print(db)
