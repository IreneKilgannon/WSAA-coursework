# Create a database, wsaa using a python script

import mysql.connector

connection = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = "",
    database = "wsaa"
)

mycursor = connection.cursor()

#########
# Create the database
#mycursor.execute("CREATE DATABASE wsaa")

#########
# Create the table
#sql = "CREATE TABLE student (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50), age INT)"


########
# CRUD operations
#sql = "insert into student (name, age) VALUES (%s, %s)"
#values = ("Mary", 32)
# mycursor.execute(sql, values)

# commit need to add values to table
#connection.commit()
#print("1 record inserted, ID", mycursor.lastrowid)

#######
# View data
#sql = "SELECT * from student where id = %s"
#values = (1, )
#mycursor.execute(sql, values)
#result = mycursor.fetchall()
#for x in result:
#    print(x)


#######
# Update data
#sql = "UPDATE student SET age = %s where id = %s"
#values = (33, 1)
#mycursor.execute(sql, values)
#connection.commit()
#print("Update completed")

#######
# Delete data
sql = "delete from student where id = %s"
values = (1,)
mycursor.execute(sql, values)
connection.commit()
print("Delete completed")

mycursor.close()
connection.close()