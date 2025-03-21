import mysql.connector
import config as cfg 

class StudentDAO:
    host =""
    user = ""
    password =""
    database =""
    connection = ""
    cursor =""

    def __init__(self):
# read from a config file
        self.host= cfg.mysql['host']
        self.user= cfg.mysql['user']
        self.password= cfg.mysql['password']
        self.database= cfg.mysql['database']

    def getCursor(self):
        self.connection = mysql.connector.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )
        self.cursor = self.connection.cursor()
        return self.cursor

    def closeAll(self):
        self.connection.close()
        self.cursor.close()

    def convertToDictionary(self, resultLine):
        attkeys=['id', 'name','age']
        student = {}
        currentkey = 0
        for attrib in resultLine:
            student[attkeys[currentkey]] = attrib
            currentkey = currentkey + 1 
        return student

    def getAll(self):
        cursor = self.getCursor()
        sql = "SELECT * from student order by id"
        cursor.execute(sql)
        results = cursor.fetchall()
        studentlist = []
        for row in results:
            studentlist.append(self.convertToDictionary(row))
        self.closeAll()
        return studentlist

    # Create new student
    def create(self, student):
        cursor = self.getCursor()
        sql="INSERT INTO student (id, name, age) VALUES (%s, %s, %s)"
        values = [student['id'], student['name'], student['age']]
        cursor.execute(sql, values)
        self.connection.commit()
        newid = cursor.lastrowid
        self.closeAll()
        return newid

    # Find student by id number
    def findByID(self, id):
        cursor = self.getCursor()
        sql = "SELECT * from student where id = %s"
        values = (id, )
        cursor.execute(sql, values)
        result = cursor.fetchone()
        returnvalue = self.convertToDictionary(result)
        self.closeAll()
        return returnvalue

    def update(self, id, student):
        cursor = self.getCursor()
        sql = "UPDATE student SET name = %s, age = %s where id = %s"
        values = (student.get("name"), student.get("age"), id)
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        return student
        print("Age updated.")


    def delete(self, id):
        cursor = self.getCursor()
        sql = "delete from student where id = %s"
        values = (id, )
        cursor.execute(sql, values)
        self.connection.commit()
        self.closeAll()
        print("Student deleted")

studentDAO = StudentDAO()