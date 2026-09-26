# TaskForge

TaskForge é um gerenciador de tarefas executado no terminal. O programa permite cadastrar tarefas, consultar a lista, marcar uma tarefa como concluída e apagar uma tarefa.

## Funcionalidades

- Cadastrar uma tarefa informando sua descrição.
- Listar as tarefas com um número e o estado de conclusão (`sim` ou `não`).
- Marcar uma tarefa da lista como concluida.
- Apagar uma tarefa da lista.
- Validar entradas numericas do menu e das operacoes que selecionam uma tarefa.
- Informar quando a lista está vazia.

## Como foi construido

O projeto foi organizado em módulos Python com responsabilidades separadas:

1. `main.py` é o ponto de entrada. Ele instancia `InterfaceCLI` e inicia o loop da aplicação com `run()`.
2. `interface/cli.py` implementa a interação com o usuário. A classe `InterfaceCLI` apresenta o menu, coleta e converte entradas, mostra tarefas e direciona as operações para o gerenciador.
3. `sistema/manager.py` concentra as operações sobre as tarefas. A classe `Manager` cadastra, lista, conclui e apaga itens.
4. `utilitarios/exceptions.py` define exceções próprias para representar erros relacionados ao gerenciamento de tarefas.

Na interface, um dicionário associa cada opção do menu a um método. A camada de interface chama os métodos de `Manager`, sem implementar diretamente a manipulação da coleção. O gerenciador representa as tarefas em um dicionário Python: a descrição é a chave e o estado de conclusão é o valor (`"não"` ou `"sim"`).

## Estrutura dos modulos

| Arquivo ou pacote | Responsabilidade |
| --- | --- |
| `main.py` | Inicia a aplicação de linha de comando. |
| `interface/cli.py` | Exibe o menu, recebe entradas, imprime resultados e chama o gerenciador. Usa `os` para limpar o terminal de acordo com o sistema operacional. |
| `interface/__init__.py` | Inicializa o pacote `interface`; atualmente está vazio. |
| `sistema/manager.py` | Mantém o dicionário de tarefas e implementa as operações de gerenciamento. |
| `sistema/__init__.py` | Inicializa o pacote `sistema`; atualmente está vazio. |
| `utilitarios/exceptions.py` | Define `TaskManagerError`, `EmptyTaskList` e `TaskNotFound`. |
| `utilitarios/__init__.py` | Inicializa o pacote `utilitarios`; atualmente está vazio. |

### Excecoes

- `TaskManagerError` e a excecao-base do dominio.
- `EmptyTaskList` é usada quando se tenta obter tarefas sem haver itens cadastrados.
- `TaskNotFound` representa uma tarefa que não foi encontrada, embora o fluxo atual do gerenciador não converta todos os casos de chave inexistente para essa exceção.

## Tecnologias e dependencias

- **Python 3**: linguagem e ambiente de execução do projeto.
- **Biblioteca padrao `os`**: usada para escolher o comando de limpeza do terminal (`cls` no Windows e `clear` em outros sistemas).
- **Modulos locais**: `interface`, `sistema` e `utilitarios`, importados entre si para separar apresentacao, logica de tarefas e excecoes.
- **Pacotes externos**: nenhum identificado na implementacao atual.

## Como executar

Com o Python 3 instalado, abra um terminal na pasta do projeto e execute:

```bash
python main.py
```

No Windows, também pode ser necessário usar:

```powershell
py main.py
```

Use as opções de 1 a 4 para gerenciar tarefas e a opção 5 para sair.

## Limites atuais

- As tarefas ficam somente na memória do processo. Ao encerrar o programa, a lista é perdida.
- Não há armazenamento em arquivo ou banco de dados, nem sincronização entre execuções.
- A seleção é feita pela posição exibida na listagem; entradas numéricas fora do intervalo não possuem tratamento específico.
- A descrição da tarefa é usada como chave do dicionário, portanto descrições repetidas substituem o estado associado a essa chave.
