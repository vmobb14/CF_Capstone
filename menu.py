import os
import bcrypt
from datetime import date
from functions import *
import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# query = '''\
# UPDATE Users
# SET email = 'tyler.gilroy.23@gmail.com'
# WHERE user_id = 1;\
# '''
# cursor.execute(query)
# connection.commit()

# while True:
#     user_info = login()
#     while True: