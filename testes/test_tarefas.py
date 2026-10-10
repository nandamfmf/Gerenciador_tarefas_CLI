import pytest
from src.tarefa import gerenciaTarefas

def test_adicionar_tarefa():
    gerenciador = gerenciaTarefas()
    gerenciador.adicionar_tarefa("Estudar Python", "10/10/2026")
    
    assert len(gerenciador.lista_tarefas) == 1
    assert gerenciador.lista_tarefas[0].id == 1
    assert gerenciador.lista_tarefas[0].descricao == "Estudar Python"
    assert gerenciador.lista_tarefas[0].status == "pendente"

def test_id_incremental_apos_remocao():
    gerenciador = gerenciaTarefas()
    gerenciador.adicionar_tarefa("Tarefa A", "10/10/2026")
    gerenciador.adicionar_tarefa("Tarefa B", "10/10/2026")
    
    gerenciador.remover_tarefa(1)

    gerenciador.adicionar_tarefa("Tarefa C", "10/10/2026")
    
    assert len(gerenciador.lista_tarefas) == 2
    assert gerenciador.lista_tarefas[0].id == 2
    assert gerenciador.lista_tarefas[1].id == 3

def test_concluir_tarefa():
    gerenciador = gerenciaTarefas()
    gerenciador.adicionar_tarefa("Fazer compras", "10/10/2026")
    
    gerenciador.concluir_tarefa(1)
    assert gerenciador.lista_tarefas[0].status == "concluida"

def test_editar_descricao_tarefa():
    gerenciador = gerenciaTarefas()
    gerenciador.adicionar_tarefa("Texto antigo", "10/10/2026")
    
    gerenciador.editar_descricao_tarefa(1, "Texto atualizado")
    assert gerenciador.lista_tarefas[0].descricao == "Texto atualizado"

def test_filtrar_tarefas_por_status():
    gerenciador = gerenciaTarefas()
    gerenciador.adicionar_tarefa("Tarefa 1", "10/10/2026")
    gerenciador.adicionar_tarefa("Tarefa 2", "10/10/2026")
    gerenciador.concluir_tarefa(2)
    
    pendentes = [t for t in gerenciador.lista_tarefas if t.status == "pendente"]
    concluidas = [t for t in gerenciador.lista_tarefas if t.status == "concluida"]
    
    assert len(pendentes) == 1
    assert len(concluidas) == 1
