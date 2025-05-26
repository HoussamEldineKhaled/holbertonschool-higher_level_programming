# get all states
import MySQLdb
import sys

if __name__ == "__main__":

    my_user = sys.argv[1]

    my_password = sys.argv[2]

    my_db = sys.argv[3]

    db = MySQLdb.connect(host='localhost', port=3306,
                         user=my_user, passwd=my_password, db=my_db)

    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
