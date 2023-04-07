import os
import bcrypt
from getpass import getpass
from datetime import date
from functions import *
import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()

# '$2b$12$5AY3Un1tAdlbax8SkkKOGeaBG/38apqs2A5xYqfN75zD08ABJs/AS'
# query = '''\
# UPDATE Users
# SET password = '$2b$12$5AY3Un1tAdlbax8SkkKOGeaBG/38apqs2A5xYqfN75zD08ABJs/AS'
# WHERE user_id = 2;\
# '''
# cursor.execute(query)
# connection.commit()

while True:
    user_data = login()
    while True:
        user1 = create_user_instance(user_data)
        if user1.manager:
            input('Success.')
            break
        else:
            user_menu(user1, user_data)
            break