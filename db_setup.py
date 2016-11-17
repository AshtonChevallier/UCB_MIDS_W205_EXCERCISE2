import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT 
conn = psycopg2.connect(database="postgres", user="postgres", password="pass", host="localhost", port="5432")

conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = conn.cursor()
# CREATE DATBASE
cur.execute("DROP DATABASE IF EXISTS Tcount;")
cur.execute("CREATE DATABASE  Tcount;")
conn.commit()
conn.close()

#CREATE TABLES
conn = psycopg2.connect(database='tcount',user='postgres',password='pass',host='localhost',port='5432')
cur = conn.cursor()
cur.execute("DROP TABLE IF EXISTS Tweetwordcount;")
conn.commit()
cur.execute("CREATE TABLE Tweetwordcount ( word TEXT PRIMARY KEY NOT NULL, COUNT INT NOT NULL);")
print "Tcount DB and Tweet Initialized"
cur.close()
conn.commit()
conn.close()
