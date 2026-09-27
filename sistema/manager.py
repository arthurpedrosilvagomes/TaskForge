from utilitarios.exceptions import TaskNotFound, EmptyTaskList, TaskAlreadyCreated

class Manager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        if task not in self.tasks:
            self.tasks[task] = "não"
        else:
            raise TaskAlreadyCreated()

    def show_task(self):
        if self.tasks:
            return self.tasks.items()
        else:
            raise EmptyTaskList()

    def task_done(self, task):
        if task in self.tasks:
            self.tasks[task] = "sim"
        else:
            raise TaskNotFound()

    def del_task(self, task):
        if task in self.tasks:
            del self.tasks[task]
        else:
            raise TaskNotFound()