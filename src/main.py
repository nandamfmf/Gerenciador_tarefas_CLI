import argparse
from datetime import datetime
from src.tarefa import Tarefa, gerenciaTarefas
from src.armazenamento import salvar_arquivo, carregar_arquivo

def main():

    # O gerenciador é um objeto criado a partir da classe gerenciaTarefas, que contém a lista de tarefas e os métodos para manipulá-las.
    gerenciador = gerenciaTarefas()
    lista_tarefas_carregadas = carregar_arquivo()
    gerenciador.lista_tarefas = lista_tarefas_carregadas

    # O parser é uma instância do módulo argparse responsável por ler e interpretar os argumentos passados na linha de comando.
    parser = argparse.ArgumentParser(description="Gerenciador de Tarefas CLI")
    subparsers = parser.add_subparsers(dest="comando", help="Comandos disponíveis")

    parser_adicionar = subparsers.add_parser("adicionar", help="Adicionar uma nova tarefa com descrição e data de criação")
    parser_adicionar.add_argument("descricao", type=str, help="Descrição da tarefa")

    parser_listar = subparsers.add_parser("listar", help="Listar todas as tarefas")

    parser_concluir = subparsers.add_parser("concluir", help="Concluir uma tarefa pelo ID")
    parser_concluir.add_argument("id", type=int, help="ID da tarefa a ser concluída")

    parser_remover = subparsers.add_parser("remover", help="Remover uma tarefa pelo ID")
    parser_remover.add_argument("id", type=int, help="ID da tarefa a ser removida")

    parser_filtrar = subparsers.add_parser("filtrar", help="Filtrar tarefas pelo status")
    parser_filtrar.add_argument("status", type=str, choices=["pendente", "concluida", "concluída"], help="Status da tarefa (pendente ou concluída)")

    parser_editar = subparsers.add_parser("editar", help="Editar a descrição de uma tarefa pelo ID")
    parser_editar.add_argument("id", type=int, help="ID da tarefa a ser editada")
    parser_editar.add_argument("nova_descricao", type=str, help="Nova descrição da tarefa")


    # Faz a leitura dos argumentos passados na linha de comando e os armazena em um objeto chamado args.
    args = parser.parse_args()

    if args.comando == "adicionar":
            
            data_atual = datetime.now().strftime("%d/%m/%Y")
            gerenciador.adicionar_tarefa(args.descricao, data_atual)
            salvar_arquivo(gerenciador.lista_tarefas)
            id_criado = len(gerenciador.lista_tarefas)
            print(f"Tarefa #{id_criado} adicionada.")

    elif args.comando == "listar":
            
            gerenciador.listar_tarefas()

    elif args.comando == "concluir":
            
            gerenciador.concluir_tarefa(args.id)
            salvar_arquivo(gerenciador.lista_tarefas)

    elif args.comando == "remover":
            
            gerenciador.remover_tarefa(args.id)
            salvar_arquivo(gerenciador.lista_tarefas)

    elif args.comando == "filtrar":
            
            gerenciador.filtra_tarefas_por_status(args.status)

    elif args.comando == "editar":

            gerenciador.editar_descricao_tarefa(args.id, args.nova_descricao)
            salvar_arquivo(gerenciador.lista_tarefas)
        
    else:
        parser.print_help()


if __name__ == "__main__":
    main()


