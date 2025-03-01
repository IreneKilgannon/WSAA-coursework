from github import Github
from config import apikeys as cfg

apikey = cfg["githubkey"]

g = Github(apikey)

#for repo in g.get_user().get_repos():
#    print(repo.name)

# Modify the program to get the clone URL of a repository

repo = g.get_repo("IreneKilgannon/WSAA-coursework")
print(repo.clone_url)

contents = repo.get_contents("")
for content in contents:
   print(content.path)
   
#fileInfo = repo.get_contents("test.txt")
#urloffile = fileInfo.download_url
#print(urloffile)