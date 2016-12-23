import psycopg2


conn = psycopg2.connect(
    "dbname='mytestdb' user='zkan' host='localhost' password='12345'"
)
cur = conn.cursor()
cur.execute("""SELECT * FROM traffic""")
rows = cur.fetchall()
for each in rows:
    print(each)

cur.close()
conn.close()


conn = psycopg2.connect(
    "dbname='mytestdb' user='zkan' host='localhost' password='12345'"
)
cur = conn.cursor()
cur.execute("""insert into traffic (sessions) values (20)""")
conn.commit()
print(cur.statusmessage)
print(cur.query)

cur.close()
conn.close()


conn = psycopg2.connect(
    "dbname='mytestdb' user='zkan' host='localhost' password='12345'"
)
cur = conn.cursor()
cur.execute("""SELECT * FROM traffic""")
rows = cur.fetchall()
for each in rows:
    print(each)

cur.close()
conn.close()
