import os
import bcrypt
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

# ------

def create_email():
    query = '''\
SELECT *
FROM Users
WHERE email = ?;\
'''
    while True:
        os.system('clear')
        email_input = input('Input user email: ')
        if '@' in email_input:
            split_email = email_input.split('@')
            if '.' in split_email[1]:
                check_data = cursor.execute(query, [email_input])
                if check_data == None:
                    return email_input
                else:
                    input('\nEmail exists in database. Please check database.')
            else:
                input('\nInvalid email input. Enter to try again.')
        else:
            input('\nInvalid email input. Enter to try again.')

# ------

def create_password():
    os.system('clear')
    while True:
        password1 = input('Input desired password at least eight characters in length: ')
        if len(password1) >= 8:
            break
        else:
            continue
    while True:
        password2 = input('Re-input your password: ')
        if password2 == password1:
            break
        else:
            continue

    # Convert password to array of bytes
    bytes = password1.encode('utf-8')
    # Generating salt
    salt = bcrypt.gensalt()
    # Hashing password
    hash = bcrypt.hashpw(bytes, salt)
    hash = hash.decode()
    return hash

# ------

def login():
    query = '''\
SELECT *
FROM Users
WHERE email = ?;\
'''
    while True:
        os.system('clear')
        print('''\
---- Competency Tracking Tool ----
''')

        email_input = input('Email: ')
        user_info = cursor.execute(query, [email_input]).fetchone()
        if user_info == None:
            continue

        else:
            user_password = user_info[6].encode('utf-8')
            password_input = input('Password: ')
            # Encoding password
            input_bytes = password_input.encode('utf-8')
            # Checking password
            result = bcrypt.checkpw(input_bytes, user_password)

            if result:
                os.system('clear')
                user_info_list = []
                user_info = user_info[:7:]
                for field in user_info:
                    user_info_list.append(field)
                input('''\
*** ACCESS GRANTED ***

Enter to continue.\
''')
                return user_info_list

            else:
                os.system('clear')
                input('''\
*** ACCESS DENIED ***

Your input password was incorrect.
Enter to try again.
''')
                continue

# ------

