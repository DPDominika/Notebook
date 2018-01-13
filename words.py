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


def create_note():
    return input('Add a note for the task: ')


def create_task_note():
    choice = None
    while choice != 'm' and choice != 'y':
        print("Choose 'y' to add note to your task or 'm' to return to menu")
        choice = input('Your choice: ')

    if choice == 'm':
        return menu_to_manage_tasks()
    elif choice == 'y':
        return create_note()


def menu_to_manage_tasks():
    while True:
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
        choice = int(input('Choose number 0-6 to manage your tasks: '))

        if choice in range(0,7):
            return choice


class CheckingIfTaskExist:

    def contains(self, user_name, user_surname, task_id):
        query = (model.Task
            .select(model.Task, model.UserTask, model.User)
            .join(model.UserTask)
            .join(model.User)
            .where(model.Task.id == task_id)
            .where((model.User.name == user_name) & (model.User.surname == user_surname)))
        for q in query:
            return q.id


def edit_task(task_existence, user_name, user_surname):
    task_id = input('Write the task id of task you want to modify: ')
    while not task_existence.contains(user_name, user_surname, task_id):
        print("The task id don't exist")
        task_id = input('Write the id of your task: ')
    description = input('Modify the task description: ')
    text = input('Modify the task note: ')
    end_at = input('Add the end date: ')
    return {'task_id': task_id,
            'description': description,
            'text': text,
            'ecd_at': end_at}



# print(activate_menu())
# print(logon(['Dominika Pleśniak', 'Jan Kowalski']))
# user = logon(['Dominika Pleśniak', 'Jan Kowalski'])
# print(user)
# user_registry = UserRegistryDB()
# print(logon(user_registry))
# print(create_task())
# print(create_task_note())
# print(ask_create_task_note())
# print(menu_to_manage_tasks())