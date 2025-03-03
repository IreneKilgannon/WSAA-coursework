# Write a program that will read a file from a repository.
# The program should replace all the instances of the text "Andrew" with your name.
# The program should then commit the changes and push the file back to the repository (authorisation will be needed).
# Handup: push the program as assignment04-github.py to the assignments repository

# Author: Irene Kilgannon

import requests
from github import Github
from config import apikeys as cfg
g = Github(cfg['githubkey'])


repo = g.get_repo("IreneKilgannon/wsaa-assignment4")
print(repo.clone_url)

# View the contents of the repository
contents = repo.get_contents("")
for content in contents:
   print(content.path)

#######
# View the contents of a file inside a directory
file_path = "text.txt"

file_info = repo.get_contents(file_path)

print(f"File Name: {file_info.name}")
print(f"Download URL: {file_info.download_url}")


# Download the url of the file
#fileInfo = repo.get_contents("assignments/text.txt")
url_of_file = file_info.download_url
print(url_of_file)
##
## Use download URL to make a http request to get the file
response = requests.get(url_of_file)
contentsOfFile = response.text
print(contentsOfFile)

# Replace Andrew with Irene
new_contents = contentsOfFile.replace("Andrew", "Irene")
#print(new_contents)

# Update the content of the file on Github
gitHubResponse = repo.update_file(file_info.path, "updated by prog", new_contents, file_info.sha)
print(gitHubResponse)
