#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa
"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    user, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=database)
    db.query("SELECT * FROM states ORDER BY id")
    r = db.store_result()
    t = r.fetch_row(maxrows=0)
    for i in t:
        print(i)
