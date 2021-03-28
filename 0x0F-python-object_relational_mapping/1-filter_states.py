#!/usr/bin/python3
"""script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    user, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=database)
    db = db.cursor()
    db.execute("""SELECT * FROM states
    WHERE REGEXP_LIKE(name, '^N', 'c') ORDER BY id""")
    r = db.fetchall()
    for i in r:
        print(i)
