#!/usr/bin/python3
"""Script to list all cities from database `hbtn_0e_4_usa`"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.`id`, cities.`name`, states.`name` FROM cities "
                "JOIN states ON states.`id` = cities.`state_id` "
                "ORDER BY cities.`id` ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
