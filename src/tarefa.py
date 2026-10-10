import unicodedata

def normalizar_texto(texto):
    # Remove acentos, converte para minúsculas e remove espaços nas pontas
    nfkd = unicodedata.normalize('NFKD', texto)
    texto_sem_acento = "".join([c for c in nfkd if not unicodedata.combining(c)])
    return texto_sem_acento.lower().strip()

class Tarefa:
    id = 0
    descricao = ""
    status = ""
    data_criacao = 0

    def __init__(self, id, descricao, status, data_criacao):
        self.id = id
        self.descricao = descricao
        self.status = status
        self.data_criacao = data_criacao


class gerenciaTarefas:

    def __init__(self):
        self.lista_tarefas = []

    def adicionar_tarefa(self, descricao, data_criacao):

        nova_tarefa = Tarefa(len(self.lista_tarefas) + 1, descricao, "pendente", data_criacao)

        self.lista_tarefas.append(nova_tarefa)

    def listar_tarefas(self):

        if not self.lista_tarefas:
            print("Nenhuma tarefa cadastrada.")

        else:
            for tarefa in self.lista_tarefas:
                status_simbolo = "[x]" if tarefa.status == "concluida" else "[ ]"
                print(f"{status_simbolo} #{tarefa.id} {tarefa.descricao} {tarefa.data_criacao}")

    def concluir_tarefa(self, id):

        for tarefa in self.lista_tarefas:
            if tarefa.id == id:
                tarefa.status = "concluida"
                print(f"Tarefa #{id} concluída.")
                break

        else:
            print(f"Tarefa com ID {id} não encontrada.")

    def remover_tarefa(self, id):
        for tarefa in self.lista_tarefas:
            if tarefa.id == id:
                self.lista_tarefas.remove(tarefa)
                print(f"Tarefa #{id} removida.")
                break
        else:
            print(f"Tarefa com ID {id} não encontrada.")

    def filtra_tarefas_por_status(self, status):

        status_alvo_normalizado = normalizar_texto(status)

        tarefas_filtradas = [tarefa for tarefa in self.lista_tarefas if normalizar_texto(tarefa.status) == status_alvo_normalizado]

        if not tarefas_filtradas:
            print(f"Nenhuma tarefa com status '{status}' encontrada.")

        else:
            for tarefa in tarefas_filtradas:
                status_simbolo = "[x]" if tarefa.status == "concluida" else "[ ]"
                print(f"{status_simbolo} #{tarefa.id} {tarefa.descricao} {tarefa.data_criacao}")

    def editar_descricao_tarefa(self, id, nova_descricao):
        for tarefa in self.lista_tarefas:
            if tarefa.id == id:
                tarefa.descricao = nova_descricao
                print(f"Tarefa #{id} atualizada com nova descrição: {nova_descricao}")
                break
        else:
            print(f"Tarefa com ID {id} não encontrada.")
    