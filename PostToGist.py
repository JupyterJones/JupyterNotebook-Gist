#Python file created to 'Post To Gist.github' with command line 
#!/usr/bin/python
"""
This posts to gist.github only NOT to database
Usage, to post fileExample.py:
python PostToGist.py fileExample.py
"""
import os, requests, sys, json
import GISTkey
username=GISTkey.gist()[0]
password=GISTkey.gist()[1]
filename = os.path.basename(sys.argv[1])
content=open(filename, 'r').read()
r = requests.post('https://api.github.com/gists',json.dumps({'files':{filename:{"content":content}}}),auth=requests.auth.HTTPBasicAuth(username, password)) 
#give the site time to respond
sleep(2)
print(r.json()['html_url'])