import sys
import query as query
import words as word


class ExitCommand:

    def run(self):
        sys.exit(0)

class NewTaskCommand:

    def __init__(self, user_name, user_surname):
        self.user_name = user_name
        self.user_surname = user_surname

    def run(self):
        task = word.create_task()
        user_task = query.create_task(task['created_at'], task['name'], task['description'], end_at=None)
        user_task_2 = query.assign_task_to_user(user_task, user_name=self.user_name, user_surname=self.user_surname)
        word.if_create_task_note()
        word.create_task_note()

COMMANDS = [
    ExitCommand(),
    NewTaskCommand(user_name, user_surname)
    ]

def run_menu():
    command_index = word.menu_to_manage_tasks()
    command = COMMANDS[command_index]
    command.run()

def start_app():
    user_registry = word.UserRegistryDB()

    answer = word.ask_about_account()

    if answer == 'no':
        user = word.create_user(query.show_emails())
        user_1 = query.create_user(user['name'], user['surname'], user['email'])

    elif answer == 'yes':
        users_list = query.show_users()
        log_details = word.logon(users_list)
        user_name = log_details['name_surname'][0]
        user_surname = log_details['name_surname'][1]


    while True:
        run_menu()





    # if task_menu == 1:
    #     task = word.create_task()
    #     user_task = query.create_task(task['created_at'], task['name'], task['description'], end_at=None)
    #     user_task_2 = query.assign_task_to_user(user_task, user_name=user_name, user_surname=user_surname)
    #     word.if_create_task_note()
    #     word.create_task_note()
    # return user_task_2

print(start_app())

# def run_words():
#     account = word.create_account()
#     if account == 'no':
#         user = doit.create_user(query.show_emails())
#         user_1 = query.create_user(user['name'], user['surname'], user['email'])
#         task_menu = doit.activate_menu()
#     elif account == 'yes':
#         users_list = qu.show_users()
#         log_details = doit.logon(users_list)
#         user_name = log_details['name_surname'][0]
#         user_surname = log_details['name_surname'][1]
#         task_menu = doit.activate_menu()
#
#
#     if task_menu == 1:
#         task = doit.create_task()
#         user_task = qu.create_task(task['created_at'], task['name'], task['description'], end_at=None)
#         user_task_2 = qu.assign_task_to_user(user_task, user_name=user_name, user_surname=user_surname)
#         doit.if_create_task_note()
#         doit.create_task_note()
#     return user_task_2
#
#
# print(run_words())
