import sys
import psycopg2


conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

args = sys.argv[1].split(',')

if len(args) != 2:
   print('Input args like histogram.py 2,3 or 10,1000')
   exit()

#Select
cur.execute("SELECT word, count from tweetwordcount where count >= %s and count <= %s ORDER BY count DESC" % (args[0], args[1]))
conn.commit()

records = cur.fetchall()
for rec in records:
   print "word = ", rec[0],'\tcount = ', rec[1]

