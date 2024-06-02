#!/usr/bin/python3
"""script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
from mysql.connector import connect


def list_states(mysql username, mysql password, database_name):
    # connect to MySQL serverb

    db = MySQLdb.connect(
        host='localhost',
        port=3306
        user=username,
        passwd=password
        db=database
    )

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
