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
        task_word = word.create_task()
        task = query.create_task(task_word['created_at'], task_word['name'], task_word['description'], end_at=None)
        query.assign_task_to_user(task, user_name=self.user_name, user_surname=self.user_surname)
        text = word.create_task_note()
        task_id = query.get_task_id(self.user_name, self.user_surname, task_word['name'])
        query.create_note_for_task(task_id, text)


class EditTaskCommand:

    def __init__(self, user_name, user_surname):
        self.user_name = user_name
        self.user_surname = user_surname

    def run(self):
        task_existence = word.CheckingIfTaskExist()
        edited_task = word.edit_task(task_existence, self.user_name, self.user_surname)
        query.update_description(edited_task['description'], edited_task['task_id'])
        query.update_text_note(edited_task['text'], edited_task['task_id'])
        query.update_end_at(edited_task['end_at'], edited_task['task_id'])


class ShowTasksCommand:

    def __init__(self, user_name, user_surname):
        self.user_name = user_name
        self.user_surname = user_surname

    def run(self):
        query.show_all_tasks(self.user_name, self.user_surname)


class ShowActiveTasksCommand:

    def __init__(self, user_name, user_surname):
        self.user_name = user_name
        self.user_surname = user_surname

    def run(self):
        query.show_active_tasks(self.user_name, self.user_surname)


def run_menu(commands):
    command_index = word.menu_to_manage_tasks()
    command = commands[command_index]
    command.run()


def start_app():
    user_registry = word.UserRegistryDB()

    answer = word.ask_about_account()

    if answer == 'no':
        user = word.create_user(query.show_emails())
        query.create_user(user['name'], user['surname'], user['email'])
        user_name = user['name']
        user_surname = user['surname']

    elif answer == 'yes':
        log_details = word.logon(user_registry)
        user_name = log_details['name']
        user_surname = log_details['surname']

    commands = [
        ExitCommand(),
        NewTaskCommand(user_name, user_surname),
        EditTaskCommand(user_name, user_surname),
        ShowTasksCommand(user_name, user_surname),
        ShowActiveTasksCommand(user_name, user_surname)
    ]

    while True:
        run_menu(commands)

print(start_app())








