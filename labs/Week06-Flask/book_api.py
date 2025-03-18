# Create an application server that will perform a RESTful API.
# Allow the user to perform CRUD operations on an entity.
# Test using cURL.
# I have many sewing patterns! 
from flask import Flask, url_for, request

app = Flask(__name__)

@app.route('/')
def index():
        return "Hello World. This is my stash of sewing patterns."
    

@app.route('/patterns', methods = ['GET'])
def getall():
        return "get all"

@app.route('/patterns/<int:id>', methods = ['GET'])
def findbyid(id):
        return f"find by id: {id}"

# Create
@app.route('/patterns', methods = ['POST'])
def create():
        # Read json from the body
        jsonstring = request.json
        return f"create {jsonstring}"

# Update
@app.route('/patterns/<int:id>', methods = ['PUT'])
def update(id):
        # Read json from the body
        jsonstring = request.json
        return f"update {id} {jsonstring}"

# Delete
@app.route('/patterns/<int:id>', methods= ['DELETE'])
def delete(id):
        return f"Delete {id}"


if __name__ == "__main__":
    # When debug mode is on it automatically updates
    app.run(debug = True)
    













