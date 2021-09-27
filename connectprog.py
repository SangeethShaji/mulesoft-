import mysql.connector

conn = mysql.connector.connect(
   user='root', password='' , host='127.0.0.1', database='cinema')

cursor = conn.cursor()

sql = '''SELECT * from cinema.movies'''

cursor.execute(sql)


result = cursor.fetchall();
print(result)

conn.close()
