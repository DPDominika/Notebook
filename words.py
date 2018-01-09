from datetime import datetime
import models as model


def ask_about_account():
    answer = input('Do you have an account on DP-Note?: ')
    while answer.lower() != 'yes' and answer.lower() != 'no':
        print("Please, answer 'yes' or 'no'")
        answer = input('Do you have an account on DP-Note?: ')
    return answer


class UserRegistryDB:

    def contains(self, name, surname):
        return model.User.select().where((model.User.name == name) & (model.User.surname == surname))


# class UserRegistry:
#
#     def __init__(self, user_list):
#         self.user_list = user_list
#
#     def contains(self, surname):
#         users = [user for user in self.user_list if user.surname == surname]
#         return len(users) >= 1


def logon(user_registry):
    name = input('To logon write your name: ')
    surname = input('To logon write your surname: ')
    while not user_registry.contains(name, surname):
        print("The user don't exist")
        name = input('To logon write your name: ')
        surname = input('To logon write your surname: ')
    return {'name': name,
            'surname': surname}

# def logon(users_list):
#     name_surname = input('To logon write your name and surname: ')
#     while name_surname not in users_list:
#         print("The user don't exist")
#         name_surname = input('To logon write your name and surname: ')
#     return {'name_surname': name_surname.split(' ')}

def create_user(email_list):
    email = ''
    print('Create an account')
    name = input('name: ')
    surname = input('surname: ')
    email = input('email: ')
    while True:
        if email not in email_list:
            email_list.append(email)
            break
        elif email in email_list:
            email = input('Email already exist, write different email: ')
    return {'name': name,
            'surname': surname,
            'email': email}


def if_create_task():
    answer = input('Do you want to create a new task?: ')
    while answer.lower() != 'yes' and answer.lower() != 'no':
        print("Please, answer 'yes' or 'no'")
        answer = input('Do you want to create a new task?: ')
    return answer == 'yes'


def create_task():
    created_at = datetime.now()
    name = input('Create a task name: ')
    while name == '':
        name = input('Please, write a task name: ')
    if name != '':
        description = input('Create short description of your task (200 symbols): ')
    return {'created_at': created_at,
            'name': name,
            'description': description}


def create_task_note():
    text = input('Add a note for the task: ')
    return {'text': text}


def if_create_task_note():
    choice = None
    while choice != 'q' and choice != 'y':
        print("Choose 'y' to add note to your task or 'q' to quit the application")
        choice = input('Your choice: ')

    if choice == 'q':
        return 'the end'
    elif choice == 'y':
        return create_task_note()

#
# def activate_menu():
#     choice = None
#     while choice != 'q' and choice != 'y':
#         print("Choose 'y' to show a DP-Note menu or 'q' to quit the application")
#         choice = input('Your choice: ')
#
#     if choice == 'q':
#         return 'the end'
#     elif choice == 'y':
#         return menu_to_manage_tasks()


def menu_to_manage_tasks():
    choice = None
    while choice != '0':
        print(
        """
        0 - exit
        1 - create a new task
        2 - edit a task
        3 - show all my tasks
        4 - show active tasks
        5 - show finished tasks
        6 - delete a task
        """
        )
        choice = int(input('Choose number 0-4 to manage your tasks: '))

        if choice == 0:
            return 0
        elif int(choice) in range(1,7):
            return int(choice)




# print(activate_menu())
# print(logon(['Dominika Pleśniak', 'Jan Kowalski']))
# user = logon(['Dominika Pleśniak', 'Jan Kowalski'])
# print(user)
user_registry = UserRegistryDB()
print(logon(user_registry))
