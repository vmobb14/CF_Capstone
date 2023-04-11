from functions import *

# '$2b$12$5AY3Un1tAdlbax8SkkKOGeaBG/38apqs2A5xYqfN75zD08ABJs/AS'
# query = '''\
# UPDATE Users
# SET password = '$2b$12$5AY3Un1tAdlbax8SkkKOGeaBG/38apqs2A5xYqfN75zD08ABJs/AS'
# WHERE user_id = 2;\
# '''
# cursor.execute(query)
# connection.commit()

def app_exe():
    while True:
        login_tuple = login()
        manager_check = login_tuple[0]
        user_data = copy.deepcopy(login_tuple[1])
        while True:
            user1 = create_user_instance(manager_check, user_data)
            if user1.manager:
                manager_menu_selection(user1, user_data)
                break
            else:
                user_menu(user1, user_data)
                break