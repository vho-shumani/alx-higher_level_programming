#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""
import sys
import MySQLdb

if __name__ == "__main__":
    try:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        db = MySQLdb.connect(host="localhost", user=username,
                             passwd=password, db=db_name, port=3306)
        cur = db.cursor()
        query = """SELECT cities.name
                   FROM cities INNER JOIN states
                   ON cities.state_id = states.id
                   WHERE states.name = %s
                   ORDER BY cities.id"""
        cur.execute(query, (state_name,))
        rows = cur.fetchall()
        for row in rows:
            print(row[0], end='')
            if row != rows[-1]:
                print(', ', end='')
        print()
        cur.close()
        db.close()
    except MySQLdb.Error as e:
        print('Error connecting to MySQL:', e)
