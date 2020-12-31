import sys
import os
from github import Github

foldername = str(sys.argv[1])
path = os.environ.get('mp')         # add projects directory to the env vars
token = os.environ.get('gt')        # add github token to the env vars
_dir = path + foldername
username = "godwillmonthe"

user = Github(token).get_user()
repo = user.create_repo(foldername)

commands = [f'echo # {repo.name} >> README.md',
            'git init',
            f'git remote add origin https://github.com/{username}/{foldername}.git',
            'git add .',
            'git commit -m "Initial commit"',
            'git branch -M main',
            'git push -u origin main']

if foldername == str(sys.argv[1]):
    os.mkdir(_dir)
    os.chdir(_dir)

    for c in commands:
        os.system(c)

    print(f'{foldername} created locally')
    os.chdir(_dir)
    os.system('code .')

else:
    print("create <foldername>")
