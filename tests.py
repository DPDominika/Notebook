import unittest
from words import (
    create_account, create_user,
    if_create_task, create_task,
    create_task_note, menu_to_manage_tasks
)

class TestWords(unittest.TestCase):

    def test_create_account(self):