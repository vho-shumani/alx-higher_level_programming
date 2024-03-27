#!/usr/bin/python3
""" displays all values in the
    states table of hbtn_0e_0_usa where name matches the argument."""
import sys
import MySQLdb

if __name__ == "__main__":
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        name = sys.argv[4]
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=db_name, port=3306)
        cur = db.cursor()
        query = "SELECT * FROM states WHERE name = %s ORDER BY id"
        cur.execute(query, (name,))
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print('Error connecting to MySQL:', e)
