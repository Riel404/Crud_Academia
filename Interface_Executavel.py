import sqlite3
import tkinter as tk
from tkinter import ttk

# Função para inserir um cliente no banco de dados com tratamento de exceções
def inserir_cliente(nome, idade, sexo, endereco, telefone):
    try:
        idade = int(idade)  # Converter a idade para inteiro
        if idade < 0:
            raise ValueError("A idade deve ser um número inteiro não negativo.")
        if not isinstance(sexo, str) or len(sexo) != 1:
            raise ValueError("O sexo deve ser uma única letra.")
        if not isinstance(endereco, str):
            raise ValueError("O endereço deve ser uma string.")
        if not isinstance(telefone, str) or len(telefone) < 8:
            raise ValueError("O telefone deve ser uma string com pelo menos 8 caracteres.")

        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO clientes (nome, idade, sexo, endereco, telefone) VALUES (?, ?, ?, ?, ?)',
                       (nome, idade, sexo, endereco, telefone))
        conn.commit()
        conn.close()
        print("Cliente cadastrado com sucesso!")
    except (sqlite3.Error, ValueError) as e:
        print(f"Erro ao inserir cliente: {e}")

# Função para inserir um treinador no banco de dados com tratamento de exceções
def inserir_treinador(nome, especializacao, experiencia, numero_registro):
    try:
        experiencia = int(experiencia)  # Converter a experiência para inteiro
        if experiencia < 0:
            raise ValueError("A experiência deve ser um número inteiro não negativo.")
        if not isinstance(numero_registro, str) or len(numero_registro) < 6:
            raise ValueError("O número de registro deve ter pelo menos 6 caracteres.")

        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO treinadores (nome, especializacao, experiencia, numero_registro) VALUES (?, ?, ?, ?)',
                       (nome, especializacao, experiencia, numero_registro))
        conn.commit()
        conn.close()
        print("Treinador cadastrado com sucesso!")
    except (sqlite3.Error, ValueError) as e:
        print(f"Erro ao inserir treinador: {e}")

# Função para listar todos os clientes com tratamento de exceções
def listar_clientes():
    try:
        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM clientes')
        clientes = cursor.fetchall()
        conn.close()
        if not clientes:
            print("Nenhum cliente cadastrado.")
        else:
            for cliente in clientes:
                print(cliente)
    except sqlite3.Error as e:
        print(f"Erro ao listar clientes: {e}")

# Função para listar todos os treinadores com tratamento de exceções
def listar_treinadores():
    try:
        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM treinadores')
        treinadores = cursor.fetchall()
        conn.close()
        if not treinadores:
            print("Nenhum treinador cadastrado.")
        else:
            for treinador in treinadores:
                print(treinador)
    except sqlite3.Error as e:
        print(f"Erro ao listar treinadores: {e}")

# Função para atualizar informações de um cliente com tratamento de exceções
def atualizar_cliente(id, nome=None, idade=None, sexo=None, endereco=None, telefone=None):
    try:
        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()

        # Verifica quais campos devem ser atualizados
        update_fields = []
        if nome:
            update_fields.append(f"nome = '{nome}'")
        if idade:
            idade = int(idade)
            if idade < 0:
                raise ValueError("A idade deve ser um número inteiro não negativo.")
            update_fields.append(f"idade = {idade}")
        if sexo:
            if len(sexo) != 1:
                raise ValueError("O sexo deve ser uma única letra.")
            update_fields.append(f"sexo = '{sexo}'")
        if endereco:
            update_fields.append(f"endereco = '{endereco}'")
        if telefone:
            if len(telefone) < 8:
                raise ValueError("O telefone deve ter pelo menos 8 caracteres.")
            update_fields.append(f"telefone = '{telefone}'")

        if not update_fields:
            raise ValueError("Nenhum campo de atualização fornecido.")

        # Monta a consulta SQL para atualização
        update_query = f"UPDATE clientes SET {', '.join(update_fields)} WHERE id = {id}"
        cursor.execute(update_query)
        conn.commit()
        conn.close()
        print("Cliente atualizado com sucesso!")
    except (sqlite3.Error, ValueError) as e:
        print(f"Erro ao atualizar cliente: {e}")

# Função para atualizar informações de um treinador com tratamento de exceções
def atualizar_treinador(id, nome=None, especializacao=None, experiencia=None, numero_registro=None):
    try:
        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()

        # Verifica quais campos devem ser atualizados
        update_fields = []
        if nome:
            update_fields.append(f"nome = '{nome}'")
        if especializacao:
            update_fields.append(f"especializacao = '{especializacao}'")
        if experiencia:
            experiencia = int(experiencia)
            if experiencia < 0:
                raise ValueError("A experiência deve ser um número inteiro não negativo.")
            update_fields.append(f"experiencia = {experiencia}")
        if numero_registro:
            update_fields.append(f"numero_registro = '{numero_registro}'")

        if not update_fields:
            raise ValueError("Nenhum campo de atualização fornecido.")

        # Monta a consulta SQL para atualização
        update_query = f"UPDATE treinadores SET {', '.join(update_fields)} WHERE id = {id}"
        cursor.execute(update_query)
        conn.commit()
        conn.close()
        print("Treinador atualizado com sucesso!")
    except (sqlite3.Error, ValueError) as e:
        print(f"Erro ao atualizar treinador: {e}")

# Função para excluir um cliente com tratamento de exceções
def excluir_cliente(id):
    try:
        if not isinstance(id, int) or id < 1:
            raise ValueError("ID do cliente inválido.")

        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM clientes WHERE id=?', (id,))
        conn.commit()
        conn.close()
        print("Cliente excluído com sucesso!")
    except (sqlite3.Error, ValueError) as e:
        print(f"Erro ao excluir cliente: {e}")

# Função para excluir um treinador com tratamento de exceções
def excluir_treinador(id):
    try:
        if not isinstance(id, int) or id < 1:
            raise ValueError("ID do treinador inválido.")

        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM treinadores WHERE id=?', (id,))
        conn.commit()
        conn.close()
        print("Treinador excluído com sucesso!")
    except (sqlite3.Error, ValueError) as e:
        print(f"Erro ao excluir treinador: {e}")

# Função para listar clientes na interface
def listar_clientes_na_interface():
    tree_clientes.delete(*tree_clientes.get_children())
    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()
    conn.close()
    for cliente in clientes:
        tree_clientes.insert('', 'end', values=cliente)

# Função para adicionar um novo cliente na interface
def adicionar_cliente_na_interface():
    nome = nome_cliente_entry.get()
    idade = idade_cliente_entry.get()
    sexo = sexo_cliente_entry.get()
    endereco = endereco_cliente_entry.get()
    telefone = telefone_cliente_entry.get()
    inserir_cliente(nome, idade, sexo, endereco, telefone)
    listar_clientes_na_interface()
    nome_cliente_entry.delete(0, tk.END)
    idade_cliente_entry.delete(0, tk.END)
    sexo_cliente_entry.delete(0, tk.END)
    endereco_cliente_entry.delete(0, tk.END)
    telefone_cliente_entry.delete(0, tk.END)

# Função para atualizar um cliente na interface
def atualizar_cliente_na_interface():
    selected_item = tree_clientes.selection()
    if selected_item:
        id_cliente = int(tree_clientes.item(selected_item, 'values')[0])
        nome = nome_cliente_entry.get()
        idade = idade_cliente_entry.get()
        sexo = sexo_cliente_entry.get()
        endereco = endereco_cliente_entry.get()
        telefone = telefone_cliente_entry.get()

        atualizar_cliente(id_cliente, nome, idade, sexo, endereco, telefone)
        listar_clientes_na_interface()
        nome_cliente_entry.delete(0, tk.END)
        idade_cliente_entry.delete(0, tk.END)
        sexo_cliente_entry.delete(0, tk.END)
        endereco_cliente_entry.delete(0, tk.END)
        telefone_cliente_entry.delete(0, tk.END)

# Função para excluir um cliente na interface
def excluir_cliente_na_interface():
    selected_item = tree_clientes.selection()
    if selected_item:
        id_cliente = int(tree_clientes.item(selected_item, 'values')[0])
        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM clientes WHERE id=?', (id_cliente,))
        conn.commit()
        conn.close()
        listar_clientes_na_interface()

# Função para listar treinadores na interface
def listar_treinadores_na_interface():
    tree_treinadores.delete(*tree_treinadores.get_children())
    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM treinadores')
    treinadores = cursor.fetchall()
    conn.close()
    for treinador in treinadores:
        tree_treinadores.insert('', 'end', values=treinador)

# Função para adicionar um novo treinador na interface
def adicionar_treinador_na_interface():
    nome_treinador = nome_treinador_entry.get()
    especializacao = especializacao_entry.get()
    experiencia = experiencia_entry.get()
    numero_registro = numero_registro_entry.get()

    try:
        experiencia = int(experiencia)  # Converter a experiência para inteiro
        inserir_treinador(nome_treinador, especializacao, experiencia, numero_registro)
        listar_treinadores_na_interface()
        nome_treinador_entry.delete(0, tk.END)
        especializacao_entry.delete(0, tk.END)
        experiencia_entry.delete(0, tk.END)
        numero_registro_entry.delete(0, tk.END)
    except ValueError:
        print("Erro: A experiência deve ser um número inteiro não negativo.")


# Função para atualizar um treinador na interface
def atualizar_treinador_na_interface():
    selected_item = tree_treinadores.selection()
    if selected_item:
        id_treinador = int(tree_treinadores.item(selected_item, 'values')[0])
        nome_treinador = nome_treinador_entry.get()
        especializacao = especializacao_entry.get()
        experiencia = experiencia_entry.get()
        numero_registro = numero_registro_entry.get()

        atualizar_treinador(id_treinador, nome_treinador, especializacao, experiencia, numero_registro)
        listar_treinadores_na_interface()
        nome_treinador_entry.delete(0, tk.END)
        especializacao_entry.delete(0, tk.END)
        experiencia_entry.delete(0, tk.END)
        numero_registro_entry.delete(0, tk.END)


# Função para excluir um treinador na interface
def excluir_treinador_na_interface():
    selected_item = tree_treinadores.selection()
    if selected_item:
        id_treinador = int(tree_treinadores.item(selected_item, 'values')[0])
        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM treinadores WHERE id=?', (id_treinador,))
        conn.commit()
        conn.close()
        listar_treinadores_na_interface()

# Configuração da interface
root = tk.Tk()
root.title("Sistema de Gestão de Academias")

# Aba de Clientes
tab_control = ttk.Notebook(root)
clientes_tab = ttk.Frame(tab_control)
treinadores_tab = ttk.Frame(tab_control)

tab_control.add(clientes_tab, text="Clientes")
tab_control.add(treinadores_tab, text="Treinadores")

tab_control.pack(expand=1, fill='both')

# Tabela de Clientes
tree_clientes = ttk.Treeview(clientes_tab, column=("ID", "Nome", "Idade", "Sexo", "Endereço", "Telefone"), show="headings")
tree_clientes.heading("#1", text="ID")
tree_clientes.heading("#2", text="Nome")
tree_clientes.heading("#3", text="Idade")
tree_clientes.heading("#4", text="Sexo")
tree_clientes.heading("#5", text="Endereço")
tree_clientes.heading("#6", text="Telefone")
tree_clientes.pack()

# Campos para adicionar/atualizar cliente
nome_cliente_label = tk.Label(clientes_tab, text="Nome")
nome_cliente_label.pack()
nome_cliente_entry = tk.Entry(clientes_tab)
nome_cliente_entry.pack()

idade_cliente_label = tk.Label(clientes_tab, text="Idade")
idade_cliente_label.pack()
idade_cliente_entry = tk.Entry(clientes_tab)
idade_cliente_entry.pack()

sexo_cliente_label = tk.Label(clientes_tab, text="Sexo")
sexo_cliente_label.pack()
sexo_cliente_entry = tk.Entry(clientes_tab)
sexo_cliente_entry.pack()

endereco_cliente_label = tk.Label(clientes_tab, text="Endereço")
endereco_cliente_label.pack()
endereco_cliente_entry = tk.Entry(clientes_tab)
endereco_cliente_entry.pack()

telefone_cliente_label = tk.Label(clientes_tab, text="Telefone")
telefone_cliente_label.pack()
telefone_cliente_entry = tk.Entry(clientes_tab)
telefone_cliente_entry.pack()

# Botões para gerenciar clientes
adicionar_cliente_button = tk.Button(clientes_tab, text="Adicionar Cliente", command=adicionar_cliente_na_interface)
adicionar_cliente_button.pack()

atualizar_cliente_button = tk.Button(clientes_tab, text="Atualizar Cliente", command=atualizar_cliente_na_interface)
atualizar_cliente_button.pack()

excluir_cliente_button = tk.Button(clientes_tab, text="Excluir Cliente", command=excluir_cliente_na_interface)
excluir_cliente_button.pack()

# Tabela de Treinadores
tree_treinadores = ttk.Treeview(treinadores_tab, column=("ID", "Nome", "Especialização", "Experiência", "Número de Registro"), show="headings")
tree_treinadores.heading("#1", text="ID")
tree_treinadores.heading("#2", text="Nome")
tree_treinadores.heading("#3", text="Especialização")
tree_treinadores.heading("#4", text="Experiência")
tree_treinadores.heading("#5", text="Número de Registro")
tree_treinadores.pack()

# Campos para adicionar/atualizar treinador
nome_treinador_label = tk.Label(treinadores_tab, text="Nome")
nome_treinador_label.pack()
nome_treinador_entry = tk.Entry(treinadores_tab)
nome_treinador_entry.pack()

especializacao_label = tk.Label(treinadores_tab, text="Especialização")
especializacao_label.pack()
especializacao_entry = tk.Entry(treinadores_tab)
especializacao_entry.pack()

experiencia_label = tk.Label(treinadores_tab, text="Experiência")
experiencia_label.pack()
experiencia_entry = tk.Entry(treinadores_tab)
experiencia_entry.pack()

numero_registro_label = tk.Label(treinadores_tab, text="Número de Registro")
numero_registro_label.pack()
numero_registro_entry = tk.Entry(treinadores_tab)
numero_registro_entry.pack()

# Botões para gerenciar treinadores
adicionar_treinador_button = tk.Button(treinadores_tab, text="Adicionar Treinador", command=adicionar_treinador_na_interface)
adicionar_treinador_button.pack()

atualizar_treinador_button = tk.Button(treinadores_tab, text="Atualizar Treinador", command=atualizar_treinador_na_interface)
atualizar_treinador_button.pack()

excluir_treinador_button = tk.Button(treinadores_tab, text="Excluir Treinador", command=excluir_treinador_na_interface)
excluir_treinador_button.pack()

listar_clientes_na_interface()
listar_treinadores_na_interface()

root.mainloop()