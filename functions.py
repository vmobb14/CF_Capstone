import os
import copy
import bcrypt
from getpass import getpass
from datetime import date
import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()
# user_data = user_id, last_name, first_name, phone, email

# ------

# with open('Assessment_Results.sql') as outfile:
#     queries = outfile.read()
# cursor.executescript(queries)

# ------

def get_date():
    today_date = str(date.today())
    return today_date

# ------

def none_check(update_input):
    if update_input == None or update_input == '':
        while True:
            os.system('clear')
            corrective_input = input('Invalid entry, input required.\nPlease try again: ')
            if corrective_input == '':
                continue
            else:
                return update_input
    else:
        return update_input

# ------

def good_id_users(id_input):
    check = '''\
SELECT *
FROM Users
WHERE user_id = ? AND active = 1;\
'''

    while True:
        data = cursor.execute(check, [id_input]).fetchone()
        if data == None:
            os.system('clear')
            id_input = int(input('Invalid ID input. Please try again: '))
        else:
            return id_input

# ------

def login():
    query = '''\
SELECT *
FROM Users
WHERE email = ? AND active = 1;\
'''
    while True:
        os.system('clear')
        print('''\
**** Competency Tracking System Login ****
''')

        email_input = input('Email: ')
        user_info = cursor.execute(query, [email_input]).fetchone()
        if user_info == None:
            input('\nEmail not found. Enter to continue.')
            continue

        else:
            user_password = user_info[6].encode('utf-8')
            password_input = getpass('Password: ')
            # Encoding password
            input_bytes = password_input.encode('utf-8')
            # Checking password
            result = bcrypt.checkpw(input_bytes, user_password)

            if result:
                os.system('clear')
                user_data = []
                user_info = user_info[:6:]
                for field in user_info:
                    user_data.append(field)
                input('''\
**** ACCESS GRANTED ****

Enter to continue.\
''')
                return user_data

            else:
                os.system('clear')
                input('''\
**** ACCESS DENIED ****

Your input password was incorrect.
Enter to try again.
''')
                continue

# ------

def create_user_instance(user_data):
    if user_data[3] == 0:
        user1 = User(user_data)
        user_data.pop(3)
        return user1
    elif user_data[3] == 1:
        user1 = Manager(user_data)
        user_data.pop(3)
        return user1

# ------

def update_user_db(user_data, update_input, update_index):
    query = '''\
UPDATE Users
SET last_name = ?, first_name = ?, phone = ?, email = ?
WHERE user_id = ?;\
'''
    user_data.insert((update_index), update_input)
    user_data.pop(update_index+1)
    update_data = copy.deepcopy(user_data)
    update_data.append(user_data[0])
    update_data.pop(0)
    cursor.execute(query, update_data)
    connection.commit()
    return user_data

# ------

def update_user_pw(user_data, update_input):
    query = '''\
UPDATE Users
SET password = ?
WHERE user_id = ?;\
'''
    update_data = []
    update_data.append(update_input)
    update_data.append(user_data[0])
    cursor.execute(query, update_data)
    connection.commit()

# ------

def create_email():
    query = '''\
SELECT *
FROM Users
WHERE email = ? AND active = 1;\
'''
    while True:
        os.system('clear')
        email_input = input('Input new email: ')
        if '@' in email_input:
            split_email = email_input.split('@')
            if '.' in split_email[1]:
                check_data = cursor.execute(query, [email_input]).fetchone()
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
        password1 = getpass('Input desired password at least eight characters in length: ')
        if len(password1) >= 8:
            break
        else:
            continue
    while True:
        password2 = getpass('Re-input desired password: ')
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

class User():
    def __init__(self, user_data):
        self.id = user_data[0]
        self.last = user_data[1]
        self.first = user_data[2]
        self.manager = False
        self.phone = user_data[4]
        self.email = user_data[5]

class Manager():
    def __init__(self, user_data):
        self.id = user_data[0]
        self.last = user_data[1]
        self.first = user_data[2]
        self.manager = True
        self.phone = user_data[4]
        self.email = user_data[5]

# ------

def user_menu_view(user1):
    query = '''\
SELECT user_id, last_name, first_name, manager, phone, email, hire_date
FROM Users
WHERE user_id = ?;\
'''
    columns = ['user_id', 'last_name', 'first_name', 'manager', 'phone', 'email', 'hire_date']
    data = cursor.execute(query, [user1.id]).fetchone()
    for index, field in enumerate(columns):
        print(f'{field}: {data[index]}')
    input('\nEnter to continue.')

# ------

def user_menu_update(user1, user_data):
    menu_options = [1, 2, 3, 4, 5]
    while True:
        os.system('clear')
        print(f'''\
    Input item to update:
    [1] last_name: {user1.last}
    [2] first_name: {user1.first}
    [3] phone: {user1.phone}
    [4] email: {user1.email}
    [5] password
    [6] Return
    ''')
        menu_input = input('>>')
        if menu_input.isnumeric():
            menu_input = int(menu_input)
            if menu_input in menu_options:
                if menu_input == 1:
                    update_input = input('Input legal surname name: ')
                    update_input = none_check(update_input)
                    user_data = update_user_db(user_data, update_input, menu_input)

                elif menu_input == 2:
                    update_input = input('Input legal given name: ')
                    update_input = none_check(update_input)
                    user_data = update_user_db(user_data, update_input, menu_input)

                elif menu_input == 3:
                    update_input = input('Input desired ten digit phone number: ')
                    user_data = update_user_db(user_data, update_input, menu_input)

                elif menu_input == 4:
                    update_input = create_email()
                    user_data = update_user_db(user_data, update_input, menu_input)

                elif menu_input == 5:
                    update_input = create_password()
                    update_user_pw(user_data, update_input)

            elif menu_input == 6:
                break
            else:
                input('\nInvalid input. Enter to continue.')
        else:
            input('\nInvalid input. Enter to continue.')

# ------

def user_menu(user1, user_data):
    main_menu = [1, 2, 3]
    while True:
        os.system('clear')
        print('''\
    **** Competency Tracking System ****  (User)

Please make a selection:
[1] View User Info
[2] Update User Info
[3] View User Competency Summary
[4] Logout
''')
        table_selection = input('>>')
        os.system('clear')
        if table_selection.isnumeric() and int(table_selection) in main_menu:
            table_selection = int(table_selection)
            if table_selection == 1:
                user_menu_view(user1)
            elif table_selection == 2:
                user_menu_update(user1, user_data)
            elif table_selection == 3:
                input()

        elif table_selection.isnumeric() and int(table_selection) == 4:
            print('Goodbye!\n')
            break

        else:
            print('Invalid input, please try again.')
            input('Enter to continue.')

# ------

