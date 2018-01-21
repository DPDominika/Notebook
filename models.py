from peewee import *
from playhouse.fields import ManyToManyField


db = SqliteDatabase('DP_note.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    name = CharField()
    surname = CharField()
    email = CharField(unique=True)


class Task(BaseModel):
    created_at = DateField()
    name = CharField()
    description = CharField(null=True)
    end_at = DateField(null=True)
    users = ManyToManyField(User, related_name='task_users')


UserTask = Task.users.get_through_model()


class Note(BaseModel):
    text = TextField()
    task = ForeignKeyField(Task, related_name='task_note')

