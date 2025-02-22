# Write a module to interact with the API at https://andrewbeatty1.pythonanywhere.com/books

import requests

url = 'https://andrewbeatty1.pythonanywhere.com/books'


# Write a function to get the books from the URL
def read_books():
    response = requests.get(url)
    return response.json()

# Write a function for find by id
def find_book(id):
    geturl = url + "/" + str(id)
    response = requests.get(geturl)
    return response.json()

# Using json parameter with post, will en
# A function to create a book
def create_book(book):
    response = requests.post(url, json= book)
    return response.json()

def update_book(id, book):
   puturl = url + "/" + str(id)
   response = requests.put(puturl, json= book)
   return response.json()

def delete_book(id):
    deleteurl = url + "/" + str(id)
    response = requests.delete(deleteurl)
    return response.json()

if __name__ == "__main__":
    book = {'author': 'Author',
            'title': 'Test Title',
            'price' : 123}
    
    #print(read_books())
    #print(find_book(545))
    #print(create_book(book))
    #print(update_book(608, book))
    print(delete_book(608))

