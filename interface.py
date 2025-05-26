import tkinter as tk
from tkinter import ttk, messagebox
from Package.Tarefas import ListaTarefas, TarefaSimples, TarefaPrioritaria
from Package.banco_dados import carregar, salvar
PATH_TAREFAS = 'Package/tarefas.json'
class Aplicacao:
    def __init__(self, master):
        self.master = master
        self.master.title("📋 Lista de Tarefas")
        self.master.geometry("550x550")
        
        self.lista = carregar(PATH_TAREFAS)  # Usa a função do banco_dados.py
        self.criar_widgets()
        self.atualizar_lista()

    def fechar(self):
        salvar(self.lista, PATH_TAREFAS)  # Usa a função do banco_dados.py
        self.master.destroy()

    def criar_widgets(self):
        # Frame principal
        main_frame = ttk.Frame(self.master, padding="10")
        main_frame.pack(fill=tk.BOTH, expand=True)

        # Frame de entrada
        entry_frame = ttk.Frame(main_frame)
        entry_frame.pack(fill=tk.X, pady=5)

        ttk.Label(entry_frame, text="Descrição:").grid(row=0, column=0, sticky=tk.W)
        self.entrada = ttk.Entry(entry_frame, width=40)
        self.entrada.grid(row=1, column=0, padx=5, sticky=tk.W+tk.E)

        ttk.Label(entry_frame, text="Prioridade (1-5):").grid(row=0, column=1, sticky=tk.W)
        self.prioridade = ttk.Combobox(entry_frame, width=5, values=list(range(1,6)))
        self.prioridade.grid(row=1, column=1, padx=5)

        # Frame de botões
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=10)

        ttk.Button(button_frame, text="Adicionar", command=self.adicionar_tarefa).pack(side=tk.LEFT, padx=5)
        self.btn_concluir = ttk.Button(button_frame, text="Concluir", command=self.concluir_tarefa, state='disabled')
        self.btn_concluir.pack(side=tk.LEFT, padx=5)
        self.btn_refazer = ttk.Button(button_frame, text="Refazer", command=self.refazer_tarefa, state='disabled')
        self.btn_refazer.pack(side=tk.LEFT, padx=5)
        self.btn_remover = ttk.Button(button_frame, text="Remover", command=self.remover_tarefa)
        self.btn_remover.pack(side=tk.LEFT, padx=5)

        # Lista de tarefas
        self.lista_box = tk.Listbox(
            main_frame,
            width=60,
            height=20,
            font=('Arial', 10),
            selectbackground='#4a98f7',
            selectforeground='white'
        )
        self.lista_box.pack(fill=tk.BOTH, expand=True)

        self.lista_box.bind('<<ListboxSelect>>', self.verificar_selecao)
        self.lista_box.bind('<Double-Button-1>', self.desmarca_tarefa)

        self.master.protocol("WM_DELETE_WINDOW", self.fechar)

    def adicionar_tarefa(self):
        descricao = self.entrada.get()
        if not descricao:
            messagebox.showwarning("Aviso", "Digite uma descrição")
            return

        prioridade = self.prioridade.get()
        if prioridade:
            try:
                tarefa = TarefaPrioritaria(descricao, int(prioridade))
            except ValueError:
                messagebox.showerror("Erro", "Prioridade deve ser 1-5")
                return
        else:
            tarefa = TarefaSimples(descricao)

        self.lista.adicionar_tarefa(tarefa)
        self.entrada.delete(0, tk.END)
        self.prioridade.set('')
        self.atualizar_lista()

    def desmarca_tarefa(self, event = None):
        indice = self.lista_box.index(f"@0,{event.y}")
        if indice >= 0 and indice in self.lista_box.curselection():
            self.lista_box.selection_clear(indice)       
            self.verificar_selecao()

    def verificar_selecao(self, event=None):
        selecao = self.lista_box.curselection()
        if selecao:
            tarefa = self.lista.tarefas[selecao[0]]
            if tarefa.concluida:
                self.btn_concluir.config(state='disabled')
                self.btn_refazer.config(state='normal')
            else:
                self.btn_concluir.config(state='normal')
                self.btn_refazer.config(state='disabled')
            self.btn_remover.config(state='normal')
        else:
            self.btn_concluir.config(state='disabled')
            self.btn_refazer.config(state='disabled')
            self.btn_remover.config(state='disabled')

    def concluir_tarefa(self):
        selecao = self.lista_box.curselection()
        if selecao:
            self.lista.concluir_tarefa(selecao[0])
            self.atualizar_lista()

    def refazer_tarefa(self):
        selecao = self.lista_box.curselection()
        if selecao:
            self.lista.refazer_tarefa(selecao[0])
            self.atualizar_lista()

    def remover_tarefa(self):
        selecao = self.lista_box.curselection()
        if selecao:
            self.lista.remover_tarefa(selecao[0])
            self.atualizar_lista()

    def atualizar_lista(self):
        self.lista_box.delete(0, tk.END)
        cores = ['#FF3B30', '#FF9500', '#FFCC00', '#34C759', '#007AFF']
        for tarefa in self.lista.tarefas:
            self.lista_box.insert(tk.END, tarefa.exibir())
            if isinstance(tarefa, TarefaPrioritaria):
                cor = cores[tarefa.nivel_prioridade - 1]
                self.lista_box.itemconfig(tk.END, fg=cor)
            if tarefa.concluida:
                self.lista_box.itemconfig(tk.END, fg='#888888')

    def fechar(self):
        salvar(self.lista, PATH_TAREFAS)
        self.master.destroy()