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