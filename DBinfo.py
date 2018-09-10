%%writefile dbINFO.py
"""
Gets tablename and column names from unknown database
just enter database name.
USAGE:
import dbINFO
database= "databases/history.db"
#database= "databases/sat2.db"
#database= "databases/ImageD.db"
dbINFO.dbinfo(database)
"""

import sqlite3
def dbinfo(database):
    conn = sqlite3.connect(database)
    conn.text_factory = str
    c = conn.cursor()
    res = c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    row = c.fetchone()
    row = str(row)
    row = row.replace("(","");row = row.replace(",)","")
    row = row.replace("'","")
    print row
    cur = c.execute("select * from "%s"" %  row)
    columns = [description[0] for description in cur.description]
    return columns

# if run directly
#database = "databases/history.db"
#dbinfo(database)
