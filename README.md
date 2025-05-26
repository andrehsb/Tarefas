# 📝 Projeto - Lista de Tarefas com Interface Gráfica

Este projeto tem como objetivo desenvolver um sistema de gerenciamento de tarefas com interface gráfica (Tkinter), utilizando os princípios da **Programação Orientada a Objetos (POO)**. 

## 🎯 Problema a Ser Resolvido

Usuários precisam organizar suas tarefas diárias, com possibilidade de atribuição de prioridade, marcação como concluída e armazenamento automático.

---

## ✅ Casos de Uso

### Caso de Uso 01 – Adicionar Tarefa
- O usuário insere uma descrição e, opcionalmente, um nível de prioridade.
- A tarefa é adicionada à lista.

### Caso de Uso 02 – Concluir Tarefa
- O usuário marca uma tarefa como concluída.

### Caso de Uso 03 – Refazer Tarefa
- O usuário desfaz a marcação de uma tarefa concluída.

### Caso de Uso 04 – Remover Tarefa
- O usuário remove uma tarefa da lista.

---

## 🧪 Casos de Teste

### Teste 01 – Adição de Tarefa Simples
**Entrada**: "Comprar pão" 
**Esperado**: A tarefa aparece na lista com ícone 🔲.

### Teste 02 – Adição de Tarefa Prioritária
**Entrada**: "Estudar para prova", Prioridade: 1 
**Esperado**: A tarefa é exibida como [P1] Estudar para prova, com cor vermelha.

### Teste 03 – Concluir Tarefa
**Ação**: Selecionar "Comprar pão" e clicar em "Concluir" 
**Esperado**: Tarefa marcada com ícone ✅.

### Teste 04 – Refazer Tarefa
**Ação**: Selecionar uma tarefa concluída e clicar em "Refazer" 
**Esperado**: Tarefa volta ao estado de não concluída.

### Teste 05 – Remoção de Tarefa
**Ação**: Selecionar qualquer tarefa e clicar em "Remover" 
**Esperado**: Tarefa removida da lista.

---

## 🧱 Diagrama de Classes (UML)

![Diagrama de Classes UML](A_UML_class_diagram_displays_four_classes_in_a_tas.png)

---

## 💾 Funcionalidades
- Adicionar tarefas simples ou com prioridade.
- Marcar como concluída ou refazer.
- Remover tarefas.
- Interface gráfica com `tkinter`.
- Armazenamento persistente em `tarefas.json`.

---

## 🧠 Recursos de POO Utilizados
- Herança (Tarefa → TarefaSimples / TarefaPrioritaria)
- Polimorfismo (método `exibir()`)
- Encapsulamento (atributos privados com métodos)
- Composição forte (ListaTarefas → lista de Tarefas)
- Associação fraca (Aplicacao → ListaTarefas)

