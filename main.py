import tkinter as tk
import tkinter.font as tkFont
from tkinter import filedialog
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
            'data_vencimento': data_vencimento,
            'concluida': False
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
      
# Função para atualizar a lista de tarefas na tela
def atualizar_lista():
    lista_tarefas.delete(0, "end")
    for tarefa in tarefas:
        dados = f"Tarefa: {tarefa['tarefa']} - Data: {tarefa['data_vencimento']} - Prioridade: {tarefa['prioridade']}"
        if tarefa['concluida']:
            dados = f'[Concluída] {dados}'
        lista_tarefas.insert("end", dados)

# Função para excluir a tarefa selecionada
def excluir_tarefa():
    selecao = lista_tarefas.curselection()
    if selecao:
        index = selecao[0]
        tarefas.pop(index)
        atualizar_lista()
        salvar_tarefas()

# Função para Concluir a tarefa selecionada
def concluir_tarefa():
    selecao = lista_tarefas.curselection()
    if selecao:
        index = selecao[0]
        tarefa = tarefas[index]
        tarefa['concluida'] = True
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

# Função para filtrar tarefas
def filtrar_tarefas():
    filtro_data = entrada_filtro_data.get()
    filtro_prioridade = var_filtro_prioridade.get()
    tarefas_filtradas = [tarefa for tarefa in tarefas if
                         (not filtro_data or tarefa['data_vencimento'] == filtro_data) and
                         (not filtro_prioridade or tarefa['prioridade'] == filtro_prioridade)]
    
    lista_tarefas.delete(0, "end")
    for tarefa in tarefas_filtradas:
        dados = f"Tarefa: {tarefa['tarefa']} - Data: {tarefa['data_vencimento']} - Prioridade: {tarefa['prioridade']}"
        lista_tarefas.insert("end", dados)

# Função para exportar as tarefas para um arquivo Json
def exportar_tarefas():
    arquivo_destino = filedialog.asksaveasfilename(defaultextension='.json', filetypes=[("Arquivos JSON", "*.json")])
    if arquivo_destino:
        with open(arquivo_destino, 'w') as arquivo:
            json.dump(tarefas, arquivo)

# Função para importar as tarefas de um arquivo Json
def importar_tarefas():
    arquivo_origem = filedialog.askopenfilename(filetypes=[("Arquivos JSON", "*.json")])
    if arquivo_origem:
        with open(arquivo_origem, 'r') as arquivo:
            tarefas.extend(json.load(arquivo))
        atualizar_lista()

# Criar a janela principal
janela = tk.Tk()
janela.title("Gerenciador de Tarefas")
janela.geometry('900x600')
janela.resizable(False, False)
janela.configure(background='#e7d4b6')
fonte = tkFont.Font(family='Comic Sans MS', size= 11, weight='bold', slant='italic')
janela.option_add('*font', fonte)
janela.option_add('*foreground', '#444444')

# Variável para a prioridade
var_prioridade = tk.StringVar()
var_prioridade.set("Prioridade")

# Criar uma entrada de texto
entrada_tarefa = tk.Entry(janela, width=30, bg= "#edebe6", selectbackground='#cccabc', selectforeground='#444444')
entrada_tarefa.insert(0, "Tarefa")
entrada_tarefa.pack(pady=10)
entrada_tarefa.place(x=313, y=10)

# Criar uma entrada para data de vencimento
entrada_data = tk.Entry(janela, width=30, bg= "#edebe6", selectbackground='#cccabc', selectforeground='#444444')
entrada_data.insert(0, "Data")
entrada_data.pack()
entrada_data.place(x=313, y= 50)

# Criar um menu suspenso para a prioridade
menu_prioridade = tk.OptionMenu(janela, var_prioridade, "Baixa", "Média", "Alta")
menu_prioridade.configure(bg= '#ece7dc', activebackground= '#ece7dc', activeforeground= '#000000', highlightbackground= '#d7cfc1')
menu_prioridade.pack(pady=5)
menu_prioridade.place(x=390, y=90)

# Criar um botão para adicionar tarefa
botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa, bg='#ece7dc', activebackground='#ece7dc')
botao_adicionar.pack()
botao_adicionar.place(x=380, y=140)

# mostrar a data atual
data_atual = datetime.datetime.now().strftime("%d-%m-%Y")
data_atualwin = tk.Message(janela, width=120, text=f'Data atual: {data_atual}', bg= "#e7d4b6")
data_atualwin.pack()
data_atualwin.place(x=276, y=250)

# Criar uma lista de tarefas
lista_tarefas = tk.Listbox(janela, width=70, bg='#edebe6', highlightbackground='#d7cfc1',selectbackground='#edebe6', selectforeground='#000000')
lista_tarefas.pack(pady=10)
lista_tarefas.place(x=134, y= 350)

# Criar um botão para editar tarefa
botao_editar = tk.Button(janela, text="Editar Tarefa", command=editar_tarefa, bg='#ece7dc', activebackground='#ece7dc')
botao_editar.pack(pady=5)
botao_editar.place(x=150, y=90)

# Criar um botão para concluir uma tarefa
botao_concluir = tk.Button(janela, text='Concluir Tarefa', command=concluir_tarefa, bg='#ece7dc', activebackground='#ece7dc')
botao_concluir.pack()
botao_concluir.place(x=145, y=190)

# Criar um botão para excluir tarefa
botao_excluir = tk.Button(janela, text="Excluir Tarefa", command=excluir_tarefa, bg='#ece7dc', activebackground='#ece7dc')
botao_excluir.pack()
botao_excluir.place(x=148, y=140)

# Criar entrada de filtro para data
entrada_filtro_data = tk.Entry(janela, width=36, bg= "#edebe6", selectbackground='#cccabc', selectforeground='#444444')
entrada_filtro_data.insert(0, "Filtrar por Data(apague caso não usar data)")
entrada_filtro_data.pack(pady=10)
entrada_filtro_data.place(x=165, y=310)

# Criar menu suspenso para filtro de prioridade
var_filtro_prioridade = tk.StringVar()
var_filtro_prioridade.set("Filtrar por Prioridade")
menu_filtro_prioridade = tk.OptionMenu(janela, var_filtro_prioridade, "", "Baixa", "Média", "Alta")
menu_filtro_prioridade.configure(bg= '#ece7dc', activebackground= '#ece7dc', activeforeground= '#000000', highlightbackground= '#d7cfc1')
menu_filtro_prioridade.pack(pady=5)
menu_filtro_prioridade.place(x=540, y= 250)

# Criar botão para aplicar filtros
botao_filtrar = tk.Button(janela, text="Filtrar Tarefas", command=filtrar_tarefas, bg='#ece7dc', activebackground='#ece7dc')
botao_filtrar.pack()
botao_filtrar.place(x=580, y= 300)

# Criar botão para exportar tarefas
botao_exportar = tk.Button(janela, text='Salvar', command=exportar_tarefas, bg='#ece7dc', activebackground='#ece7dc')
botao_exportar.pack(pady=10)
botao_exportar.place(x=680, y=90)

# Criar botão para importar tarefas
botao_importar = tk.Button(janela, text='Carregar',command=importar_tarefas, bg='#ece7dc', activebackground='#ece7dc')
botao_importar.pack(pady=5)
botao_importar.place(x=672, y=140)

# Atualizar a lista de tarefas na inicialização
tarefas = carregar_tarefas()
atualizar_lista()

# Iniciar a interface gráfica
janela.mainloop()