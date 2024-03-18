#!/usr/bin/python3
"""
Write a script that takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbName = sys.argv[3]
    host = 'localhost'
    port = 3306
    name = sys.argv[4]

    db = MySQLdb.connect(user=username, password=password,
                         database=dbName, host=host, port=port)
    result = db.cursor()
    result.execute("""SELECT cities.name FROM cities INNER JOIN states ON
                   states.id=cities.state_id WHERE states.name=%s""", (name, ))
    rows = result.fetchall()
    print(", ".join(map(lambda x: x[0], rows)))
    result.close()
    db.close()
