import json
from Package.Tarefas import ListaTarefas, TarefaSimples, TarefaPrioritaria

def salvar(lista, caminho):
    dados = []
    for tarefa in lista.tarefas:
        if isinstance(tarefa, TarefaPrioritaria):
            dados.append({
                'tipo': 'prioritaria',
                'descricao': tarefa.descricao,
                'nivel_prioridade': tarefa.nivel_prioridade,
                'concluida': tarefa.concluida
            })
        else:
            dados.append({  
                'tipo': 'simples',
                'descricao': tarefa.descricao,
                'concluida': tarefa.concluida
            })
    with open(caminho, 'w') as f:
        json.dump(dados, f, indent=2)

def carregar(caminho):
    print (caminho)
    lista = ListaTarefas()
    try:
        with open(caminho, 'r') as f:
            dados = json.load(f)
            for item in dados:
                if item['tipo'] == 'prioritaria':
                    tarefa = TarefaPrioritaria(item['descricao'], item['prioridade'])
                else:
                    tarefa = TarefaSimples(item['descricao'])
                if item['concluida']:
                    tarefa.marcar_como_concluida()
                lista.adicionar_tarefa(tarefa)
    except FileNotFoundError:
        pass
    return lista
