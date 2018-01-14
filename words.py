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


def get_task_id(task_existence, user_name, user_surname):
    task_id = input('Write the task id of task you want to modify: ')
    while not task_existence.contains(user_name, user_surname, task_id):
        print("The task id don't exist")
        task_id = input('Write the id of your task: ')
    return task_id


def ask_about_edit_description():
    answer = input('Do you want to edit task description?: ')
    while answer.lower() != 'yes' and answer.lower() != 'no':
        print("Please, answer 'yes' or 'no'")
        answer = input('Do you want to edit task description?: ')
    return answer


def ask_about_edit_note():
    answer = input('Do you want to edit task note?: ')
    while answer.lower() != 'yes' and answer.lower() != 'no':
        print("Please, answer 'yes' or 'no'")
        answer = input('Do you want to edit task note?: ')
    return answer


def ask_about_end_at():
    answer = input('Do you want to end the task?: ')
    while answer.lower() != 'yes' and answer.lower() != 'no':
        print("Please, answer 'yes' or 'no'")
        answer = input('Do you want to end the task?: ')
    return answer


def edit_description():
    return input('Modify the task description: ')


def edit_note():
    return input('Modify the task note: ')


def add_end_at():
    return input('Add the end date: ')


def get_task_id_to_delete(task_existence, user_name, user_surname):
    task_id = input('Write the task id of task you want to delete: ')
    while not task_existence.contains(user_name, user_surname, task_id):
        print("The task id don't exist")
        task_id = input('Write the id of your task: ')
    return task_id

