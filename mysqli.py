import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="automotive"
)

mycursor = mydb.cursor()

v1 = "data 1"
v2 = "data 2"


sql = "INSERT INTO demo VALUES (%s,%s)"
#val = ("Michelle", "Blue Village")
mycursor.execute(sql,(v1,v2))

mydb.commit()

print(mydb)