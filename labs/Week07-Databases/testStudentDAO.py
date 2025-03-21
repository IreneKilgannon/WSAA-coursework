from StudentDAO import studentDAO

student = {"id": 3,
            'name': 'Andrew',
            'age' : 56
            }

student2 = {"id": 1,
        'name': 'Barry',
        'age' : 17
        }

#returnValue = studentDAO.create(student)
#returnValue = studentDAO.getAll()
#print(returnValue)
#returnValue = studentDAO.findByID(2)
#print("find By Id")
#print(returnValue)

returnValue = studentDAO.update(3, student)
print(returnValue)
#returnValue = studentDAO.delete(1)
#print(returnValue)
returnValue = studentDAO.getAll()
#print(returnValue)
