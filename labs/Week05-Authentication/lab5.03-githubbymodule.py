from github import Github
from config import apikeys as cfg
import requests

apikey = cfg["githubkey"]

g = Github(apikey)

#for repo in g.get_user().get_repos():
#    print(repo.name)

# Modify the program to get the clone URL of a repository

repo = g.get_repo("IreneKilgannon/WSAA-coursework")
#print(repo.clone_url)

# To view the contents of the repository
#contents = repo.get_contents("")
#for content in contents:
#   print(content.path)

########
# To view the contents of the labs directory
folder_path = "labs"

contents = repo.get_contents(folder_path)
for file in contents:
   print(file.path)

#######
# To view the contents of a file inside a directory
file_path = "labs/text.txt"

file_info = repo.get_contents(file_path)

print(f"File Name: {file_info.name}")
print(f"Download URL: {file_info.download_url}")

#######
# To upload a file to a specific directory
#file_path = "labs/new_file.txt"
#repo.create_file(file_path, "Add new file", "Hello, GitHub!", branch="main")

# Download the url of the file
#fileInfo = repo.get_contents("test.txt")
#urloffile = fileInfo.download_url
##print(urloffile)
#
## Use download URL to make a http request tot he file
#response = requests.get(urloffile)
#contentsOfFile = response.text
##print(contentsOfFile)
#
#newContents = contentsOfFile + "more stuff \n"
##print(newContents)
#
## update the content of the file on github
#gitHubResponse = repo.update_file(fileInfo.path, "updated by prog", newContents, fileInfo.sha)
#print(gitHubResponse)