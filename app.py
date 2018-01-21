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

    def _get_task(self):
        self.task_existence = word.CheckingIfTaskExist()
        return word.get_task_id(self.task_existence, self.user_name, self.user_surname)

    def _process_task_description(self, task):
        descript_answer = word.get_user_yesno(info='Do you want to edit task description?: ')
        if descript_answer == 'no':
            pass
        elif descript_answer == 'yes':
            description = word.edit_description()
            query.update_description(description, task)

    def _process_task_note(self, task):
        note_answer = word.get_user_yesno(info='Do you want to edit task note?: ')
        if note_answer == 'no':
            pass
        elif note_answer == 'yes':
            text = word.edit_note()
            query.update_text_note(text, task)

    def _process_task_end(self, task):
        end_at_answer = word.get_user_yesno(info='Do you want to end the task?: ')
        if end_at_answer == 'no':
            pass
        elif end_at_answer == 'yes':
            end_at = word.add_end_at()
            query.update_end_at(end_at, task)
        
    def run(self):
        task = self._get_task()
        self._process_task_description(task)
        self._process_task_note(task)
        self._process_task_end(task)


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
        active_tasks = query.get_active_tasks(name=self.user_name, surname=self.user_surname)
        query.display_active_tasks(active_tasks)


class ShowFinishedTasksCommand:

    def __init__(self, user_name, user_surname):
        self.user_name = user_name
        self.user_surname = user_surname

    def run(self):
        finished_tasks = query.get_finished_tasks(name=self.user_name, surname=self.user_surname)
        query.display_finished_tasks(finished_tasks)


class DeleteTaskCommand:

    def __init__(self, user_name, user_surname):
        self.user_name = user_name
        self.user_surname = user_surname

    def run(self):
        task_existence = word.CheckingIfTaskExist()
        task_id = word.get_task_id_to_delete(task_existence, self.user_name, self.user_surname)
        query.delete_task(self.user_name, self.user_surname, task_id)


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
        ShowActiveTasksCommand(user_name, user_surname),
        ShowFinishedTasksCommand(user_name, user_surname),
        DeleteTaskCommand(user_name, user_surname)
    ]

    while True:
        run_menu(commands)










