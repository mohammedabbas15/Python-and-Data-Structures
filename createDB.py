# we will connect to a data base
import sqlite3 as sql

conn = sql.connect('TestDB.db')
c = conn.cursor()

# create table - Clients
c.execute('''CREATE TABLE CLIENTS
             ([generated_id] INTEGER PRIMARY KEY,
             [Client_Name] text, [Country_ID] integer,
             [Date] date)''')
                
# create table - Country
c.execute('''CREATE TABLE COUNTRY
             ([generated_id] INTEGER PRIMARY KEY,
             [Country_ID] integer,
             [Country_Name] text)''')

# create table - Daily Status
c.execute('''CREATE TABLE DAILY_STATUS
             ([Client_Name] text, [Country_Name] text, [Date] date)''')

conn.commit()
