#!/usr/bin/python3
"""
This script takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
But is safe from SQL injection
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name=%s\
            ORDER BY id ASC", [sys.argv[4]])

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()
