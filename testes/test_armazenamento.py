import os
import pytest
from src.tarefa import Tarefa, gerenciaTarefas
from src.armazenamento import salvar_arquivo, carregar_arquivo

def test_salvar_e_carregar_tarefas(tmp_path):
    """ Cria um caminho de arquivo temporário isolado para o teste """
    arquivo_temp = tmp_path / "tarefas_teste.json"
    
    gerenciador = gerenciaTarefas()
    gerenciador.adicionar_tarefa("Tarefa de Teste 1", "10/10/2026")
    gerenciador.adicionar_tarefa("Tarefa de Teste 2", "10/10/2026")
    
    """ Salva no arquivo temporário """
    salvar_arquivo(gerenciador.lista_tarefas, arquivo=str(arquivo_temp))
    
    """ Carrega do arquivo temporário """
    tarefas_carregadas = carregar_arquivo(arquivo=str(arquivo_temp))
    
    assert len(tarefas_carregadas) == 2
    assert tarefas_carregadas[0].descricao == "Tarefa de Teste 1"
    assert tarefas_carregadas[1].status == "pendente"

def test_carregar_arquivo_inexistente():
    """ Deve retornar uma lista vazia sem quebrar caso o arquivo não exista """
    resultado = carregar_arquivo("arquivo_que_nao_existe.json")
    assert resultado == []

def test_carregar_arquivo_vazio(tmp_path):
    arquivo_vazio = tmp_path / "vazio.json"
    arquivo_vazio.write_text("") 
    
    resultado = carregar_arquivo(str(arquivo_vazio))
    assert resultado == []