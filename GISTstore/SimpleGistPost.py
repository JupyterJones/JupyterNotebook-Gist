#!/usr/bin/python
#USE: python SimpleGistPost.py FileToPost.py
import os, requests, sys, json
import GISTkey
from time import sleep
username=GISTkey.gistkey()[0]
password=GISTkey.gistkey()[1]
filename = os.path.basename(sys.argv[1])
content=open(filename, 'r').read()
r = requests.post('https://api.github.com/gists',json.dumps({'files':{filename:{"content":content}}}),auth=requests.auth.HTTPBasicAuth(username, password)) 
sleep(2)
print(r.json()['html_url'])