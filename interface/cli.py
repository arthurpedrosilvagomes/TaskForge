from sistema.manager import Manager
from utilitarios.exceptions import EmptyTaskList, TaskNotFound, TaskAlreadyCreated
import os

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

class InterfaceCLI:
    def __init__(self):
        self.manager = Manager()

        self.menu_options = {
            1: self.add_task,
            2: self.show_tasks,
            3: self.task_is_done,
            4: self.del_task
        }

    def add_task(self):
        try:
            new_task = self.user_input("Digite a tarefa: ").lower()
            self.manager.add_task(new_task)
            clear()
            print("Tarefa:", new_task, "criada com sucesso!")

        except TaskAlreadyCreated as e:
            clear()
            print(e)
    
    def show_tasks(self):
        try:
            task_list = list(self.manager.show_task())

            for i in range(len(task_list)):
                print(f"[{i + 1}] Tarefa: {task_list[i][0]} - Feito?: {task_list[i][1]}")
        
        except EmptyTaskList as e:
            print(e)
            return False

    def task_is_done(self):
        try:
            if self.show_tasks() == False:
                return

            users_choice = self.user_input("Escolha uma tarefa disponível: ", "Algo deu errado, tente novamente", str).lower()

            self.manager.task_done(users_choice)
            clear()
            print("Tarefa:", users_choice, "marcada como feita com sucesso!")

        except TaskNotFound as e:
            clear()
            print(e)

    def del_task(self):
        try:
            if self.show_tasks() == False:
                return

            users_choice = self.user_input("Escolha uma tarefa disponível: ", "Algo deu errado, tente novamente", str).lower()

            self.manager.del_task(users_choice)
            clear()
            print("Tarefa:", users_choice, "Deletada com sucesso!")

        except TaskNotFound as e:
            clear()
            print(e) 

    def show_menu(self):
        print("=== TASKFORGE - GERENCIADOR DE TAREFAS ===\n" \
              "[1] Cadastrar tarefa\n" \
              "[2] Mostrar tarefas cadastradas\n" \
              "[3] Marcar tarefa como concluída\n" \
              "[4] Apagar tarefa\n" \
              "[5] Sair" \
        )
        print("=" * 42)

    def user_input(self, input_msg: str = "", error_msg: str = "", input_type: type = str):
        while True:
            try:
                value = input_type(input(input_msg))
                return value
            except ValueError:
                print(error_msg)

    def run(self):
        while True:
            self.show_menu()

            users_choice = self.user_input("Digite um dos números acima: ", "Digite apenas números!", int)

            if users_choice == 5:
                break
            elif not (1 <= users_choice <= 4):
                clear()
                print("Digite apenas os números mostrados no menu!")
            else:
                clear()
                self.menu_options[users_choice]()