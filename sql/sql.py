import csv
import sqlite3

conn = sqlite3.connect('test.db')

c=conn.cursor()

c.execute("CREATE TABLE IF NOT EXISTS clients (fisrt_name, lastn_name, birth, email)")

with conn:
    c.execute("INSERT INTO clients values (?,?,?,?)", ('Kevin', 'Harnan', 22, 'kharnan@ucema.edu.ar'))
    c.execute("INSERT INTO clients values (?,?,?,?)", ('Alejo', 'Di Lelle', 24, 'adilelle@ucema.edu.ar'))
    c.execute("INSERT INTO clients values (?,?,?,?)", ('Ignacio', 'Freiria', 21, 'ifreirian@ucema.edu.ar'))
    c.execute("INSERT INTO clients values (?,?,?,?)", ('Catalina', 'Dapena', 20, 'cdapena@ucema.edu.ar'))

'''with conn:
    c.execute("DELETE FROM clients WHERE fist_name = 'Catalina'")'''
'''with conn:
    c.execute("UPDATE clients set birth = '21' WHERE fist_name = 'Catalina'")'''

c.execute("SELECT * FROM clients")

print(c.fetchall())

