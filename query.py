from datetime import date
import models as model

def create_tables():
    model.db.connect()
    model.db.create_tables([model.User, model.Task, model.UserTask, model.Note], True)


def create_user(name, surname, email):
    model.User.create(name=name, surname=surname, email=email)


def create_task(created_at, name, description, end_at):
    return model.Task.create(created_at=created_at, name=name, description=description, end_at=end_at)


def assign_task_to_user(task, user_name, user_surname):
    # task = create_task(created_at, name, description, end_at)
    return model.User.get((model.User.name == user_name) & (model.User.surname == user_surname)).task_users.add(task)


def assign_task_user(name, surname, task_name):
    user = model.User.get((model.User.name == name) & (model.User.surname == surname))
    user.model.task_users.add(model.Task.get(model.Task.name == task_name))


# def show_all_tasks():
#     for t in model.Task.select():
#         return t.


def show_emails():
    email_list = []
    for u in model.User.select():
        email_list.append(u.email)
    return email_list

def show_users():
    users_list = []
    for u in model.User.select():
        user = u.name, u.surname
        user_join = ' '.join(user)
        users_list.append(user_join)
    return users_list

def select_user(name, surname):
    return model.User.select((model.User.name == name) & (model.User.surname == surname))

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