# Write a program that will read a file from a repository.
# The program should replace all the instances of the text "Andrew" with your name.
# The program should then commit the changes and push the file back to the repository (authorisation will be needed).
# Author: Irene Kilgannon



# Starting basic, write a script to read a file and replace "Andrew" with my name
# https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/

search_text = "Andrew"

replace_text = "Irene"

with open ('andrew.txt', "r") as f:
    data = f.read()
    data = data.replace(search_text, replace_text)

# Write the changes to the file. 
with open('andrew.txt', 'w') as f:
    f.write(data)

# to read a file from a repository.
# Using PyGitHub 

from github import Github
from config import apikeys as cfg

g = Github(cfg['githubkey'])

# Get the authenticated user
#user = g.get_user()
#print(user.name)

# Get all repos by the user
#for repo in g.get_user().get_repos():
#    print(repo.name)

# Create a new file
repo = g.get_repo("IreneKilgannon/PythonPractice")
#repo.create_file("new_file.txt", "Initial commit", "Hello, GitHub!")


# Update a file, this overwrites the existing content in the file
file = repo.get_contents("new_file.txt")
repo.update_file(file.path, "Updating file", "New content here", file.sha)
print("File updated successfully!")

g.close()