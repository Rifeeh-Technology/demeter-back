import os
import psycopg2
from psycopg2.extras import RealDictCursor
import urllib.parse as urlparse

url = urlparse.urlparse(os.environ['DEMETER_DB'])
dbname = url.path[1:]
user = url.username
password = url.password
host = url.hostname
port = url.port


def get_db_connection():
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


def get(sql):
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute(sql)
    return cur.fetchall()
