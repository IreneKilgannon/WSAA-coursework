# Write a program that will read a file from a repository.
# The program should replace all the instances of the text "Andrew" with your name.
# The program should then commit the changes and push the file back to the repository (authorisation will be needed).
# Handup: push the program as assignment04-github.py to the assignments repository.
# Author: Irene Kilgannon

import requests
from github import Github
from config import apikeys as cfg

# The file is text.txt in the wsaa-assignment4 repository.

# Authenticate with GitHub fine grained personal access token
g = Github(cfg['githubkey'])

# Get the repository, wsaa-assignment4
repo = g.get_repo("IreneKilgannon/wsaa-assignment4")

# Get the file from the repository
file_path = "text.txt"
file_info = repo.get_contents(file_path)

# Get the URL of the file
url_of_file = file_info.download_url

print(f"File Name: {file_info.name}")
print(f"Download URL: {url_of_file}")

# Make a HTTP GET request to get the contents of the file
response = requests.get(url_of_file)
contentsOfFile = response.text
print(contentsOfFile)

# Replace Andrew with Irene
new_contents = contentsOfFile.replace("Andrew", "Irene")
print(new_contents)

try:
    # Update the file and push to Github
    gitHubResponse = repo.update_file(file_info.path, "final test, updated by assignment4-github.py", new_contents, file_info.sha)
    print("File updated", gitHubResponse)
except Exception as e:
    print("File not updated", e)

# References
# Lab 5.03 using packages of Web Services and Applications
# Understanding Git commit SHAs https://graphite.dev/guides/git-hash
