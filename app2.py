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
