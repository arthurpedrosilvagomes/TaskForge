class TaskManagerError(Exception):
    pass

class EmptyTaskList(TaskManagerError):
    def __init__(self, message = "Lista de tarefas vazias"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return super().__str__()

class TaskNotFound(TaskManagerError):
    def __init__(self, message = "Tarefa não encontrada!"):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return super().__str__()