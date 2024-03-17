#!/usr/bin/python3
"""
Write a script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    host = 'localhost'
    port = 3306
    target = sys.argv[4]

    db = MySQLdb.connect(user=username, password=password,
                         database=dbName, host=host, port=port)
    result = db.cursor()
    result.execute("""SELECT * FROM states WHERE name LIKE BINARY '{}'
ORDER BY id""".format(target))
    rows = result.fetchall()
    for row in rows:
        print(row)
    result.close()
    db.close()
