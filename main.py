import mysql.connector as mydb
conn = mydb.connect(
    host="localhost",
    user="app_user",
    port="3306",
    password="!ChangeMe!",
    database="app_db"
)

conn.ping(reconnect=True)
print(conn.is_connected())
