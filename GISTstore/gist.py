#%%writefile GISTstore/post2gist.py
import os
from time import sleep
import sqlite3
import os, requests, sys, json
import GISTkey
username=GISTkey.gistkey()[0]
password=GISTkey.gistkey()[1]
database ="GISTstore/gist.db"
conn = sqlite3.connect(database)
c = conn.cursor()
c.execute("""
CREATE VIRTUAL TABLE IF NOT EXISTS gist 
USING FTS4(content, description, filename);
""")
c.close()
conn.close()
conn = sqlite3.connect(database)
conn.text_factory=str 
c = conn.cursor()
filename = "countlines.py"
#PATH = "GISTstore/"
#content=open(PATH+filename, 'r').read()
content=open(filename, 'r').read()
r = requests.post('https://api.github.com/gists',json.dumps({'files':{filename:{"content":content}}}),auth=requests.auth.HTTPBasicAuth(username, password)) 
sleep(2)
Url= (r.json()['html_url'])
c.execute("INSERT INTO gist VALUES (?,?,?)", (content, Url, filename)) 
conn.commit()
title = "Index"
c.execute("INSERT INTO gist VALUES (?,?,?)", (title, Url, filename)) 
conn.commit()
for row in c.execute('SELECT rowid, content, description, filename FROM gist \
    WHERE filename MATCH ?', (filename,)):
        print Url,"\n",row[0],row[1],row[2],row[3]
c.close()
conn.close()