# TaskForge

TaskForge é um gerenciador de tarefas em linha de comando, desenvolvido em Python para facilitar o cadastro, a consulta, a marcação de conclusão e a exclusão de atividades diretamente no terminal.

O projeto foi pensado como uma aplicação simples, organizada por camadas, com separação entre interface do usuário, lógica de negócio e tratamento de erros. Ele funciona como uma ferramenta de produtividade básica para quem deseja controlar pequenas listas de tarefas de forma prática.

## Funcionalidades implementadas

A versão atual do projeto oferece as seguintes operações:

- Cadastro de tarefas com descrição informada pelo usuário.
- Listagem das tarefas cadastradas com seu status de conclusão.
- Marcação de uma tarefa como concluída.
- Exclusão de uma tarefa da lista.
- Validação de entradas numéricas para o menu e para a seleção de tarefas.
- Tratamento de casos quando a lista está vazia.
- Mensagens de erro para tarefas duplicadas e tarefas inexistentes.

## O que foi feito

O projeto foi estruturado em módulos para manter a organização e facilitar a manutenção do código:

- `main.py`: arquivo principal da aplicação. Ele instancia a interface e inicia o loop principal do programa.
- `interface/cli.py`: responsável pela interação com o usuário, apresentação do menu, leitura de entradas e chamadas às ações do sistema.
- `sistema/manager.py`: centraliza a lógica de gerenciamento das tarefas, armazenando e manipulando os dados.
- `utilitarios/exceptions.py`: define as exceções personalizadas do domínio da aplicação.

Além disso, o programa foi implementado com um fluxo de execução em terminal, em que o usuário escolhe opções em um menu e o sistema responde imediatamente com mensagens de confirmação ou erro.

## Como foi feito

### 1. Ponto de entrada

O arquivo `main.py` é muito simples e tem a função de inicializar a aplicação:

```python
from interface.cli import InterfaceCLI

taskmanager = InterfaceCLI()
taskmanager.run()
```

Esse trecho cria uma instância da classe `InterfaceCLI` e chama o método `run()`, que inicia o loop principal da aplicação.

### 2. Interface de linha de comando

A classe `InterfaceCLI` fica em `interface/cli.py` e é responsável por:

- exibir o menu do programa;
- capturar a entrada do usuário;
- converter valores para os tipos esperados;
- limpar o console conforme o sistema operacional;
- chamar os métodos adequados do gerenciador.

Ela também usa um dicionário chamado `menu_options`, no qual cada opção numérica do menu é associada a uma função específica:

```python
self.menu_options = {
    1: self.add_task,
    2: self.show_tasks,
    3: self.task_is_done,
    4: self.del_task
}
```

Isso torna a aplicação mais organizada e facilita a extensão do código.

A leitura das entradas é feita por um método reutilizável chamado `user_input()`, que tenta converter a informação digitada para o tipo solicitado e repete a pergunta caso o valor seja inválido.

### 3. Lógica de negócio do gerenciamento de tarefas

A lógica principal está em `sistema/manager.py`. A classe `Manager` mantém um dicionário em memória:

```python
self.tasks = {}
```

No sistema atual, cada tarefa é representada pela sua descrição como chave e pelo status como valor:

- `"não"` → tarefa ainda não concluída
- `"sim"` → tarefa concluída

A estrutura fica assim:

```python
self.tasks[task] = "não"
```

Os métodos implementados são:

- `add_task(task)`: cadastra uma nova tarefa se ela ainda não existir.
- `show_task()`: retorna as tarefas cadastradas ou dispara erro quando a lista estiver vazia.
- `task_done(task)`: marca a tarefa informada como concluída.
- `del_task(task)`: remove a tarefa escolhida.

### 4. Tratamento de exceções

O projeto usa exceções personalizadas em `utilitarios/exceptions.py` para deixar o código mais claro e a aplicação mais robusta.

As exceções definidas são:

- `TaskManagerError`: classe base para erros do domínio.
- `EmptyTaskList`: usada quando o usuário tenta listar tarefas sem que nenhuma tenha sido cadastrada.
- `TaskNotFound`: lançada quando uma tarefa informada não existe.
- `TaskAlreadyCreated`: lançada quando o usuário tenta criar uma tarefa duplicada.

Essas exceções ajudam a centralizar as mensagens de erro e tornam o fluxo da aplicação mais organizado.

## Como a aplicação funciona

O fluxo de uso do programa é simples:

1. O usuário executa o programa.
2. O menu é exibido com as opções disponíveis.
3. O usuário escolhe uma ação.
4. O sistema valida a entrada.
5. A operação específica é executada.
6. O programa retorna uma mensagem de confirmação ou informa o erro correspondente.

### Menu principal

```text
=== TASKFORGE - GERENCIADOR DE TAREFAS ===
[1] Cadastrar tarefa
[2] Mostrar tarefas cadastradas
[3] Marcar tarefa como concluída
[4] Apagar tarefa
[5] Sair
```

## Estrutura atual do projeto

```text
TaskForge/
├── main.py
├── README.md
├── interface/
│   ├── __init__.py
│   └── cli.py
├── sistema/
│   ├── __init__.py
│   └── manager.py
└── utilitarios/
    ├── __init__.py
    └── exceptions.py
```

## Como executar

Certifique-se de ter o Python instalado e, em seguida, execute:

```bash
python main.py
```

No Windows, também é possível usar:

```powershell
py main.py
```

## Observações da implementação atual

- As tarefas são armazenadas apenas em memória durante a execução do programa.
- Quando o programa é encerrado, a lista é perdida.
- A aplicação usa a descrição da tarefa como identificador principal.
- Como a descrição é convertida para minúsculas antes do cadastro, tarefas repetidas em diferentes capitalizações não são permitidas.
- A validação do menu e da seleção de tarefas é feita por conversão de tipo e repetição de entrada em caso de erro.

## Conclusão

O TaskForge é uma aplicação simples, funcional e bem organizada, que demonstra uma boa separação entre interface, lógica e tratamento de erros. Ele funciona como um exemplo claro de um sistema CLI em Python, com operações básicas para gestão de tarefas e estrutura pronta para expansão futura.
