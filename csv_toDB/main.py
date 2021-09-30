import psycopg2
import csv
import re




def copy_to_db(db_name, file):
    conn = psycopg2.connect("host='localhost' port='5432' dbname='testdb' user='test_user' password='PASS'")
    cur = conn.cursor()
    next(file)
    cur.copy_from(file, db_name, sep=';')
    conn.commit()
    conn.close()


with open(r"D:\Питон\Питон codewars\csv_toDB\energy.csv", 'r', encoding='utf-8') as f:
    copy_to_db('energy', f)


with open(r"D:\Питон\Питон codewars\csv_toDB\operators.csv", 'r', encoding='utf-8') as f:
    copy_to_db('operators', f)

with open(r"D:\Питон\Питон codewars\csv_toDB\periods.csv", 'r', encoding='utf-8') as f:
    copy_to_db('periods', f)

with open(r"D:\Питон\Питон codewars\csv_toDB\reasons.csv", 'r', encoding='utf-8') as f:
    copy_to_db('reasons', f)


