# Useage: python GistIndex.py
# Prints an index of all posts in the database created by post2gist.py 
import sqlite3
def Index():
    database ='GISTstore/gist.db'
    conn = sqlite3.connect(database)
    c = conn.cursor()
    for row in c.execute('SELECT rowid, content, description, filename FROM gist \
        WHERE content = ?', ("Index",)):
            print row[0],row[1],row[2],row[3]
            

if __name__ == "__main__":
    Index() 