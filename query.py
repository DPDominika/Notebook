from datetime import date
# import logging
# logger = logging.getLogger('peewee')
# logger.setLevel(logging.DEBUG)
# logger.addHandler(logging.StreamHandler())
import models as model

def create_tables():
    model.db.connect()
    model.db.create_tables([model.User, model.Task, model.UserTask, model.Note], True)


def create_user(name, surname, email):
    model.User.create(name=name, surname=surname, email=email)


def show_emails():
    email_list = []
    for u in model.User.select():
        email_list.append(u.email)
    return email_list


def create_task(created_at, name, description, end_at):
    return model.Task.create(created_at=created_at, name=name, description=description, end_at=end_at)


def assign_task_to_user(task, user_name, user_surname):
    return model.User.get((model.User.name == user_name) & (model.User.surname == user_surname)).task_users.add(task)


def assign_task_user(name, surname, task_name):
    user = model.User.get((model.User.name == name) & (model.User.surname == surname))
    user.model.task_users.add(model.Task.get(model.Task.name == task_name))


def get_task_id(name, surname, task_name):
    query = (model.Task
            .select(model.Task, model.UserTask, model.User)
            .join(model.UserTask)
            .join(model.User)
            .group_by(model.Task)
            .having(model.Task.name == task_name)
            .having((model.User.name == name) & (model.User.surname == surname)))
    for q in query:
        return q.id


def show_all_tasks(name, surname):
    lp = 0
    user = model.User.get((model.User.name == name) & (model.User.surname == surname))
    for task in user.task_users:
        lp += 1
        print('lp. {0}, task id: {1}, name: {2}, description: {3}'.format(lp, task.id, task.name, task.description))


def show_active_tasks(name, surname):
    lp = 0
    query = (model.Task
            .select(model.Task, model.UserTask, model.User)
            .join(model.UserTask)
            .join(model.User)
            .where((model.User.name == name) & (model.User.surname == surname))
            .where(model.Task.end_at == None))
    for q in query:
        lp += 1
        print('lp. {0}, task id: {1}, name: {2}, description: {3}'.format(lp, q.id, q.name, q.description))


def show_finished_tasks(name, surname):
    lp = 0
    query = (model.Task
            .select(model.Task, model.UserTask, model.User)
            .join(model.UserTask)
            .join(model.User)
            .where((model.User.name == name) & (model.User.surname == surname))
            .where(model.Task.end_at != None))
    for q in query:
        lp += 1
        print('lp. {0}, task id: {1}, name: {2}, description: {3}'.format(lp, q.id, q.name, q.description))


def create_note_for_task(task_id, text):
    try:
        user_task = model.UserTask.get(
            task_id=task_id,
        )
    except model.DoesNotExist:
        return None

    return model.Note.create(
        task_id=user_task.task_id,
        text=text
    )


def update_description(new_description, task_id):
    return model.Task.update(description=new_description).where(model.Task.id == task_id).execute()


def update_text_note(text, task_id):
    return model.Note.update(text=text).where(model.Note.task_id == task_id).execute()


def update_end_at(end_at, task_id):
    return model.Task.update(end_at=end_at).where(model.Task.id == task_id).execute()


def contains(user_name, user_surname, task_id):
    query = (model.Task
            .select(model.Task, model.UserTask, model.User)
            .join(model.UserTask)
            .join(model.User)
            .where(model.Task.id == task_id)
            .where((model.User.name == user_name) & (model.User.surname == user_surname)))
    for q in query:
        print(q.id)


def delete_task(user_name, user_surname, task_id):
    query = (model.Task
            .select(model.Task, model.UserTask, model.User)
            .join(model.UserTask)
            .join(model.User)
            .where(model.Task.id == task_id)
            .where((model.User.name == user_name) & (model.User.surname == user_surname)))
    for q in query:
        return q.delete_instance()



