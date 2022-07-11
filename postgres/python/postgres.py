import os
import psycopg2
import urllib.parse as urlparse

url = urlparse.urlparse(os.environ.get("DEMETER_DB"))
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


def restore(sql):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute(sql)
    result = cur.fetchall()
    cur.close()
    conn.close()
    return result
