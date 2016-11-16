import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
# CREATE DATBASE
cur.execute("DROP DATABASE IF EXISTS Tcount")
cur.execute("CREATE DATABASE  Tcount")
conn.commit()
#CREATE TABLES
cur.execute("DROP TABLE IF EXISTS Tweetwordcount;")
conn.commit()
cur.execute("CREATE TABLE Tweetwordcount ( word TEXT PRIMARY KEY NOT NULL, COUNT INT NOT NULL);")
#CREATE DUMMY RECORD
cur.execute("INSERT INTO Tweetwordcount (word,count) VALUES ('test',1)")
conn.commit()
#Select
cur.execute("SELECT word, count from Tweetwordcount")
records = cur.fetchall()
for rec in records:
   print "word = ", rec[0]
   print "count = ", rec[1], "\n"
conn.commit()
cur.execute("DELETE FROM Tweetwordcount where word = 'test'")
print "Tcount DB and Tweet Initialized"
cur.close()
conn.commit()
conn.close()
