#!/usr/bin/python3


import MySQLdb
from sys import argv

'''
a script that lists all states
from the database
'''
if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """
    user, password, database = argv[1], argv[2], argv[3]
    db = MySQLdb.connect(
        host="localhost", port=3306, user=user,
        password=password, database=database, charset="utf8")
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    db.close()
