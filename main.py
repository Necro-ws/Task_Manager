import tkinter as tk
import json
import datetime

# Função para adicionar uma nova tarefa
def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    prioridade = var_prioridade.get()
    data_vencimento = entrada_data.get()
    
    if tarefa:
        nova_tarefa = {
            'tarefa': tarefa,
            'prioridade': prioridade,
            'data_vencimento': data_vencimento
        }
        tarefas.append(nova_tarefa)
        atualizar_lista()
        entrada_tarefa.delete(0, "end")
        entrada_data.delete(0, "end")
        var_prioridade.set("Baixa")
        salvar_tarefas()

# Função para editar a tarefa selecionada
def editar_tarefa():
    selecao = lista_tarefas.curselection()
    if selecao:
        index = selecao[0]
        tarefa = tarefas[index]
        entrada_tarefa.delete(0, "end")
        entrada_tarefa.insert(0, tarefa['tarefa'])
        entrada_data.delete(0, "end")
        entrada_data.insert(0, tarefa['data_vencimento'])
        var_prioridade.set(tarefa['prioridade'])
        excluir_tarefa()
        salvar_tarefas()

# função para copiar tarefas selecionadas

def copiar_tarefa():
    lista_up = []
    selecao = lista_tarefas.curselection()
    if selecao:
        index = selecao[0]
        tarefa = tarefas[index]
        lista_up.append(tarefa)
        print(lista_up[0])
        

# Função para atualizar a lista de tarefas na tela
def atualizar_lista():
    lista_tarefas.delete(0, "end")
    for tarefa in tarefas:
        dados = f"Tarefa: {tarefa['tarefa']} - Data: {tarefa['data_vencimento']} - Prioridade: {tarefa['prioridade']}"
        lista_tarefas.insert("end", dados)

# Função para excluir a tarefa selecionada
def excluir_tarefa():
    selecao = lista_tarefas.curselection()
    if selecao:
        index = selecao[0]
        tarefas.pop(index)
        atualizar_lista()
        salvar_tarefas()

# Função para salvar as tarefas em um arquivo JSON
def salvar_tarefas():
    with open("tarefas.json", "w") as arquivo:
        json.dump(tarefas, arquivo)

# Função para carregar as tarefas a partir do arquivo JSON
def carregar_tarefas():
    try:
        with open("tarefas.json", "r") as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return []

# Criar a janela principal
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.configure(background='#78bbf5')

# Variável para a prioridade
var_prioridade = tk.StringVar()
var_prioridade.set("Prioridade")

# Criar uma entrada de texto
entrada_tarefa = tk.Entry(janela, width=30)
entrada_tarefa.insert(0, "Tarefa")
entrada_tarefa.pack(pady=10)

# Criar uma entrada para data de vencimento
entrada_data = tk.Entry(janela, width=30)
entrada_data.insert(0, "Data")
entrada_data.pack()

# Criar um menu suspenso para a prioridade
menu_prioridade = tk.OptionMenu(janela, var_prioridade, "Baixa", "Média", "Alta")
menu_prioridade.pack()

# Criar um botão para adicionar tarefa
botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa, bg='#ffffff')
botao_adicionar.pack()

# mostrar a data atual
data_atual = datetime.datetime.now().strftime("%d-%m-%Y")
data_atualwin = tk.Message(janela, width=60, text=f'Data atual: {data_atual}')
data_atualwin.pack()

# Criar uma lista de tarefas
lista_tarefas = tk.Listbox(janela, width=70, bg='#ffffff')
lista_tarefas.pack(pady=10)

# Criar um botão para editar tarefa
botao_editar = tk.Button(janela, text="Editar Tarefa", command=editar_tarefa, bg='#ffffff')
botao_editar.pack()

# Criar um botão para excluir tarefa
botao_excluir = tk.Button(janela, text="Excluir Tarefa", command=excluir_tarefa, bg='#ffffff')
botao_excluir.pack()

# Botao para salvar no google
botao_salvar = tk.Button(janela, text="Salvar", command=copiar_tarefa)
botao_salvar.pack()

# Atualizar a lista de tarefas na inicialização
tarefas = carregar_tarefas()
atualizar_lista()

# Iniciar a interface gráfica
janela.mainloop()