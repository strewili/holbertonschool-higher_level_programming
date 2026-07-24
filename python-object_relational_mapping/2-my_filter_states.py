#!/usr/bin/python3
"""Lists all states with a name matching the argument (NOT injection safe)."""
import sys
import MySQLdb


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306,
                          user=username, passwd=password,
                          db=db_name)
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY states.id ASC" \
        .format(state_name)
    cursor.execute(query)
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
