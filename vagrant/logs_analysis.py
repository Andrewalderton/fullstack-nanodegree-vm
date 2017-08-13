#!/usr/bin/env python3

import psycopg2

conn = psycopg2.connect("dbname=news")
cursor = conn.cursor()
cursor.execute(
    "SELECT title, count(*) FROM articles LEFT JOIN log ON log.path LIKE "
    "CONCAT ('%', articles.slug) GROUP BY articles.title ORDER BY count(*) "
    "DESC LIMIT 3;"
    )

results = cursor.fetchall()
print (results)
conn.close()
