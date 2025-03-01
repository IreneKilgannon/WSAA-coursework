from github import Github
from config import apikeys as cfg
import requests

apikey = cfg["githubkey"]

g = Github(apikey)

#for repo in g.get_user().get_repos():
#    print(repo.name)

# Modify the program to get the clone URL of a repository

repo = g.get_repo("IreneKilgannon/WSAA-coursework")
print(repo.clone_url)

folder_path = "labs"

# To view the contents of the labs directory in the repository
contents = repo.get_contents(folder_path)
for file in contents:
   print(file.path)
