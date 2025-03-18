# a server for providing a RESTful api that allows CRUD operations
# on a book table
# Author: Andrew Beatty
from flask import Flask, url_for, request, redirect, abort, jsonify
from StudentDAO import studentDAO

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "This is the Student Database."
#get all


@app.route('/students')
def getAll():
    return jsonify(studentDAO.getAll())
#
## find By id
@app.route('/students/<int:id>', methods = ['GET'])
def findByID(id):
    return jsonify(studentDAO.findByID(id))
#
## create
## curl POST -d "{\"id\":\"test\", \"name\":\"Barry\", \"Age\":32}" http://127.0.0.1:5000/books
@app.route('/students', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)

    book = {
        "id": request.json["id"],
        "name": request.json["name"],
        "age": request.json["age"],
    }
    return jsonify(studentDAO.create(book))
#
#  
##update
## curl -X PUT -d "{\"Title\":\"new Title\", \"Price\":999}" -H "content-type:application/json" http://127.0.0.1:5000/books/1
@app.route('/students/<int:id>', methods=['PUT'])
def update_age(id):
    foundStudent = studentDAO.findByID(id)
    print (foundStudent)
    if foundStudent == {}:
        return jsonify({}), 404
    currentStudent = foundStudent
    if 'id' in request.json:
        currentStudent['id'] = request.json['id']
    if 'name' in request.json:
        currentStudent['name'] = request.json['name']
    if 'age' in request.json:
        currentStudent['age'] = request.json['age']
    studentDAO.update(currentStudent)

    return jsonify(currentStudent)
#

##delete
## curl -X DELETE http://127.0.0.1:5000/books/1
@app.route('/students/<int:id>', methods=['DELETE'])
def delete(id):
    studentDAO.delete(id)

    return jsonify({"done": True})
#

if __name__ == "__main__":
    app.run(debug=True)
