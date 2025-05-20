# get all states
import MySQLdb
import sys

my_user = sys.argv[1]

my_password = sys.argv[2]

my_db = sys.argv[3]

db = MySQLdb.connect(host='localhost', user=my_user, passwd=my_password, db=my_db)

