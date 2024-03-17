#!/usr/bin/python3
"""Write a script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    host = 'localhost'
    port = 3306

    db = MySQLdb.connect(user=username, password=password,
                         database=dbName, host=host, port=port)
    result = db.cursor()
    result.execute("""SELECT * FROM states ORDER BY id""")
    row = result.fetchall()
    for row in rows:
        print(row)
    result.close()
    db.close()
