import os
import json
from src.tarefa import Tarefa, gerenciaTarefas, normalizar_texto
from src.armazenamento import salvar_arquivo, carregar_arquivo

def test_normalizar_texto_variacoes():
    assert normalizar_texto("  CONCLUÍDA  ") == "concluida"
    assert normalizar_texto("pendente") == "pendente"
    assert normalizar_texto("  PENDENTE  ") == "pendente"

def test_ciclo_completo_gerenciamento():
    gerenciador = gerenciaTarefas()
    
    gerenciador.adicionar_tarefa("Comprar pão", "09/10/2026")
    gerenciador.adicionar_tarefa("Estudar Python", "09/10/2026")
    gerenciador.adicionar_tarefa("Pagar contas", "09/10/2026")
    
    assert len(gerenciador.lista_tarefas) == 3
    
    gerenciador.concluir_tarefa(2)
    assert normalizar_texto(gerenciador.lista_tarefas[1].status) == "concluida"
    
    gerenciador.editar_descricao_tarefa(3, "Pagar internet e luz")
    assert gerenciador.lista_tarefas[2].descricao == "Pagar internet e luz"
    
    gerenciador.remover_tarefa(1)
    assert len(gerenciador.lista_tarefas) == 2
    assert gerenciador.lista_tarefas[0].descricao == "Estudar Python"

def test_persistencia_arquivo_completo(tmp_path):
    arquivo_json = tmp_path / "tarefas_complexas.json"
    
    gerenciador = gerenciaTarefas()
    gerenciador.adicionar_tarefa("Tarefa persistente 1", "09/10/2026")
    gerenciador.adicionar_tarefa("Tarefa persistente 2", "09/10/2026")
    gerenciador.concluir_tarefa(1)
    
    salvar_arquivo(gerenciador.lista_tarefas, arquivo=str(arquivo_json))
    assert os.path.exists(arquivo_json)
    
    tarefas_carregadas = carregar_arquivo(arquivo=str(arquivo_json))
    
    assert len(tarefas_carregadas) == 2
    assert tarefas_carregadas[0].descricao == "Tarefa persistente 1"
    assert normalizar_texto(tarefas_carregadas[0].status) == "concluida"
    assert tarefas_carregadas[1].descricao == "Tarefa persistente 2"
    assert normalizar_texto(tarefas_carregadas[1].status) == "pendente"

def test_persistencia_arquivo_inexistente():
    resultado = carregar_arquivo("arquivo_que_nao_existe.json")
    assert resultado == []

def test_persistencia_arquivo_vazio(tmp_path):
    arquivo_vazio = tmp_path / "vazio.json"
    arquivo_vazio.write_text("")
    
    resultado = carregar_arquivo(str(arquivo_vazio))
    assert resultado == []

def test_persistencia_arquivo_corrompido(tmp_path):
    arquivo_corrompido = tmp_path / "corrompido.json"
    arquivo_corrompido.write_text("{ json invalido ...")
    
    resultado = carregar_arquivo(str(arquivo_corrompido))
    assert resultado == []