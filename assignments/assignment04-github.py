# Write a program that will read a file from a repository.
# The program should replace all the instances of the text "Andrew" with your name.
# The program should then commit the changes and push the file back to the repository (authorisation will be needed).
# Handup: push the program as assignment04-github.py to the assignments repository

# Author: Irene Kilgannon

import requests
from github import Github
from config import apikeys as cfg
g = Github(cfg['githubkey'])


repo = g.get_repo("IreneKilgannon/WSAA-coursework")
print(repo.clone_url)

#To view the contents of the repository
contents = repo.get_contents("")
for content in contents:
   print(content.path)

# To view the contents of the assignments directory
folder_path = "assignments"

contents = repo.get_contents(folder_path)
for file in contents:
   print(file.path)

#######
# To view the contents of a file inside a directory
file_path = "test.txt"

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
#

newContents = contentsOfFile.replace("Andrew", "Irene") + "more stuff \n"
print(newContents)
#
## update the content of the file on github
#gitHubResponse = repo.update_file(fileInfo.path, "updated by prog", newContents, fileInfo.sha)
#print(gitHubResponse)
# Starting basic, write a script to read a file and replace "Andrew" with my name
# https://www.geeksforgeeks.org/how-to-search-and-replace-text-in-a-file-in-python/
#
#search_text = "Andrew"
#
#replace_text = "Irene"
#
#with open ('andrew.txt', "r") as f:
#    data = f.read()
#    data = data.replace(search_text, replace_text)
#
## Write the changes to the file. 
#with open('andrew.txt', 'w') as f:
#    f.write(data)
#