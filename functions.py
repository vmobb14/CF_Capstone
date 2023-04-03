import os
from datetime import date
import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# ------

# with open('Assessment_Results.sql') as outfile:
#     queries = outfile.read()
# cursor.executescript(queries)

# ------

def get_date():
    today = str(date.today())
    return today