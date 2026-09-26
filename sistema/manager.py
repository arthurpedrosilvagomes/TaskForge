from utilitarios.exceptions import TaskNotFound, EmptyTaskList

class Manager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        self.tasks[task] = "não"

    def show_task(self):
        if self.tasks:
            return self.tasks.items()
        else:
            raise EmptyTaskList()

    def task_done(self, task):
        if self.tasks[task]:
            self.tasks[task] = "sim"
        else:
            raise TaskNotFound()

    def del_task(self, task):
        if self.tasks[task]:
            del self.tasks[task]
        else:
            raise TaskNotFound()