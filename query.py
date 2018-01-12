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
        print(lp, task.name, '-', task.description)


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
        print(lp, q.name,'-', q.description)


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


def show_emails():
    email_list = []
    for u in model.User.select():
        email_list.append(u.email)
    return email_list


def select_description(name, surname, task_name):
    query = (model.Task
            .select(model.Task, model.UserTask, model.User)
            .join(model.UserTask)
            .join(model.User)
            .where(model.Task.name == task_name)
            .where(((model.User.name == name) & (model.User.surname == surname))))
    for q in query:
        return {'description': q.description,
                'end_at': q.end_at}

def update_description(name, surname, task_name, new_description):
    old_description = select_description(name, surname, task_name)
    return model.Task.(description=new_description).where(model.Task.description == old_description['description'])




# def show_users():
#     users_list = []
#     for u in model.User.select():
#         user = u.name, u.surname
#         user_join = ' '.join(user)
#         users_list.append(user_join)
#     return users_list


# def select_user(name, surname):
#     return model.User.select((model.User.name == name) & (model.User.surname == surname))

# def create_note():


# def check_if_exist(email):
#     try:
#         mail = model.User.get(email=email)
#     except UserDoesNotExist:
#         return False






# create_user('Dominika', 'Pleśniak', 'dominika.plesniak@gmail.com')
# create_task(date(2017,12,26), 'shopping', 'christmas shopping', None)
# print(show_emails())
# print(check_if_exist(email='dkromka@gmail.com'))
# print(show_users())
# print(select_user('Dominika', 'Plesniak'))
# task = create_task(date(2017,1,11), 'new_task_2', 'description_2', None)
# assign_task_to_user(task, 'anna', 'libura')
# create_note_for_task(1, 'note for task nr 1 user 2')
# print(get_task_id('anna', 'libura', 'shopping'))
#print(get_task_users('shopping'))
# print(get_task_id('Katarzyna', 'Koba', 'shopping'))
# print(show_all_tasks('Dominika', 'Pleśniak'))
# print(show_active_tasks('Dominika', 'Pleśniak'))
# print(update_description('Dominika', 'Pleśniak', 'shopping'))
