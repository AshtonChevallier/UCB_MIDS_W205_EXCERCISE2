import sys
import psycopg2

conn = psycopg2.connect(database="tcount", user="postgres", password="pass", host="localhost", port="5432")
cur = conn.cursor()

if len(sys.argv) == 1:
    cur.execute("SELECT word, count from tweetwordcount ORDER BY word asc")
    records = cur.fetchall()
    conn.commit()
elif len(sys.argv) == 2:
    cur.execute('''SELECT word, count from tweetwordcount where word = '%s';''' % (sys.argv[1]))
    records = cur.fetchall()
    conn.commit()
else:
    print('Too many args')
    exit()

print "Word\t\tCount\n"
for rec in records:
    if len(rec[0])<4:
        print rec[0], " \t\t",rec[1]
    elif len(rec[0]) > 6:
        print rec[0], "\t", rec[1]
    else:
        print rec[0], "\t\t", rec[1]
conn.commit()
cur.close()
conn.close()
