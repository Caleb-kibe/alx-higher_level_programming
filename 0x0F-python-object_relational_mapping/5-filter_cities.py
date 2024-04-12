#!/usr/bin/python3
"""This script takes in the name of a state and lists
all the cities of that state"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                          passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s", [sys.argv[4]])

    cities = cursor.fetchall()
    j = []
    for i in cities:
        j.append(i[1])
    print(", ".join(j))

    cursor.close()
    db.close()
