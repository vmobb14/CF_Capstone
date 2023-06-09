import os
import csv
import copy
import bcrypt
from datetime import date
from getpass import getpass
import sqlite3
connection = sqlite3.connect('database.db')
cursor = connection.cursor()
# user_data = user_id, last_name, first_name, phone, email

# ------

def get_today():
    return date.today()

# ------

def leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

# ------

def num_days_in_month(month, year):
    months_31 = [1, 3, 5, 7, 8, 10, 12]
    months_30 = [4, 6, 9, 11]
    if month in months_31:
      return 31
    elif month in months_30:
      return 30
    else:
      if leap(year):
        return 29
      else:
        return 28

# ------

def get_hire_date():
    current_date = []
    raw_date = str(get_today())
    raw_date = raw_date.split('-')
    for field in raw_date:
        current_date.append(int(field))

    while True:
        os.system('clear')
        year_input = input('Enter year employee was hired (YYYY): ')
        if year_input.isnumeric() and len(year_input) == 4 and int(year_input) >= 1972:
            year_input = int(year_input)
        else:
            input('Invalid year input. Enter to try again.')
            continue

        month_input = input('Enter month employee was hired (MM): ')
        if month_input.isnumeric() and (len(month_input) == 1 or len(month_input) == 2) and (int(month_input) > 0 and int(month_input) < 13):
            month_input = int(month_input)
        else:
            input('Invalid month input. Enter to try again.')
            continue

        day_input = input('Enter day employee was hired (DD): ')
        if day_input.isnumeric() and (len(day_input) == 1 or len(day_input) == 2) and (int(day_input) > 0 and int(day_input) <= num_days_in_month(month_input, year_input)):
            day_input = int(day_input)
        else:
            input('Invalid day input. Enter to try again.')
            continue

        if date(year_input, month_input, day_input) > get_today():
            input('Invalid date input. Enter to try again.')
        else:
            return date(year_input, month_input, day_input)

# ------

def get_assessment_date():
    current_date = []
    raw_date = str(get_today())
    raw_date = raw_date.split('-')
    for field in raw_date:
        current_date.append(int(field))

    while True:
        os.system('clear')
        year_input = input('Enter year assessment was taken (YYYY): ')
        if year_input.isnumeric() and len(year_input) == 4 and int(year_input) >= 1972:
            year_input = int(year_input)
        else:
            input('Invalid year input. Enter to try again.')
            continue

        month_input = input('Enter month assessment was taken (MM): ')
        if month_input.isnumeric() and (len(month_input) == 1 or len(month_input) == 2) and (int(month_input) > 0 and int(month_input) < 13):
            month_input = int(month_input)
        else:
            input('Invalid month input. Enter to try again.')
            continue

        day_input = input('Enter day assessment was taken (DD): ')
        if day_input.isnumeric() and (len(day_input) == 1 or len(day_input) == 2) and (int(day_input) > 0 and int(day_input) <= num_days_in_month(month_input, year_input)):
            day_input = int(day_input)
        else:
            input('Invalid day input. Enter to try again.')
            continue

        if date(year_input, month_input, day_input) > get_today():
            input('Invalid date input. Enter to try again.')
        else:
            return date(year_input, month_input, day_input)

# ------

def import_date_taken(date_input):
    date_input = date_input.split('-')
    if len(date_input) == 3:
        if len(date_input[0]) == 4:
            if len(date_input[1]) == 2:
                if len(date_input[2]) == 2:
                    if date(int(date_input[0]), int(date_input[1]), int(date_input[2])) <= get_today():
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False

# ------

def none_check(update_input):
    if update_input == None or update_input == '':
        while True:
            os.system('clear')
            corrective_input = input('Invalid entry, input required.\nPlease try again: ')
            if corrective_input == '':
                continue
            else:
                os.system('clear')
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
        if id_input.isnumeric():
            data = cursor.execute(check, [int(id_input)]).fetchone()
            if data == None:
                os.system('clear')
                id_input = input('Invalid ID input. Please try again: ')
            else:
                os.system('clear')
                return int(id_input)
        else:
            os.system('clear')
            id_input = input('Invalid ID input. Please try again: ')

# ------

def import_id_users(id_input):
    check = '''\
SELECT *
FROM Users
WHERE user_id = ? AND active = 1;\
'''
    if id_input.isnumeric():
        data = cursor.execute(check, [int(id_input)]).fetchone()
        if data == None:
            return False
        else:
            return True
    else:
        return False

# ------

def good_id_managers(id_input):
    check = '''\
SELECT *
FROM Users
WHERE user_id = ? AND active = 1 AND manager = 1;\
'''
    while True:
        if id_input.isnumeric():
            data = cursor.execute(check, [int(id_input)]).fetchone()
            if data == None:
                os.system('clear')
                id_input = input('Invalid ID input. Please try again: ')
            else:
                os.system('clear')
                return int(id_input)
        else:
            os.system('clear')
            id_input = input('Invalid ID input. Please try again: ')

# ------

def good_id_competencies(id_input):
    check = '''\
SELECT *
FROM Competencies
WHERE competency_id = ? AND active = 1;\
'''
    while True:
        if id_input.isnumeric():
            data = cursor.execute(check, [int(id_input)]).fetchone()
            if data == None:
                os.system('clear')
                id_input = input('Invalid ID input. Please try again: ')
            else:
                os.system('clear')
                return int(id_input)
        else:
            os.system('clear')
            id_input = input('Invalid ID input. Please try again: ')

# ------

def good_id_assessments(id_input):
    check = '''\
SELECT *
FROM Assessments
WHERE assessment_id = ? AND active = 1;\
'''
    while True:
        if id_input.isnumeric():
            data = cursor.execute(check, [int(id_input)]).fetchone()
            if data == None:
                os.system('clear')
                id_input = input('Invalid ID input. Please try again: ')
            else:
                os.system('clear')
                return int(id_input)
        else:
            os.system('clear')
            id_input = input('Invalid ID input. Please try again: ')

# ------

def import_id_assessments(id_input):
    check = '''\
SELECT *
FROM Assessments
WHERE assessment_id = ? AND active = 1;\
'''
    if id_input.isnumeric():
        data = cursor.execute(check, [int(id_input)]).fetchone()
        if data == None:
            return False
        else:
            return True
    else:
        return False

# ------

def good_id_results(id_input):
    check = '''\
SELECT *
FROM Assessment_Results
WHERE result_id = ? AND active = 1;\
'''
    while True:
        if id_input.isnumeric():
            data = cursor.execute(check, [int(id_input)]).fetchone()
            if data == None:
                os.system('clear')
                id_input = input('Invalid ID input. Please try again: ')
            else:
                os.system('clear')
                return int(id_input)
        else:
            os.system('clear')
            id_input = input('Invalid ID input. Please try again: ')

# ------

def import_score(score_input):
    if score_input.isnumeric():
        if int(score_input) >= 0 and int(score_input) <= 4:
            return True
        else:
            return False
    else:
        return False

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
    while True:
        os.system('clear')
        password1 = getpass('Input desired password at least eight characters in length (input will not display): ')
        if len(password1) >= 8:
            break
        else:
            continue
    while True:
        os.system('clear')
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

def phone_check(phone_input):
    while True:
        phone_input = phone_input.split('-')
        if len(phone_input) == 3:
            if len(phone_input[0]) == 3:
                if len(phone_input[1]) == 3:
                    if len(phone_input[2]) == 4:
                        return '-'.join(phone_input)
                    else:
                        phone_input = input('Invalid input, please re-enter using XXX-XXX-XXXX formatting: ')
                else:
                    phone_input = input('Invalid input, please re-enter using XXX-XXX-XXXX formatting: ')
            else:
                phone_input = input('Invalid input, please re-enter using XXX-XXX-XXXX formatting: ')
        else:
            phone_input = input('Invalid input, please re-enter using XXX-XXX-XXXX formatting: ')

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
[6] Return
    ''')
        menu_input = input('>>')
        if menu_input.isnumeric():
            menu_input = int(menu_input)
            if menu_input in menu_options:
                if menu_input == 1:
                    update_input = input('Input legal surname: ')
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
                    update_input = input('Input desired ten digit phone number using XXX-XXX-XXXX formatting: ')
                    if update_input == '':
                        update_input = 'None'
                    else:
                        update_input = phone_check(update_input)
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

def competency_summary(user1):
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
        result_dict[competencies_tuple[index]] = avg(summary_dict[key])

    print(f'User Competency Summary for: {user1.last}, {user1.first} -- {user1.email}')
    for key in result_dict:
        print(f'{key[0]}, {key[1]}: {result_dict[key]}')
    input('\nEnter to continue.\n')
##
# ------
##
def user_menu(user1, user_data):
    main_menu = [1, 2, 3]
    while True:
        os.system('clear')
        print(f'''\
    **** Competency Tracking System ****  U

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
                competency_summary(user1)

        elif table_selection.isnumeric() and int(table_selection) == 4:
            break

        else:
            input('Invalid input. Enter to continue.\n')
##
# ------
# ------
##
def user_menu_m(user1, user_data):
    main_menu = [1, 2, 3]
    while True:
        os.system('clear')
        print(f'''\
    **** Competency Tracking System ****  M

Welcome, {user1.first}. Please make a selection:
[1] View User Info
[2] Update User Info
[3] View User Competency Summary
[4] Return
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
                competency_summary(user1)

        elif table_selection.isnumeric() and int(table_selection) == 4:
            break

        else:
            input('Invalid input. Enter to continue.\n')

# ------

def competency_levels():
    competency_query = '''\
SELECT name
FROM Competencies
WHERE competency_id = ?;\
'''
    data_query = '''\
SELECT r.user_id, u.last_name, u.first_name, r.score
FROM Assessment_Results r
JOIN Users u
ON r.user_id = u.user_id
JOIN Assessments a
ON r.assessment_id = a.assessment_id
WHERE a.competency_id = ? AND u.active = 1
ORDER BY u.last_name ASC;\
'''
    another_query = '''\
SELECT competency_id, name
FROM Competencies
ORDER BY competency_id ASC;\
'''
    columns = ['id', 'name']
    data = cursor.execute(another_query).fetchall()
    print(f'{columns[0]:<5}| {columns[1]}')
    for row in data:
        print(f'{row[0]:<5}| {row[1]}')
    id_search = input('\nInput competency ID to retrieve assessments for: ')
    good_id_competencies(id_search)

    data_tuple = cursor.execute(data_query, [id_search]).fetchall()
    competency_tuple = cursor.execute(competency_query, [id_search]).fetchone()
    users_dict = {}
    parsing_dict = {}
    result_dict = {}

    for row in data_tuple:
        print(row)
        if parsing_dict.get(row[0]):
            parsing_dict[row[0]].append(row[3])
        if not parsing_dict.get(row[0]):
            parsing_dict[row[0]] = [0]
            parsing_dict[row[0]].append(row[3])
        if not users_dict.get(row[0]):
            users_dict[row[0]] = (row[1], row[2])

    for key in parsing_dict:
        result_dict[users_dict[key]] = avg(parsing_dict[key])

    os.system('clear')
    print(f'Competency Levels Summary for: {competency_tuple[0]}')
    for key in result_dict:
        print(f'{key[0]}, {key[1]}: {result_dict[key]}')
    input('\nEnter to continue.\n')

# ------

def competency_summary_m():
    user_query = '''\
SELECT last_name, first_name, email
FROM Users
WHERE user_id = ?;\
'''
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
    another_query = '''\
SELECT user_id, last_name, first_name
FROM Users
ORDER BY user_id ASC;\
'''
    columns = ['id', 'last_name', 'first_name']
    data = cursor.execute(another_query).fetchall()
    print(f'{columns[0]:<5}| {columns[1]:<22}| {columns[2]}')
    for row in data:
        print(f'{row[0]:<5}| {row[1]:<22}| {row[2]}')
    id_search = input('\nInput user ID to retrieve scores for: ')
    good_id_users(id_search)

    competencies_tuple = cursor.execute(competencies_query).fetchall()
    scores_tuple = cursor.execute(scores_query, [id_search]).fetchall()
    user_info_tuple = cursor.execute(user_query, [id_search]).fetchone()
    parsing_dict = {}
    result_dict = {}

    for row in competencies_tuple:
        parsing_dict[row[0]] = [0]

    for row in scores_tuple:
        parsing_dict[row[0]].append(row[1])

    for index, key in enumerate(parsing_dict):
        result_dict[competencies_tuple[index]] = avg(parsing_dict[key])

    os.system('clear')
    print(f'User Competency Summary for: {user_info_tuple[0]}, {user_info_tuple[1]} -- {user_info_tuple[2]}')
    for key in result_dict:
        print(f'{key[0]}, {key[1]}: {result_dict[key]}')
    input('\nEnter to continue.\n')

# ------

def assessment_summary():
    user_query = '''\
SELECT last_name, first_name, email
FROM Users
WHERE user_id = ?;\
'''
    assessments_query = '''\
SELECT name
FROM Assessments
WHERE active = 1
ORDER BY assessment_id ASC;\
'''
    attempts_query = '''\
SELECT assessment_id
FROM Assessment_Results
WHERE user_id = ? AND active = 1
ORDER BY assessment_id ASC, result_id DESC;\
'''
    another_query = '''\
SELECT user_id, last_name, first_name
FROM Users
ORDER BY user_id ASC;\
'''
    columns = ['id', 'last_name', 'first_name']
    data = cursor.execute(another_query).fetchall()
    print(f'{columns[0]:<5}| {columns[1]:<22}| {columns[2]}')
    for row in data:
        print(f'{row[0]:<5}| {row[1]:<22}| {row[2]}')
    id_search = input('\nInput user ID to retrieve assessments for: ')
    good_id_users(id_search)

    assessments_tuple = cursor.execute(assessments_query).fetchall()
    attempts_tuple = cursor.execute(attempts_query, [id_search]).fetchall()
    user_info_tuple = cursor.execute(user_query, [id_search]).fetchone()
    assessments_list = [0]
    parsing_dict = {}
    result_dict = {}

    for row in assessments_tuple:
        assessments_list.append(row[0])

    for row in attempts_tuple:
        parsing_dict[row[0]] = 0

    for row in attempts_tuple:
        parsing_dict[row[0]] += 1

    for key in parsing_dict:
        result_dict[(key, assessments_list[key])] = parsing_dict[key]

    os.system('clear')
    print(f'User Assessment Summary for: {user_info_tuple[0]}, {user_info_tuple[1]} -- {user_info_tuple[2]}')
    for key in result_dict:
        print(f'{key[0]}, {key[1]}: {result_dict[key]}')
    input('\nEnter to continue.\n')

# ------

def results_summary():
    users_query = '''\
SELECT user_id, last_name, first_name
FROM Users;\
'''
    scores_query = '''\
SELECT r.user_id, r.score, a.name, r.date_taken, c.name
FROM Assessment_Results r
JOIN Users u
ON r.user_id = u.user_id
JOIN Assessments a
ON r.assessment_id = a.assessment_id
JOIN Competencies c
ON a.competency_id = c.competency_id
WHERE a.competency_id = ?
GROUP BY r.user_id
ORDER BY r.user_id, r.date_taken DESC;\
'''
    another_query = '''\
SELECT competency_id, name
FROM Competencies
ORDER BY competency_id ASC;\
'''
    columns = ['id', 'name']
    data = cursor.execute(another_query).fetchall()
    print(f'{columns[0]:<5}| {columns[1]}')
    for row in data:
        print(f'{row[0]:<5}| {row[1]}')
    id_input = input('\nInput competency ID to retrieve scores for: ')
    id_input = good_id_competencies(id_input)

    users_tuples = cursor.execute(users_query).fetchall()
    scores_tuples = cursor.execute(scores_query, [id_input]).fetchall()
    results_dict = {}
    competency_avg = [0]
    competency_name = ''
    blank_space = 'N\\A'
    for user in users_tuples:
        results_dict[user[0]] = [user[1], user[2]]

    for score in scores_tuples:
        competency_name = score[4]
        competency_avg.append(score[1])
        results_dict[score[0]].append(score[1])
        results_dict[score[0]].append(score[2])
        results_dict[score[0]].append(score[3])

    os.system('clear')
    for key in results_dict:
        temp_list = results_dict[key]
        if len(results_dict[key]) == 5:
            print(f'ID: {key:<5}| Last: {temp_list[0]:<22}| First: {temp_list[1]:<22}| Score: {temp_list[2]:<5}| Name: {temp_list[3]:<32}| Date: {temp_list[4]}')
        else:
            print(f'ID: {key:<5}| Last: {temp_list[0]:<22}| First: {temp_list[1]:<22}| Score: {blank_space:<5}| Name: {blank_space:<32}| Date: {blank_space}')
    print(f'\nCurrent company average for {competency_name} is {avg(competency_avg)}')
    input('\nEnter to continue.\n')
##
# ------
##
def manager_reports_menu():
    main_menu = [1, 2, 3, 4]
    while True:
        os.system('clear')
        print(f'''\
    **** Reports System ****  M

Please make a selection:
[1] Competency Levels Summary
[2] User Competency Summary
[3] User Assessment Summary
[4] Competency Results Summary
[5] Return
''')
        table_selection = input('>>')
        os.system('clear')
        if table_selection.isnumeric() and int(table_selection) in main_menu:
            table_selection = int(table_selection)
            if table_selection == 1:
                competency_levels()

            elif table_selection == 2:
                competency_summary_m()

            elif table_selection == 3:
                assessment_summary()

            elif table_selection == 4:
                results_summary()

        elif table_selection.isnumeric() and int(table_selection) == 5:
            break

        else:
            input('Invalid input. Enter to continue.\n')

# ------

def search_last():
    query = '''\
SELECT user_id, last_name, first_name, manager, phone, email, hire_date, date_entered
FROM Users
WHERE last_name LIKE ?
ORDER BY user_id ASC;\
'''
    name_input = input('Input surname to search for: ')
    name_input = f'%{name_input}%'
    columns = ['id', 'last_name', 'first_name', 'm', 'phone', 'email', 'hire_date', 'date_entered']
    data = cursor.execute(query, [name_input]).fetchall()
    os.system('clear')
    print(f'{columns[0]:<5}| {columns[1]:<22}| {columns[2]:<22}| {columns[3]:<3}| {columns[4]:<16}| {columns[5]:40}| {columns[6]:<12}| {columns[7]}')
    for row in data:
        print(f'{row[0]:<5}| {row[1]:<22}| {row[2]:<22}| {row[3]:<3}| {row[4]:<16}| {row[5]:40}| {row[6]:<12}| {row[7]}')
    input('\nEnter to continue.\n')

# ------

def search_first():
    query = '''\
SELECT user_id, last_name, first_name, manager, phone, email, hire_date, date_entered
FROM Users
WHERE first_name LIKE ?
ORDER BY user_id ASC;\
'''
    name_input = input('Input given name to search for: ')
    name_input = f'%{name_input}%'
    columns = ['id', 'last_name', 'first_name', 'm', 'phone', 'email', 'hire_date', 'date_entered']
    data = cursor.execute(query, [name_input]).fetchall()
    os.system('clear')
    print(f'{columns[0]:<5}| {columns[1]:<22}| {columns[2]:<22}| {columns[3]:<3}| {columns[4]:<16}| {columns[5]:40}| {columns[6]:<12}| {columns[7]}')
    for row in data:
        print(f'{row[0]:<5}| {row[1]:<22}| {row[2]:<22}| {row[3]:<3}| {row[4]:<16}| {row[5]:40}| {row[6]:<12}| {row[7]}')
    input('\nEnter to continue.\n')

# ------

def view_users():
    query = '''\
SELECT user_id, last_name, first_name, manager, phone, email, hire_date, date_entered
FROM Users
ORDER BY user_id ASC;\
'''
    columns = ['id', 'last_name', 'first_name', 'm', 'phone', 'email', 'hire_date', 'date_entered']
    data = cursor.execute(query).fetchall()
    print(f'{columns[0]:<5}| {columns[1]:<22}| {columns[2]:<22}| {columns[3]:<3}| {columns[4]:<16}| {columns[5]:40}| {columns[6]:<12}| {columns[7]}')
    for row in data:
        print(f'{row[0]:<5}| {row[1]:<22}| {row[2]:<22}| {row[3]:<3}| {row[4]:<16}| {row[5]:40}| {row[6]:<12}| {row[7]}')
    input('\nEnter to continue.\n')

# ------

def view_competencies():
    query = '''\
SELECT competency_id, name, date_entered
FROM Competencies
ORDER BY competency_id ASC;\
'''
    columns = ['id', 'name', 'date_entered']
    data = cursor.execute(query).fetchall()
    print(f'{columns[0]:<4}| {columns[1]:<32}| {columns[2]}')
    for row in data:
        print(f'{row[0]:<4}| {row[1]:<32}| {row[2]}')
    input('\nEnter to continue.\n')

# ------

def view_assessments():
    query = '''\
SELECT assessment_id, name, competency_id, date_entered
FROM Assessments
ORDER BY assessment_id ASC;\
'''
    columns = ['id', 'name', 'competency', 'date_entered']
    data = cursor.execute(query).fetchall()
    print(f'{columns[0]:<5}| {columns[1]:<32}| {columns[2]:<12}| {columns[3]}')
    for row in data:
        print(f'{row[0]:<5}| {row[1]:<32}| {row[2]:<12}| {row[3]}')
    input('\nEnter to continue.\n')

# ------

def view_results():
    query = '''\
SELECT result_id, user_id, assessment_id, score, date_taken, manager_id, date_entered
FROM Assessment_Results
ORDER BY result_id ASC;\
'''
    columns = ['id', 'user', 'assessment', 'score', 'date_taken', 'manager', 'date_entered']
    data = cursor.execute(query).fetchall()
    print(f'{columns[0]:<6}| {columns[1]:<6}| {columns[2]:<12}| {columns[3]:<7}| {columns[4]:<12}| {columns[5]:<9}| {columns[6]}')
    for row in data:
        if row[5]:
            print(f'{row[0]:<6}| {row[1]:<6}| {row[2]:<12}| {row[3]:<7}| {row[4]:<12}| {row[5]:<9}| {row[6]}')
        else:
            print(f'{row[0]:<6}| {row[1]:<6}| {row[2]:<12}| {row[3]:<7}| {row[4]:<12}|          | {row[6]}')
    input('\nEnter to continue.\n')
##
# ------
##
def manager_viewing_menu():
    main_menu = [1, 2, 3, 4, 5, 6]
    while True:
        os.system('clear')
        print(f'''\
    **** Viewing System ****  M

Please make a selection:
[1] Search active users by surname
[2] Search active users by given name
[3] View active users
[4] View active competencies
[5] View active assessments
[6] View all assessment results
[7] Return
''')
        table_selection = input('>>')
        os.system('clear')
        if table_selection.isnumeric() and int(table_selection) in main_menu:
            table_selection = int(table_selection)
            if table_selection == 1:
                search_last()

            elif table_selection == 2:
                search_first()

            elif table_selection == 3:
                view_users()

            elif table_selection == 4:
                view_competencies()

            elif table_selection == 5:
                view_assessments()

            elif table_selection == 6:
                view_results()

        elif table_selection.isnumeric() and int(table_selection) == 7:
            break

        else:
            input('Invalid input. Enter to continue.\n')

# ------

def add_user():
    os.system('clear')
    query = '''\
INSERT INTO Users (last_name, first_name, phone, email, password, hire_date, date_entered)
VALUES (?, ?, ?, ?, ?, ?, ?);\
'''
    create_info = []
    columns = ['last_name', 'first_name', 'phone', 'email', 'password', 'hire_date', 'date_entered']
    for index, column in enumerate(columns):
        os.system('clear')
        if index ==0:
            create_input = input(f'{column}: ')
            create_input = none_check(create_input)
            create_info.append(create_input.title())

        elif index ==1:
            create_input = input(f'{column}: ')
            create_input = none_check(create_input)
            create_info.append(create_input.title())

        elif index ==2:
            create_input = input(f'{column}: ')
            if create_input == '':
                create_input = 'None'
            else:
                create_input = phone_check(create_input)
            create_info.append(create_input)

        elif index ==3:
            create_input = create_email()
            create_info.append(create_input)

        elif index ==4:
            create_input = create_password()
            create_info.append(create_input)

        elif index ==5:
            create_input = get_hire_date()
            create_info.append(create_input)

        elif index ==6:
            create_input = get_today()
            create_info.append(create_input)

    os.system('clear')
    cursor.execute(query, create_info)
    connection.commit()
    print(f'{create_info[1]} {create_info[0]} data successfully added.\n')
    input('Enter to continue.\n')

# ------

def add_competency():
    os.system('clear')
    query = '''\
INSERT INTO Competencies (name, date_entered)
VALUES (?, ?);\
'''
    create_info = []
    columns = ['name', 'date_entered']
    for index, column in enumerate(columns):
        os.system('clear')
        if index ==0:
            create_input = input(f'{column}: ')
            create_input = none_check(create_input)
            create_info.append(create_input.title())

        elif index ==1:
            create_input = get_today()
            create_info.append(create_input)

    os.system('clear')
    cursor.execute(query, create_info)
    connection.commit()
    print(f'{create_info[0]} data successfully added.\n')
    input('Enter to continue.\n')

# ------

def add_assessment():
    os.system('clear')
    query = '''\
INSERT INTO Assessments (name, competency_id, date_entered)
VALUES (?, ?, ?);\
'''
    create_info = []
    columns = ['name', 'competency_id', 'date_entered']
    for index, column in enumerate(columns):
        os.system('clear')
        if index ==0:
            create_input = input(f'{column}: ')
            create_input = none_check(create_input)
            create_info.append(create_input.title())

        elif index ==1:
            create_input = int(input(f'{column}: '))
            create_input = good_id_competencies(create_input)
            create_info.append(create_input)

        elif index ==2:
            create_input = get_today()
            create_info.append(create_input)

    os.system('clear')
    cursor.execute(query, create_info)
    connection.commit()
    print(f'{create_info[0]} data successfully added.\n')
    input('Enter to continue.\n')

# ------

def add_result():
    os.system('clear')
    query = '''\
INSERT INTO Assessment_Results (user_id, assessment_id, score, date_taken, manager_id, date_entered)
VALUES (?, ?, ?, ?, ?, ?);\
'''
    create_info = []
    columns = ['user_id', 'assessment_id', 'score', 'date_taken', 'manager_id', 'date_entered']
    for index, column in enumerate(columns):
        os.system('clear')
        if index ==0:
            create_input = int(input(f'{column}: '))
            create_input = good_id_users(create_input)
            create_info.append(create_input)

        elif index ==1:
            create_input = int(input(f'{column}: '))
            create_input = good_id_assessments(create_input)
            create_info.append(create_input)

        elif index ==2:
            while True:
                os.system('clear')
                create_input = input(f'{column} (0-4): ')
                if create_input.isnumeric():
                    if int(create_input) >= 0 and int(create_input) <= 4:
                        create_info.append(int(create_input))
                        break
                    else:
                        input('Invalid score. Enter to input a score within 0-4.\n')
                else:
                    input('Invalid score. Enter to input a score within 0-4.\n')

        elif index ==3:
            create_input = get_assessment_date()
            create_info.append(create_input)

        elif index ==4:
            create_input = int(input(f'{column}: '))
            create_input = good_id_managers(create_input)
            create_info.append(create_input)

        elif index ==5:
            create_input = get_today()
            create_info.append(create_input)

    os.system('clear')
    cursor.execute(query, create_info)
    connection.commit()
    print('Result data successfully added.\n')
    input('Enter to continue.\n')
##
# ------
##
def manager_creation_menu():
    main_menu = [1, 2, 3, 4]
    while True:
        os.system('clear')
        print(f'''\
    **** Creation System ****  M

Please make a selection:
[1] Create user record
[2] Create competency record
[3] Create assessment record
[4] Create assessment result record
[5] Return
''')
        table_selection = input('>>')
        os.system('clear')
        if table_selection.isnumeric() and int(table_selection) in main_menu:
            table_selection = int(table_selection)
            if table_selection == 1:
                add_user()

            elif table_selection == 2:
                add_competency()

            elif table_selection == 3:
                add_assessment()

            elif table_selection == 4:
                add_result()

        elif table_selection.isnumeric() and int(table_selection) == 5:
            break

        else:
            input('Invalid input. Enter to continue.\n')

# ------

def update_user():
    pull_query = '''\
SELECT last_name, first_name, manager, phone, email, hire_date
FROM Users
WHERE user_id = ?;\
'''
    push_query = '''\
UPDATE Users
SET last_name = ?, first_name = ?, manager = ?, phone = ?, email = ?, hire_date = ?
WHERE user_id = ?;\
'''
    update_list = []
    columns = ['last_name', 'first_name', 'manager', 'phone', 'email', 'hire_date']

    id_input = input('Input user ID to update: ')
    id_input = good_id_users(id_input)
    pull_data = cursor.execute(pull_query, [id_input]).fetchone()
    for field in pull_data:
        update_list.append(field)

    update_menu = [1, 2, 3, 4, 5, 6, 7]
    while True:
        os.system('clear')
        print(f'''\
Select field to update:
[1] {columns[0]}: {update_list[0]}
[2] {columns[1]}: {update_list[1]}
[3] {columns[2]}: {update_list[2]}
[4] {columns[3]}: {update_list[3]}
[5] {columns[4]}: {update_list[4]}
[6] {columns[5]}: {update_list[5]}
[7] Commit changes
''')
        field_selection = input('>>')

        if field_selection.isnumeric() and int(field_selection) in update_menu:
            field_selection = int(field_selection)
            if field_selection == 1:
                os.system('clear')
                update_input = input(f'{columns[0]}: ')
                update_input = none_check(update_input)
                update_list.pop(0)
                update_list.insert(0, update_input.title())

            elif field_selection == 2:
                os.system('clear')
                update_input = input(f'{columns[1]}: ')
                update_input = none_check(update_input)
                update_list.pop(1)
                update_list.insert(1, update_input.title())

            elif field_selection == 3:
                os.system('clear')
                manager_values = [0, 1]
                update_input = input(f'{columns[2]} (1 or 0): ')
                if update_input.isnumeric() and int(update_input) in manager_values:
                    update_input = int(update_input)
                    update_list.pop(2)
                    update_list.insert(2, update_input)
                else:
                    input('Invalid input. Enter to return.')

            elif field_selection == 4:
                os.system('clear')
                update_input = input(f'{columns[3]}: ')
                if update_input == '':
                    update_input = 'None'
                else:
                    update_input = phone_check(update_input)
                update_list.pop(3)
                update_list.insert(3, update_input)

            elif field_selection == 5:
                os.system('clear')
                update_input = create_email()
                update_list.pop(4)
                update_list.insert(4, update_input)

            elif field_selection == 6:
                os.system('clear')
                update_input = get_hire_date()
                update_list.pop(5)
                update_list.append(update_input)

            elif field_selection == 7:
                update_list.append(id_input)
                cursor.execute(push_query, update_list)
                connection.commit()
                break
        else:
            input('Invalid input. Enter to try again.')

# ------

def update_competency():
    pull_query = '''\
SELECT name
FROM Competencies
WHERE competency_id = ?;\
'''
    push_query = '''\
UPDATE Competencies
SET name = ?
WHERE competency_id = ?;\
'''
    update_list = []
    id_input = input('Input competency ID to update: ')
    id_input = good_id_competencies(id_input)
    pull_data = cursor.execute(pull_query, [id_input]).fetchone()
    for field in pull_data:
        update_list.append(field)

    update_input = input(f'{update_list[0]}\nname: ')
    update_input = none_check(update_input)
    update_list.append(update_input.title())
    update_list.pop(0)

    update_list.append(id_input)
    cursor.execute(push_query, update_list)
    connection.commit()

# ------

def update_assessment():
    pull_query = '''\
SELECT name, competency_id
FROM Assessments
WHERE assessment_id = ?;\
'''
    push_query = '''\
UPDATE Assessments
SET name = ?, competency_id = ?
WHERE assessment_id = ?;\
'''
    update_list = []
    columns = ['name', 'competency_id']

    id_input = input('Input assessment ID to update: ')
    id_input = good_id_assessments(id_input)
    pull_data = cursor.execute(pull_query, [id_input]).fetchone()
    for field in pull_data:
        update_list.append(field)

    update_menu = [1, 2, 3]
    while True:
        os.system('clear')
        print(f'''\
Select field to update:
[1] {columns[0]}: {update_list[0]}
[2] {columns[1]}: {update_list[1]}
[3] Commit changes
''')
        field_selection = input('>>')

        if field_selection.isnumeric() and int(field_selection) in update_menu:
            field_selection = int(field_selection)
            if field_selection == 1:
                os.system('clear')
                update_input = input(f'{columns[0]}: ')
                update_input = none_check(update_input)
                update_list.pop(0)
                update_list.insert(0, update_input.title())

            elif field_selection == 2:
                os.system('clear')
                update_input = input(f'{columns[1]}: ')
                update_input = good_id_competencies(update_input)
                update_list.pop(1)
                update_list.append(update_input)

            elif field_selection == 3:
                update_list.append(id_input)
                cursor.execute(push_query, update_list)
                connection.commit()
                break
        else:
            input('Invalid input. Enter to try again.')

# ------

def update_result():
    pull_query = '''\
SELECT user_id, assessment_id, score, date_taken, manager_id
FROM Assessment_Results
WHERE result_id = ?;\
'''
    push_query = '''\
UPDATE Assessment_Results
SET user_id = ?, assessment_id = ?, score = ?, date_taken = ?, manager_id = ?
WHERE result_id = ?;\
'''
    update_list = []
    columns = ['user_id', 'assessment_id', 'score', 'date_taken', 'manager_id']

    id_input = input('Input result ID to update: ')
    id_input = good_id_results(id_input)
    pull_data = cursor.execute(pull_query, [id_input]).fetchone()
    for field in pull_data:
        update_list.append(field)

    update_menu = [1, 2, 3, 4, 5, 6]
    while True:
        os.system('clear')
        print(f'''\
Select field to update:
[1] {columns[0]}: {update_list[0]}
[2] {columns[1]}: {update_list[1]}
[3] {columns[2]}: {update_list[2]}
[4] {columns[3]}: {update_list[3]}
[5] {columns[4]}: {update_list[4]}
[6] Commit changes
''')
        field_selection = input('>>')

        if field_selection.isnumeric() and int(field_selection) in update_menu:
            field_selection = int(field_selection)
            if field_selection == 1:
                os.system('clear')
                update_input = input(f'{columns[0]}: ')
                update_input = good_id_users(update_input)
                update_list.pop(0)
                update_list.insert(0, update_input)

            elif field_selection == 2:
                os.system('clear')
                update_input = input(f'{columns[1]}: ')
                update_input = good_id_assessments(update_input)
                update_list.pop(1)
                update_list.insert(1, update_input)

            elif field_selection == 3:
                os.system('clear')
                update_input = input(f'{columns[2]}: ')
                if update_input.isnumeric():
                    if int(update_input) >= 0 and int(update_input) <= 4:
                        update_list.pop(2)
                        update_list.insert(2, int(update_input))
                        break
                    else:
                        input('Invalid score. Enter to input a score within 0-4.\n')
                else:
                    input('Invalid score. Enter to input a score within 0-4.\n')

            elif field_selection == 4:
                os.system('clear')
                update_input = get_assessment_date()
                update_list.pop(3)
                update_list.insert(3, update_input)

            elif field_selection == 5:
                os.system('clear')
                update_input = input(f'{columns[4]}: ')
                update_input = good_id_managers(update_input)
                update_list.pop(4)
                update_list.insert(4, update_input)

            elif field_selection == 6:
                update_list.append(id_input)
                cursor.execute(push_query, update_list)
                connection.commit()
                break
        else:
            input('Invalid input. Enter to try again.')
##
# ------
##
def manager_update_menu():
    main_menu = [1, 2, 3, 4]
    while True:
        os.system('clear')
        print(f'''\
    **** Updates System ****  M

Please make a selection:
[1] Update user
[2] Update competency
[3] Update assessment
[4] Update assessment
[5] Return
''')
        table_selection = input('>>')
        os.system('clear')
        if table_selection.isnumeric() and int(table_selection) in main_menu:
            table_selection = int(table_selection)
            if table_selection == 1:
                update_user()

            elif table_selection == 2:
                update_competency()

            elif table_selection == 3:
                update_assessment()

            elif table_selection == 4:
                update_result()

        elif table_selection.isnumeric() and int(table_selection) == 5:
            break

        else:
            input('Invalid input. Enter to continue.\n')

# ------

def deac_user(user1):
    os.system('clear')
    query = '''\
UPDATE Users
SET active = 0
WHERE user_id = ?;\
'''
    while True:
        deac_input = int(input('Input user ID to be deactivated: '))
        if deac_input != user1.id:
            deac_input = good_id_users(deac_input)
            break
        else:
            input('Cannot input own ID. Enter to try again.\n')

    cursor.execute(query, [deac_input])
    connection.commit()
    print(f'\nUser ID {deac_input} has been deactivated.')
    input('Enter to continue.\n')

# ------

def deac_competency():
    os.system('clear')
    query = '''\
UPDATE Competencies
SET active = 0
WHERE competency_id = ?;\
'''
    deac_input = int(input('Input competency ID to be deactivated: '))
    deac_input = good_id_competencies(deac_input)

    cursor.execute(query, [deac_input])
    connection.commit()
    print(f'\nCompetency ID {deac_input} has been deactivated.')
    input('Enter to continue.\n')

# ------

def deac_assessment():
    os.system('clear')
    query = '''\
UPDATE Assessments
SET active = 0
WHERE assessment_id = ?;\
'''
    deac_input = int(input('Input assessment ID to be deactivated: '))
    deac_input = good_id_assessments(deac_input)

    cursor.execute(query, [deac_input])
    connection.commit()
    print(f'\nAssessment ID {deac_input} has been deactivated.')
    input('Enter to continue.\n')

# ------

def del_result():
    os.system('clear')
    query = '''\
DELETE
FROM Assessment_Results
WHERE result_id = ?;\
'''
    del_input = int(input('Input result ID to be deleted: '))
    del_input = good_id_results(del_input)

    cursor.execute(query, [del_input])
    connection.commit()
    print(f'\nResult ID {del_input} has been deleted.')
    input('Enter to continue.\n')
##
# ------
##
def manager_deactivate_menu(user1):
    main_menu = [1, 2, 3, 4]
    while True:
        os.system('clear')
        print(f'''\
    **** Deactivation/Deletion System ****  M

Please make a selection:
[1] Deactivate user
[2] Deactivate competency
[3] Deactivate assessment
[4] Delete assessment result
[5] Return
''')
        table_selection = input('>>')
        os.system('clear')
        if table_selection.isnumeric() and int(table_selection) in main_menu:
            table_selection = int(table_selection)
            if table_selection == 1:
                deac_user(user1)

            elif table_selection == 2:
                deac_competency()

            elif table_selection == 3:
                deac_assessment()

            elif table_selection == 4:
                del_result()

        elif table_selection.isnumeric() and int(table_selection) == 5:
            break

        else:
            input('Invalid input. Enter to continue.\n')

# ------

def export_users():
    columns_query = '''\
PRAGMA table_info(Users);\
'''
    data_query = '''\
SELECT user_id, last_name, first_name, manager, phone, email, hire_date, date_entered, active
FROM USERS
ORDER BY active DESC, manager DESC, user_id ASC;\
'''
    clean_columns = []
    raw_columns = cursor.execute(columns_query).fetchall()
    for row in raw_columns:
        clean_columns.append(row[1])
    clean_columns.pop(6)

    data = cursor.execute(data_query).fetchall()

    with open('outfile.csv', 'wt') as outfile:
        wrtr = csv.writer(outfile)
        wrtr.writerow(clean_columns)
        wrtr.writerows(data)

# ------

def export_competencies():
    columns_query = '''\
PRAGMA table_info(Competencies);\
'''
    data_query = '''\
SELECT *
FROM Competencies
ORDER BY active DESC, competency_id ASC;\
'''
    clean_columns = []
    raw_columns = cursor.execute(columns_query).fetchall()
    for row in raw_columns:
        clean_columns.append(row[1])

    data = cursor.execute(data_query).fetchall()

    with open('outfile.csv', 'wt') as outfile:
        wrtr = csv.writer(outfile)
        wrtr.writerow(clean_columns)
        wrtr.writerows(data)

# ------

def export_assessments():
    columns_query = '''\
PRAGMA table_info(Assessments);\
'''
    data_query = '''\
SELECT *
FROM Assessments
ORDER BY active DESC, assessment_id ASC;\
'''
    clean_columns = []
    raw_columns = cursor.execute(columns_query).fetchall()
    for row in raw_columns:
        clean_columns.append(row[1])

    data = cursor.execute(data_query).fetchall()

    with open('outfile.csv', 'wt') as outfile:
        wrtr = csv.writer(outfile)
        wrtr.writerow(clean_columns)
        wrtr.writerows(data)

# ------

def export_results():
    columns_query = '''\
PRAGMA table_info(Assessment_Results);\
'''
    data_query = '''\
SELECT *
FROM Assessment_Results
ORDER BY result_id ASC;\
'''
    clean_columns = []
    raw_columns = cursor.execute(columns_query).fetchall()
    for row in raw_columns:
        clean_columns.append(row[1])

    data = cursor.execute(data_query).fetchall()

    with open('outfile.csv', 'wt') as outfile:
        wrtr = csv.writer(outfile)
        wrtr.writerow(clean_columns)
        wrtr.writerows(data)

# ------

def import_results():
    query = '''\
INSERT INTO Assessment_Results (user_id, assessment_id, score, date_taken, date_entered)
VALUES (?, ?, ?, ?, ?);\
'''
    with open('infile.csv', 'rt') as infile:
        rdr = csv.reader(infile)
        next(rdr)
        counter = 1
        for row in rdr:
            good_import = False
            good_import = import_id_users(row[0])
            good_import = import_id_assessments(row[1])
            good_import = import_score(row[2])
            good_import = import_date_taken(row[3])
            if good_import:
                row.append(get_today())
                cursor.execute(query, row)
                counter += 1
            else:
                input(f'Bad input, failure on line {counter}')
                return
##
# ------
##
def manager_export_menu():
    main_menu = [1, 2, 3, 4, 5]
    while True:
        os.system('clear')
        print(f'''\
    **** Import/Export System ****  M

Please make a selection:
[1] Export users
[2] Export competencies
[3] Export assessments
[4] Export assessment results
[5] Import assessment results
[6] Return
''')
        table_selection = input('>>')
        os.system('clear')
        if table_selection.isnumeric() and int(table_selection) in main_menu:
            table_selection = int(table_selection)
            if table_selection == 1:
                export_users()

            elif table_selection == 2:
                export_competencies()

            elif table_selection == 3:
                export_assessments()

            elif table_selection == 4:
                export_results()

            elif table_selection == 5:
                import_results()

        elif table_selection.isnumeric() and int(table_selection) == 6:
            break

        else:
            input('Invalid input. Enter to continue.\n')
##
# ------
##
def manager_menu(user1):
    main_menu = [1, 2, 3, 4, 5, 6]
    while True:
        os.system('clear')
        print(f'''\
    **** Competency Tracking System ****  M

Welcome, {user1.first}. Please make a selection:
[1] Reports
[2] View
[3] Create
[4] Update
[5] Deactivate/Delete
[6] Import/Export
[7] Return
''')
        table_selection = input('>>')
        os.system('clear')
        if table_selection.isnumeric() and int(table_selection) in main_menu:
            table_selection = int(table_selection)
            if table_selection == 1:
                manager_reports_menu()

            elif table_selection == 2:
                manager_viewing_menu()

            elif table_selection == 3:
                manager_creation_menu()

            elif table_selection == 4:
                manager_update_menu()

            elif table_selection == 5:
                manager_deactivate_menu(user1)

            elif table_selection == 6:
                manager_export_menu()

        elif table_selection.isnumeric() and int(table_selection) == 7:
            break

        else:
            input('Invalid input. Enter to continue.\n')
##
# ------
##
def manager_menu_selection(user1, user_data):
    main_menu = [1, 2]
    while True:
        os.system('clear')
        print(f'''\
    **** Manager Login System ****  M

Please make a selection:
[1] User Menus
[2] Manager Menus
[3] Logout
''')
        table_selection = input('>>')
        os.system('clear')
        if table_selection.isnumeric() and int(table_selection) in main_menu:
            table_selection = int(table_selection)
            if table_selection == 1:
                user_menu_m(user1, user_data)

            elif table_selection == 2:
                manager_menu(user1)

        elif table_selection.isnumeric() and int(table_selection) == 3:
            break

        else:
            input('Invalid input. Enter to continue.\n')
######
