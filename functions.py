import os
import copy
import bcrypt
from datetime import date
from getpass import getpass
import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()
# user_data = user_id, last_name, first_name, phone, email

# ------

# with open('Assessment_Results.sql') as outfile:
#     queries = outfile.read()
# cursor.executescript(queries)

# query = '''\
# DELETE FROM Assessment_Results;\
# '''
# cursor.execute(query)
# connection.commit()

# ------

def get_today():
    return date.today()

# ------

def get_date():
    os.system('clear')
    current_date = []
    raw_date = str(get_today())
    raw_date = raw_date.split('-')
    for field in raw_date:
        current_date.append(int(field))

    while True:
        day_input = int(input('Enter day assessment was taken (DD): '))
        month_input = int(input('Enter month assessment was taken (MM): '))
        year_input = int(input('Enter year assessment was taken (YYYY): '))

        if year_input > current_date[0] or year_input < 1973:
            input('Invalid year input. Enter to re-input date.\n')
        if year_input == current_date[0]:
            if month_input <= current_date[1]:
                if day_input > current_date[2]:
                    input('Invalid day input. Enter to re-input date.\n')
                    continue
            else:
                input('Invalid month input. Enter to re-input date.\n')
                continue
        return date(year_input, month_input, day_input)

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
        user_tuple = cursor.execute(query, [email_input]).fetchone()
        if user_tuple == None:
            input('\nEmail not found. Enter to continue.\n')
            continue

        else:
            user_password = user_tuple[6].encode('utf-8')
            password_input = getpass('Password: ')
            # Encoding password
            input_bytes = password_input.encode('utf-8')
            # Checking password
            result = bcrypt.checkpw(input_bytes, user_password)

            if result:
                os.system('clear')
                manager_check = False
                user_data = []
                for field in user_tuple[:6:]:
                    user_data.append(field)
                if user_tuple[3] == 1:
                    manager_check = True
                user_data.pop(3)
                input('''\
**** ACCESS GRANTED ****

Enter to continue.
''')
                return (manager_check, user_data)

            else:
                os.system('clear')
                input('''\
**** ACCESS DENIED ****

Your input password was incorrect.
Enter to try again.
''')
                continue

# ------

class User():
    def __init__(self, user_data):
        self.id = user_data[0]
        self.last = user_data[1]
        self.first = user_data[2]
        self.manager = False
        self.phone = user_data[3]
        self.email = user_data[4]

class Manager():
    def __init__(self, user_data):
        self.id = user_data[0]
        self.last = user_data[1]
        self.first = user_data[2]
        self.manager = True
        self.phone = user_data[3]
        self.email = user_data[4]

# ------

def create_user_instance(manager_check, user_data):
    if manager_check:
        user1 = Manager(user_data)
        return user1
    else:
        user1 = User(user_data)
        return user1

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
                    input('\nEmail exists in database. Enter to continue.\n')
            else:
                input('\nInvalid email input. Enter to try again.\n')
        else:
            input('\nInvalid email input. Enter to try again.\n')

# ------

def create_password():
    os.system('clear')
    while True:
        password1 = getpass('Input desired password at least eight characters in length (input will not display): ')
        if len(password1) >= 8:
            break
        else:
            continue
    while True:
        password2 = getpass('Re-input desired password (input will not display): ')
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

def avg(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        num_list.pop(0)
        return sum(num_list) / len(num_list)

# ------
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
    input('\nEnter to continue.\n')

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
    [6] Return (Updates profile)
    ''')
        menu_input = input('>>')
        if menu_input.isnumeric():
            menu_input = int(menu_input)
            if menu_input in menu_options:
                if menu_input == 1:
                    update_input = input('Input legal surname name: ')
                    update_input = none_check(update_input)
                    user_data = update_user_db(user_data, update_input, menu_input)
                    user1 = create_user_instance(user1.manager, user_data)
                    input('Field has been updated. Enter to continue.\n')

                elif menu_input == 2:
                    update_input = input('Input legal given name: ')
                    update_input = none_check(update_input)
                    user_data = update_user_db(user_data, update_input, menu_input)
                    user1 = create_user_instance(user1.manager, user_data)
                    input('Field has been updated. Enter to continue.\n')

                elif menu_input == 3:
                    update_input = input('Input desired ten digit phone number: ')
                    user_data = update_user_db(user_data, update_input, menu_input)
                    user1 = create_user_instance(user1.manager, user_data)
                    input('Field has been updated. Enter to continue.\n')

                elif menu_input == 4:
                    update_input = create_email()
                    user_data = update_user_db(user_data, update_input, menu_input)
                    user1 = create_user_instance(user1.manager, user_data)
                    input('Field has been updated. Enter to continue.\n')

                elif menu_input == 5:
                    update_input = create_password()
                    update_user_pw(user_data, update_input)
                    user1 = create_user_instance(user1.manager, user_data)
                    input('Field has been updated. Enter to continue.\n')

            elif menu_input == 6:
                return user1
            else:
                input('\nInvalid input. Enter to continue.\n')
        else:
            input('\nInvalid input. Enter to continue.\n')

# ------

def user_menu_summary(user1):
    competencies_query = '''\
SELECT competency_id, name
FROM Competencies
WHERE active = 1
ORDER BY competency_id ASC;\
'''
    scores_query = '''\
SELECT a.competency_id, r.score
FROM Assessment_Results r
JOIN Assessments a
ON r.assessment_id = a.assessment_id
WHERE r.user_id = ?
GROUP BY r.assessment_id
ORDER BY a.competency_id ASC, r.assessment_id ASC, r.date_taken DESC;\
'''
    competencies_tuple = cursor.execute(competencies_query).fetchall()
    scores_tuple = cursor.execute(scores_query, [user1.id]).fetchall()
    summary_dict = {}
    result_dict = {}
    for row in competencies_tuple:
        summary_dict[row[0]] = [0]

    for row in scores_tuple:
        summary_dict[row[0]].append(row[1])

    for index, key in enumerate(summary_dict):
        summary_dict[key] = avg(summary_dict[key])
        result_dict[f'{competencies_tuple[index]}'] = summary_dict[key]

    print(f'User Competency Summary for: {user1.last}, {user1.first} -- {user1.email}')
    for key in result_dict:
        print(f'{key}: {result_dict[key]}')
    input('\nEnter to continue.\n')

# ------

def user_menu(user1, user_data):
    main_menu = [1, 2, 3]
    while True:
        os.system('clear')
        print(f'''\
    **** Competency Tracking System **** U

Welcome, {user1.first}. Please make a selection:
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
                user1 = user_menu_update(user1, user_data)

            elif table_selection == 3:
                user_menu_summary(user1)

        elif table_selection.isnumeric() and int(table_selection) == 4:
            print('Goodbye!\n')
            break

        else:
            input('Invalid input. Enter to continue.\n')

# ------

