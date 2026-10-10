import json
from src.tarefa import Tarefa, gerenciaTarefas

ARQUIVO_PADRAO = "tarefas.json"

# Objetivo: transformar os objetos (tarefas) em um formato que possa ser armazenado em arquivo (JSON)
def salvar_arquivo(lista_tarefas, arquivo=ARQUIVO_PADRAO):

    # Dicionário é uma estrutura exclusiva do python.
    lista_dicionarios = []
    for tarefa in lista_tarefas:

        tarefa_dicionario = {
            "id": tarefa.id,
            "descricao": tarefa.descricao,
            "status": tarefa.status,
            "data_criacao": tarefa.data_criacao
        }

        lista_dicionarios.append(tarefa_dicionario)

    # Salvar a lista de dicionários em um arquivo JSON. "w" significa escrita (write), e "utf-8" é a codificação padrão de caracteres.
    # O ensure_ascii=False permite que caracteres especiais (como acentos) sejam salvos corretamente, e indent=4 deixa o arquivo mais legível.
    # O json.dump() é a função que faz a conversão de objeto Python para JSON e escreve no arquivo.
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(lista_dicionarios, f, ensure_ascii=False, indent=4)


def carregar_arquivo(arquivo=ARQUIVO_PADRAO):
    try:
        with open(arquivo, "r", encoding="utf-8") as f:

            conteudo = f.read().strip()  
            if not conteudo: 
                return []

            lista_json = json.loads(conteudo)
            lista_tarefas = []
            
            for tarefa in lista_json:
                nova_tarefa = Tarefa(**tarefa) # O ** desempacota o dicionário, passando cada chave como argumento para o construtor da classe Tarefa
                lista_tarefas.append(nova_tarefa)
                
            return lista_tarefas
            
    except (FileNotFoundError, json.JSONDecodeError):
        # Se o arquivo não existe, retorna uma lista vazia na primeira execução
        return []

