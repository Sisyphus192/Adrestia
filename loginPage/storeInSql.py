import sys
import mysql.connector as mc

try:
    connection = mc.connect (host = "localhost",
                             user = "root",
                             passwd = "",
                             db = "Adrestia")
except mc.Error as e:
    print("Error %d: %s" % (e.args[0], e.args[1]))
    sys.exit(1)

cursor = connection.cursor()

cursor.execute ("DROP TABLE IF EXISTS userInfo")

sql_command = """
CREATE TABLE userInfo (
userName VARCHAR(20) PRIMARY KEY,
password VARCHAR(20));"""

cursor.execute(sql_command)

userName = raw_input("Enter user name: ")
password = raw_input("Enter password: ")

sql_command = "INSERT INTO userInfo (userName, password) VALUES " + "('" + userName + "', '" + password + "');"

cursor.execute(sql_command)

connection.commit()


cursor.close()
connection.close()