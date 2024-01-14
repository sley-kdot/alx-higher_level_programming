#!/usr/bin/python3
""" a script that takes in the name of a state as an argument and lists
all cities of that state using the database hbtn_0e_4_usa"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM states\
                INNER JOIN cities ON states.id = cities.state_id\
                WHERE states.name=%s\
                ORDER BY cities.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    new_list = []
    for row in query_rows:
        new_list.append(", ".join(row))
    result = ", ".join(new_list)
    print(result)
    cur.close()
    db.close()
