# import the mysql client for python

import pymysql

#rpw = e77G7T$bNwIAJ4VfRlW#

# Create a connection object

databaseServerIP = "127.0.0.1"  # IP address of the MySQL database server

databaseUserName = "root"       # User name of the database server

databaseUserPassword = ""           # Password for the database user

newDatabaseName = "NewDatabase"  # Name of the database that is to be created

charSet = "utf8mb4"     # Character set

connectionInstance = pymysql.connect(
    host=databaseServerIP, user=databaseUserName, password=databaseUserPassword, charset=charSet)

try:

    # Create a cursor object

    cursorInsatnce = connectionInstance.cursor()

    # SQL Statement to create a database

    sqlStatement = "CREATE DATABASE "+newDatabaseName

    # Execute the create database SQL statment through the cursor instance

    cursorInsatnce.execute(sqlStatement)

    # SQL query string

    sqlQuery = "SHOW DATABASES"

    # Execute the sqlQuery

    cursorInsatnce.execute(sqlQuery)

    # Fetch all the rows

    databaseList = cursorInsatnce.fetchall()

    for datatbase in databaseList:

        print(datatbase)


except Exception as e:

    print("Exeception occured:{}".format(e))


finally:

    connectionInstance.close()
