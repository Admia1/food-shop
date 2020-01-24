import mysql.connector as mariadb

try:
    mariadb_connection = mariadb.connect(user='kiho', password='kiho', database='kiho')
except:
    print("oh fuck")
cursor = mariadb_connection.cursor()

cursor.execute("SELECT * FROM City")

result = cursor.fetchall()

for row in result:
    print ("id = ",row[0])
    print ("name = ",row[1])
    print ("location = ",row[0])

