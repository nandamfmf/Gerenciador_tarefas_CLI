# Gerenciador de Tarefas (CLI)

## Sobre o projeto

Aplicação de linha de comando, feita em Python, para gerenciar uma lista de tarefas pelo terminal.
É possível adicionar, listar, concluir, remover, filtrar por status e editar tarefas.
Cada tarefa tem **id**, **descrição**, **status** (pendente ou concluída) e **data de criação**.
As tarefas ficam salvas em um arquivo JSON local (`tarefas.json`) e continuam lá depois que o programa é fechado.

## Tecnologias

- **Python 3.8 ou superior** 
- Apenas a biblioteca padrão: `argparse` (comandos), `json` (armazenamento), `datetime`, `pathlib`, `os`, `unicodedata`
- **pytest** — somente para rodar os testes automatizados (opcional para usar o programa)

## Como instalar

Pré-requisito: ter o [Python](https://www.python.org/downloads/) instalado. Para conferir:

```bash
python --version      # no Linux/macOS pode ser: python3 --version
```

Passo a passo, do clone até rodar:

```bash
git clone https://github.com/nandamfmf/Gerenciador_tarefas_CLI
cd Gerenciador_tarefas_CLI
python tarefas.py --help
```

Não há nada para instalar: o programa não depende de bibliotecas externas.
No Linux/macOS, se `python` não existir, use `python3` em todos os comandos.

## Como usar

Formato geral: `python tarefas.py <comando> [argumentos]`

Se o comando for digitado sem argumentos (`python tarefas.py`), a ajuda é exibida.

| Comando | O que faz |
|---|---|
| `adicionar "descrição"` | Cria uma tarefa pendente |
| `listar` | Mostra todas as tarefas |
| `concluir ID` | Marca a tarefa como concluída |
| `remover ID` | Remove a tarefa |
| `filtrar pendente` / `filtrar concluida` | Mostra só as tarefas com aquele status (`concluída` com acento também funciona) |
| `editar ID "nova descrição"` | Troca a descrição da tarefa |
| `--help` (ou `<comando> --help`) | Lista os comandos disponíveis |

Use aspas quando a descrição tiver espaços.

### Exemplos

```text
$ python tarefas.py adicionar "Estudar Git"
Tarefa #1 adicionada.

$ python tarefas.py adicionar "Ler documentação do argparse"
Tarefa #2 adicionada.

$ python tarefas.py listar
[ ] #1 Estudar Git 10/10/2026
[ ] #2 Ler documentação do argparse 10/10/2026

$ python tarefas.py concluir 1
Tarefa #1 concluída.

$ python tarefas.py filtrar pendente
[ ] #2 Ler documentação do argparse 10/10/2026

$ python tarefas.py filtrar concluida
[x] #1 Estudar Git 10/10/2026

$ python tarefas.py editar 2 "Ler a documentação do pytest"
Tarefa #2 atualizada: Ler a documentação do pytest

$ python tarefas.py remover 1
Tarefa #1 removida.

$ python tarefas.py listar
[ ] #2 Ler a documentação do pytest 10/10/2026
```

Quando uma lista está vazia:

```text
$ python tarefas.py listar
Nenhuma tarefa cadastrada.
```

### Mensagens de erro

Os erros são escritos no terminal (stderr) e o programa termina com código diferente de 0.

```text
$ python tarefas.py concluir 99
Erro: Tarefa com ID 99 não encontrada.

$ python tarefas.py adicionar "   "
Erro: A descrição da tarefa não pode ser vazia.

$ python tarefas.py concluir abc
usage: tarefas.py concluir [-h] id
tarefas.py concluir: error: argument id: invalid int value: 'abc'

$ python tarefas.py voar
usage: tarefas.py [-h] {adicionar,listar,concluir,remover,filtrar,editar} ...
tarefas.py: error: argument comando: invalid choice: 'voar' (choose from 'adicionar', 'listar', 'concluir', 'remover', 'filtrar', 'editar')
```

### Onde ficam os dados

Em `tarefas.json`, na pasta do projeto (ou na pasta do executável, se você usar a versão empacotada) — não importa de qual diretório o comando seja executado.
O arquivo é criado automaticamente na primeira tarefa adicionada e não é versionado (está no `.gitignore`).

### Gerar um executável (opcional)

Dá para empacotar o programa em um único arquivo que roda **sem ter o Python instalado**, usando o [PyInstaller](https://pyinstaller.org/). O executável é gerado para o sistema operacional em que você roda o comando (para ter a versão de Windows, gere no Windows; para Linux, no Linux; para macOS, no macOS).

```bash
pip install pyinstaller
pyinstaller --onefile --name tarefas tarefas.py
```

O resultado fica na pasta `dist/`: `dist/tarefas.exe` (Windows) ou `dist/tarefas` (Linux/macOS). Para usar:

```bash
# Windows (PowerShell ou CMD)
dist\tarefas.exe adicionar "Estudar Git"
dist\tarefas.exe listar

# Linux / macOS
./dist/tarefas adicionar "Estudar Git"
./dist/tarefas listar
```

Os comandos são os mesmos da tabela acima; basta trocar `python tarefas.py` pelo caminho do executável.
Com o executável, o `tarefas.json` é criado **na mesma pasta do executável** (mantenha-o em um local onde você tenha permissão de escrita).
As pastas `build/` e `dist/` e o arquivo `tarefas.spec` são gerados pelo PyInstaller e já estão no `.gitignore`.

Se o Windows ou o antivírus reclamar de um executável desconhecido, é um comportamento comum em arquivos gerados pelo PyInstaller que não são assinados.

### Rodando os testes

```bash
pip install pytest
python -m pytest
```

## Como foi o desenvolvimento

>  Apesar de já ter feito um gerenciador de tarefas em outra linguagem de programação, foi minha primeira vez utilizando o Python para um projeto com programação orientada a objetos e conhecendo a sua bibloioteca argparse. De maneira geral, acredito que foi uma excelente escolha, porque o Pyhton é uma linguagem versátil e a cada projeto consigo aprender novos módulos úteis.

**Organização do código:**

```text
tarefas.py             # ponto de entrada: só chama main()
src/main.py            # entrada: lê os comandos (argparse), chama as regras e mostra as mensagens
src/tarefa.py          # regras: classe Tarefa e gerenciaTarefas (adicionar, concluir, remover, filtrar, editar)
src/armazenamento.py   # armazenamento: salvar e carregar o JSON
testes/                # testes automatizados (pytest)
```

**Decisões tomadas.**
- **JSON** para guardar as tarefas: legível, simples de depurar e suportado direto pela biblioteca padrão.
- **`argparse` com subcomandos**: gera a ajuda e valida os argumentos automaticamente.
- **Novo id = maior id existente + 1**, assim um id nunca é reaproveitado por engano depois de uma remoção no meio da lista.
- **Filtro tolerante**: `concluida`, `concluída` e `CONCLUÍDA` funcionam (acentos e maiúsculas são normalizados).
- **Caminho fixo do arquivo**: o `tarefas.json` fica na pasta do projeto, evitando que o programa leia/grave arquivos diferentes conforme a pasta em que foi executado.

**Dificuldades e como resolvi.**
- Garantir que o programa **não perdesse dados** com arquivo vazio ou inexistente.
- Fazer o filtro aceitar **acentos** (`concluída`) → função `normalizar_texto` com `unicodedata`.

## Próximos passos

- Melhorar e aumentar a quantidade de testes, aumentar a quantidade de funcionalidades para deixar o programa mais robusto, fazer um painel visual com front-end.
