#!/usr/bin/python3
"""script that lists all cities from the database hbtn_0e_4_usa
"""
from sys import argv
import MySQLdb


if __name__ == '__main__':
    user, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(host="localhost", user=user,
                         passwd=password, db=database)
    db = db.cursor()
    db.execute("""SELECT cities.id, cities.name, states.name FROM cities
    JOIN states ON state_id=states.id ORDER BY cities.id""")
    r = db.fetchall()
    for i in r:
        print(i)
