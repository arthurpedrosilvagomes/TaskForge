from sistema.manager import Manager
from utilitarios.exceptions import EmptyTaskList, TaskNotFound
import os

clear = lambda: os.system("cls" if os.name == "nt" else "clear")

class InterfaceCLI:
    def __init__(self):
        self.manager = Manager()

        self.menu_options = {
            1: self.add_task,
            2: self.show_tasks
        }

    def add_task(self):
        new_task = self.user_input("Digite a tarefa: ")
        self.manager.add_task(new_task)
    
    def show_tasks(self):
        try:
            for task, is_done in self.manager.show_task():
                print(f"Tarefa: {task} - feita: {is_done}")
        
        except EmptyTaskList as e:
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