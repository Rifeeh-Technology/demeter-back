import os
import psycopg2
import urllib.parse as urlparse

url = urlparse.urlparse("postgres://ljwxygsnwdvdmx:5118d6f02021ce9b56716856b698f06335f73407394d31358935bdfde268d185@ec2-52-205-61-230.compute-1.amazonaws.com:5432/d2r51ni4693fb1")
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port
print(dbname, user, password, host, port)


def get_db_connection():
    # conn = psycopg2.connect(host=os.environ['DB_SERVER'],
    #                         database=os.environ['DB_DATABASE'],
    #                         user=os.environ['DB_USERNAME'],
    #                         password=os.environ['DB_PASSWORD'])
    conn = psycopg2.connect(host=host,
                            database=dbname,
                            user=user,
                            password=password,
                            port=port)
    return conn


def insert(sql):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()