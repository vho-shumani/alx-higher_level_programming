#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name, port=3306)
    
        cur = db.cursor()
        cur.execute("SELECT * FROM states ORDER BY states.id")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print('Error connecting to MySQL:', e)
