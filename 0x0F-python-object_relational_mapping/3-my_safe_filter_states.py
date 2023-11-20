#!/usr/bin/python3
"""SQL injection safe query to get rows of states where name matches
an argument.
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states "
                "WHERE name = %s "
                "COLLATE 'latin1_general_cs' "
                "ORDER BY id ASC", (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
