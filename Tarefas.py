from abc import ABC, abstractmethod
import json

class Tarefa(ABC):
    def __init__(self, descricao):
        self.descricao = descricao
        self.concluida = False

    def marcar_como_concluida(self):
        self.concluida = True

    def desmarcar_como_concluida(self):
        self.concluida = False

    @abstractmethod
    def exibir(self):
        pass

    def to_dict(self):
        return {
            'tipo': self.__class__.__name__,
            'descricao': self.descricao,
            'concluida': self.concluida
        }

class TarefaSimples(Tarefa):
    def exibir(self):
        status = '✅' if self.concluida else '🔲'
        return f'{status} {self.descricao}'

class TarefaPrioritaria(Tarefa):
    def __init__(self, descricao, nivel_prioridade):
        super().__init__(descricao)
        self.nivel_prioridade = nivel_prioridade

    def exibir(self):
        status = '✅' if self.concluida else '🔲'
        return f'{status} [P{self.nivel_prioridade}] {self.descricao}'

    def to_dict(self):
        dados = super().to_dict()
        dados['prioridade'] = self.nivel_prioridade
        return dados

class ListaTarefas:
    def __init__(self):
        self.tarefas = []

    def adicionar_tarefa(self, tarefa):
        if isinstance(tarefa, TarefaPrioritaria): 
            posicao = len(self.tarefas)  
            for i, t in enumerate(self.tarefas):
                if isinstance(t, TarefaPrioritaria):
                    if tarefa.nivel_prioridade <= t.nivel_prioridade:
                        posicao = i
                        break
                    posicao = i + 1
                else:
                    posicao = i
                    break
            self.tarefas.insert(posicao, tarefa)
        else:
            self.tarefas.append(tarefa)

    def remover_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            return self.tarefas.pop(indice)

    def concluir_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].marcar_como_concluida()

    def refazer_tarefa(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].desmarcar_como_concluida()