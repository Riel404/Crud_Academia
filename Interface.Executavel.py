import sqlite3
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


# Função para cadastrar um cliente no banco de dados com tratamento de exceções
def inserir_cliente(nome, idade, sexo, endereco, telefone):
    try:
        if not nome or nome[0].isdigit():
            messagebox.showerror("Erro ao inserir cliente", "Favor digitar no campo Nome começando com letras.")
            raise ValueError("Favor digitar no campo Nome começando com letras.")

        if not idade.isdigit():
            messagebox.showerror("Erro ao inserir cliente", "A idade deve ser um número inteiro.")
            raise ValueError("A idade deve ser um número inteiro.")
        idade = int(idade)
        if idade < 0:
            messagebox.showerror("Erro ao inserir cliente", "A idade deve ser um número inteiro não negativo.")
            raise ValueError("A idade deve ser um número inteiro não negativo.")

        sexo = sexo.lower()
        if sexo not in ['m', 'f', 'masculino', 'feminino']:
            messagebox.showerror("Erro ao inserir cliente", "Digite M para masculino ou F para feminino.")
            raise ValueError("Digite M para masculino ou F para feminino.")
        if sexo.startswith('m'):
            sexo = 'M'
        elif sexo.startswith('f'):
            sexo = 'F'

        if not endereco:
            messagebox.showerror("Erro ao inserir cliente", "O endereço não pode estar vazio.")
            raise ValueError("O endereço não pode estar vazio.")

        if len(telefone) < 8:
            messagebox.showerror("Erro ao adicionar cliente",
                                 "O telefone deve ser uma string com pelo menos 8 caracteres.")
            raise ValueError("Digite um telefone com pelo menos 8 dígitos.")

        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO clientes (nome, idade, sexo, endereco, telefone) VALUES (?, ?, ?, ?, ?)',
                       (nome, idade, sexo, endereco, telefone))
        conn.commit()
        conn.close()
        print("Cliente cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir cliente: {e}")
        messagebox.showerror("Erro ao inserir cliente", str(e))
    except ValueError as ve:
        print(f"Erro ao inserir cliente: {ve}")
        messagebox.showerror("Erro ao inserir cliente", str(ve))


# Função para adicionar um novo cliente na interface
def adicionar_cliente_na_interface():
    nome = nome_cliente_entry.get()
    idade = idade_cliente_entry.get()
    sexo = sexo_cliente_entry.get()
    endereco = endereco_cliente_entry.get()
    telefone = telefone_cliente_entry.get()

    campos_inconsistentes = []

    if not nome or nome[0].isdigit():
        campos_inconsistentes.append("Nome (deve começar com letras)")

    if not idade.isdigit() or int(idade) < 0:
        campos_inconsistentes.append("Idade (deve ser um número inteiro não negativo)")

    sexo = sexo.lower()
    if sexo not in ['m', 'f', 'masculino', 'feminino']:
        campos_inconsistentes.append("Sexo (M para masculino, F para feminino)")

    if not endereco:
        campos_inconsistentes.append("Endereço (não pode estar vazio)")

    if len(telefone) < 8:
        campos_inconsistentes.append("Telefone (pelo menos 8 dígitos)")

    if campos_inconsistentes:
        messagebox.showinfo("Atenção", f"Campos inconsistentes: {', '.join(campos_inconsistentes)}")
    else:
        try:
            inserir_cliente(nome, idade, sexo, endereco, telefone)
            listar_clientes_na_interface()
            messagebox.showinfo("Sucesso", "Seu cadastro foi realizado com sucesso!")
            limpar_campos_cliente()  # Limpar campos após adicionar com sucesso
        except:
            messagebox.showerror("Erro", "Ocorreu um erro ao adicionar o cliente. Por favor, tente novamente.")


def limpar_campos_cliente():
    nome_cliente_entry.delete(0, 'end')
    idade_cliente_entry.delete(0, 'end')
    sexo_cliente_entry.delete(0, 'end')
    endereco_cliente_entry.delete(0, 'end')
    telefone_cliente_entry.delete(0, 'end')


# Função para cadastrar um treinador no banco de dados com tratamento de exceções
def inserir_treinador(nome, especializacao, experiencia, numero_registro):
    try:
        if not nome or nome[0].isdigit():
            messagebox.showerror("Erro ao inserir treinador", "Favor digitar no campo Nome começando com letras.")
            raise ValueError("Favor digitar no campo Nome começando com letras.")

        if not especializacao:
            messagebox.showerror("Erro ao inserir treinador", "Especialização não pode estar vazia.")
            raise ValueError("Especialização não pode estar vazia.")

        if not experiencia.isdigit():
            messagebox.showerror("Erro ao inserir treinador", "A experiência deve ser um número inteiro não negativo.")
            raise ValueError("A experiência deve ser um número inteiro não negativo.")
        experiencia = int(experiencia)
        if experiencia < 0:
            messagebox.showerror("Erro ao inserir treinador", "A experiência deve ser um número inteiro não negativo.")
            raise ValueError("A experiência deve ser um número inteiro não negativo.")

        if not isinstance(numero_registro, str) or len(numero_registro) < 6:
            messagebox.showerror("Erro ao inserir treinador", "O número de registro não pode ter menos de 6 dígitos.")
            raise ValueError("O número de registro não pode ter menos de 6 dígitos..")

        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO treinadores (nome, especializacao, experiencia, numero_registro) VALUES (?, ?, ?, ?)',
            (nome, especializacao, experiencia, numero_registro))
        conn.commit()
        conn.close()
        print("Treinador cadastrado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao inserir treinador: {e}")
        messagebox.showerror("Erro ao inserir treinador", str(e))
    except ValueError as ve:
        print(f"Erro ao inserir treinador: {ve}")
        messagebox.showerror("Erro ao inserir treinador", str(ve))


def adicionar_treinador_na_interface():
    nome_treinador = nome_treinador_entry.get()
    especializacao = especializacao_entry.get()
    experiencia = experiencia_entry.get()
    numero_registro = numero_registro_entry.get()

    campos_inconsistentes = []

    if not nome_treinador or nome_treinador[0].isdigit():
        campos_inconsistentes.append("Nome (deve começar com letras)")

    if not especializacao:
        campos_inconsistentes.append("Especialização (não pode estar vazia)")

    if not experiencia.isdigit() or int(experiencia) < 0:
        campos_inconsistentes.append("Experiência (deve ser um número inteiro não negativo)")

    if not isinstance(numero_registro, str) or len(numero_registro) < 6:
        campos_inconsistentes.append("Número de Registro (pelo menos 6 dígitos)")

    if campos_inconsistentes:
        messagebox.showinfo("Atenção", f"Campos inconsistentes: {', '.join(campos_inconsistentes)}")
    else:
        try:
            inserir_treinador(nome_treinador, especializacao, experiencia, numero_registro)
            listar_treinadores_na_interface()
            messagebox.showinfo("Sucesso", "Seu cadastro foi realizado com sucesso!")
            limpar_campos_treinador()  # Limpar campos após adicionar com sucesso
        except:
            messagebox.showerror("Erro", "Ocorreu um erro ao adicionar o treinador. Por favor, tente novamente.")


# Função para limpar campos de texto para treinadores
def limpar_campos_treinador():
    nome_treinador_entry.delete(0, 'end')
    especializacao_entry.delete(0, 'end')
    experiencia_entry.delete(0, 'end')
    numero_registro_entry.delete(0, 'end')


# Função para atualizar informações de um cliente com tratamento de exceções
def atualizar_cliente(id, nome=None, idade=None, sexo=None, endereco=None, telefone=None):
    try:
        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()

        # Verifica quais campos devem ser atualizados
        update_fields = []
        if nome:
            if not nome or nome[0].isdigit():
                messagebox.showerror("Erro ao atualizar cliente", "Favor digitar no campo Nome começando com letras.")
                raise ValueError("Favor digitar no campo Nome começando com letras.")
            update_fields.append(f"nome = '{nome}'")
        if idade:
            if not idade.isdigit():
                messagebox.showerror("Erro ao atualizar cliente", "A idade deve ser um número inteiro.")
                raise ValueError("A idade deve ser um número inteiro.")
            idade = int(idade)
            if idade < 0:
                messagebox.showerror("Erro ao atualizar cliente", "A idade deve ser um número inteiro não negativo.")
                raise ValueError("A idade deve ser um número inteiro não negativo.")
            update_fields.append(f"idade = {idade}")
        if sexo:
            sexo = sexo.lower()
            if sexo not in ['m', 'f', 'masculino', 'feminino']:
                messagebox.showerror("Erro ao atualizar cliente", "Digite M para masculino ou F para feminino.")
                raise ValueError("Digite M para masculino ou F para feminino.")
            if sexo.startswith('m'):
                sexo = 'M'
            elif sexo.startswith('f'):
                sexo = 'F'
            update_fields.append(f"sexo = '{sexo}'")
        if endereco:
            update_fields.append(f"endereco = '{endereco}'")
        if telefone:
            if len(telefone) < 8:
                messagebox.showerror("Erro ao adicionar cliente",
                                     "O telefone deve ser uma string com pelo menos 8 caracteres.")
                raise ValueError("Digite um telefone com pelo menos 8 dígitos.")
            update_fields.append(f"telefone = '{telefone}'")

        if not update_fields:
            raise ValueError("Nenhum campo de atualização fornecido.")

        # Monta a consulta SQL para atualização
        update_query = f"UPDATE clientes SET {', '.join(update_fields)} WHERE id = {id}"
        cursor.execute(update_query)
        conn.commit()
        conn.close()
        print("Cliente atualizado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar cliente: {e}")
        messagebox.showerror("Erro ao atualizar cliente", str(e))
    except ValueError as ve:
        print(f"Erro ao atualizar cliente: {ve}")
        messagebox.showerror("Erro ao atualizar cliente", str(ve))


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

    try:
        atualizar_cliente(id_cliente, nome, idade, sexo, endereco, telefone)
        listar_clientes_na_interface()
        messagebox.showinfo("Sucesso", "Seu cadastro foi atualizado com sucesso!")
    except:
        messagebox.showerror("Erro", "Verifique os campos e tente novamente.")


# Função para atualizar informações de um treinador com tratamento de exceções
def atualizar_treinador(id, nome=None, especializacao=None, experiencia=None, numero_registro=None):
    try:
        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()

        # Verifica quais campos devem ser atualizados
        update_fields = []
        if nome:
            if not nome or nome[0].isdigit():
                messagebox.showerror("Erro ao atualizar treinador", "Favor digitar no campo Nome começando com letras.")
                raise ValueError("Favor digitar no campo Nome começando com letras.")
            update_fields.append(f"nome = '{nome}'")
        if especializacao:
            update_fields.append(f"especializacao = '{especializacao}'")
        if experiencia:
            if not experiencia.isdigit():
                messagebox.showerror("Erro ao atualizar treinador",
                                     "A experiência deve ser um número inteiro não negativo.")
                raise ValueError("A experiência deve ser um número inteiro não negativo.")
            experiencia = int(experiencia)
            if experiencia < 0:
                messagebox.showerror("Erro ao atualizar treinador",
                                     "A experiência deve ser um número inteiro não negativo.")
                raise ValueError("A experiência deve ser um número inteiro não negativo.")
            update_fields.append(f"experiencia = {experiencia}")
        if numero_registro:
            if not isinstance(numero_registro, str) or len(numero_registro) < 6:
                messagebox.showerror("Erro ao atualizar treinador",
                                     "O número de registro não pode ter menos de 6 dígitos.")
                raise ValueError("O número de registro não pode ter menos de 6 dígitos.")
            update_fields.append(f"numero_registro = '{numero_registro}'")

        if not update_fields:
            raise ValueError("Nenhum campo de atualização fornecido.")

        # Monta a consulta SQL para atualização
        update_query = f"UPDATE treinadores SET {', '.join(update_fields)} WHERE id = {id}"
        cursor.execute(update_query)
        conn.commit()
        conn.close()
        print("Treinador atualizado com sucesso!")
    except sqlite3.Error as e:
        print(f"Erro ao atualizar treinador: {e}")
        messagebox.showerror("Erro ao atualizar treinador", str(e))
    except ValueError as ve:
        print(f"Erro ao atualizar treinador: {ve}")
        messagebox.showerror("Erro ao atualizar treinador", str(ve))


# Função para atualizar um treinador na interface
def atualizar_treinador_na_interface():
    selected_item = tree_treinadores.selection()
    if selected_item:
        id_treinador = int(tree_treinadores.item(selected_item, 'values')[0])
        nome_treinador = nome_treinador_entry.get()
        especializacao = especializacao_entry.get()
        experiencia = experiencia_entry.get()
        numero_registro = numero_registro_entry.get()

        campos_atualizacao = {
            "nome": nome_treinador,
            "especializacao": especializacao,
            "experiencia": experiencia,
            "numero_registro": numero_registro
        }

        campos_atualizados = {campo: valor for campo, valor in campos_atualizacao.items() if valor}

        if not campos_atualizados:
            messagebox.showerror("Erro ao atualizar treinador", "Nenhum campo de atualização fornecido.")
        else:
            atualizar_treinador(id_treinador, **campos_atualizados)
            listar_treinadores_na_interface()
            nome_treinador_entry.delete(0, tk.END)
            especializacao_entry.delete(0, tk.END)
            experiencia_entry.delete(0, tk.END)
            numero_registro_entry.delete(0, tk.END)
    try:
        atualizar_treinador(id_treinador, nome_treinador, especializacao, experiencia, numero_registro)
        listar_treinadores_na_interface()
        messagebox.showinfo("Sucesso", "Seu cadastro foi atualizado com sucesso!")
    except:
        messagebox.showerror("Erro", "Verifique os campos e tente novamente.")


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
        raise ValueError(f"Erro ao excluir cliente: {e}")


# Função para excluir um cliente na interface
def excluir_cliente_na_interface():
    selected_item = tree_clientes.selection()
    if selected_item:
        confirmation = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir?")
        if confirmation:
            id_cliente = int(tree_clientes.item(selected_item, 'values')[0])
            excluir_cliente(id_cliente)
            listar_clientes_na_interface()
            messagebox.showinfo("Sucesso", "Cliente excluído com sucesso!")


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
        raise ValueError(f"Erro ao excluir treinador: {e}")


# Função para excluir um treinador na interface
def excluir_treinador_na_interface():
    selected_item = tree_treinadores.selection()
    if selected_item:
        confirmation = messagebox.askyesno("Confirmação", "Tem certeza que deseja excluir?")
        if confirmation:
            id_treinador = int(tree_treinadores.item(selected_item, 'values')[0])
            excluir_treinador(id_treinador)
            listar_treinadores_na_interface()
            messagebox.showinfo("Sucesso", "Treinador excluído com sucesso!")


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


# Função para pesquisar clientes na interface
def pesquisar_clientes_na_interface():
    texto_nome = nome_cliente_entry.get()
    texto_idade = idade_cliente_entry.get()
    texto_sexo = sexo_cliente_entry.get()
    texto_endereco = endereco_cliente_entry.get()
    texto_telefone = telefone_cliente_entry.get()

    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()

    # Consulta SQL para pesquisar clientes baseada nos campos preenchidos
    query = "SELECT * FROM clientes WHERE nome LIKE ? AND idade LIKE ? AND sexo LIKE ? AND endereco LIKE ? AND telefone LIKE ?"
    cursor.execute(query,
                   (texto_nome + "%", texto_idade + "%", texto_sexo + "%", texto_endereco + "%", texto_telefone + "%"))

    clientes = cursor.fetchall()
    conn.close()

    # Limpar tabela antes de exibir resultados
    tree_clientes.delete(*tree_clientes.get_children())

    # Exibir resultados na tabela
    for cliente in clientes:
        tree_clientes.insert('', 'end', values=cliente)


# Função para pesquisar clientes na interface
def pesquisar_clientes_na_interface():
    texto_nome = nome_cliente_entry.get()
    texto_idade = idade_cliente_entry.get()
    texto_sexo = sexo_cliente_entry.get()
    texto_endereco = endereco_cliente_entry.get()
    texto_telefone = telefone_cliente_entry.get()

    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()

    # Consulta SQL para pesquisar clientes baseada nos campos preenchidos
    query = "SELECT * FROM clientes WHERE nome LIKE ? AND idade LIKE ? AND sexo LIKE ? AND endereco LIKE ? AND telefone LIKE ?"
    cursor.execute(query,
                   (texto_nome + "%", texto_idade + "%", texto_sexo + "%", texto_endereco + "%", texto_telefone + "%"))

    clientes = cursor.fetchall()
    conn.close()

    # Limpar tabela antes de exibir resultados
    tree_clientes.delete(*tree_clientes.get_children())

    # Exibir resultados na tabela
    for cliente in clientes:
        tree_clientes.insert('', 'end', values=cliente)


# Função para pesquisar treinadores na interface
def pesquisar_treinadores_na_interface():
    texto_nome = nome_treinador_entry.get()
    texto_especializacao = especializacao_entry.get()
    texto_experiencia = experiencia_entry.get()
    texto_numero_registro = numero_registro_entry.get()

    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()

    # Consulta SQL para pesquisar treinadores baseada nos campos preenchidos
    query = "SELECT * FROM treinadores WHERE nome LIKE ? AND especializacao LIKE ? AND experiencia LIKE ? AND numero_registro LIKE ?"
    cursor.execute(query,
                   (texto_nome + "%", texto_especializacao + "%", texto_experiencia + "%", texto_numero_registro + "%"))

    treinadores = cursor.fetchall()
    conn.close()

    # Limpar tabela antes de exibir resultados
    tree_treinadores.delete(*tree_treinadores.get_children())

    # Exibir resultados na tabela
    for treinador in treinadores:
        tree_treinadores.insert('', 'end', values=treinador)


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


# Função para pesquisar treinadores na interface
def pesquisar_treinadores_na_interface():
    texto_nome = nome_treinador_entry.get()
    texto_especializacao = especializacao_entry.get()
    texto_experiencia = experiencia_entry.get()
    texto_numero_registro = numero_registro_entry.get()

    conn = sqlite3.connect('academia.db')
    cursor = conn.cursor()

    # Consulta SQL para pesquisar treinadores baseada nos campos preenchidos
    query = "SELECT * FROM treinadores WHERE nome LIKE ? AND especializacao LIKE ? AND experiencia LIKE ? AND numero_registro LIKE ?"
    cursor.execute(query,
                   (texto_nome + "%", texto_especializacao + "%", texto_experiencia + "%", texto_numero_registro + "%"))

    treinadores = cursor.fetchall()
    conn.close()

    # Limpar tabela antes de exibir resultados
    tree_treinadores.delete(*tree_treinadores.get_children())

    # Exibir resultados na tabela
    for treinador in treinadores:
        tree_treinadores.insert('', 'end', values=treinador)


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
tree_clientes = ttk.Treeview(clientes_tab, column=("ID", "Nome", "Idade", "Sexo", "Endereço", "Telefone"),
                             show="headings")
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

# Botão para pesquisar clientes
pesquisar_clientes_button = tk.Button(clientes_tab, text="Pesquisar Clientes", command=pesquisar_clientes_na_interface)
pesquisar_clientes_button.pack()

# Evento para chamar a função de pesquisa de clientes ao pressionar a tecla "Enter" nos campos de pesquisa
nome_cliente_entry.bind('<Return>', lambda event: pesquisar_clientes_na_interface())
idade_cliente_entry.bind('<Return>', lambda event: pesquisar_clientes_na_interface())
sexo_cliente_entry.bind('<Return>', lambda event: pesquisar_clientes_na_interface())
endereco_cliente_entry.bind('<Return>', lambda event: pesquisar_clientes_na_interface())
telefone_cliente_entry.bind('<Return>', lambda event: pesquisar_clientes_na_interface())

# Tabela de Treinadores
tree_treinadores = ttk.Treeview(treinadores_tab,
                                column=("ID", "Nome", "Especialização", "Experiência", "Número de Registro"),
                                show="headings")
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
adicionar_treinador_button = tk.Button(treinadores_tab, text="Adicionar Treinador",
                                       command=adicionar_treinador_na_interface)
adicionar_treinador_button.pack()

atualizar_treinador_button = tk.Button(treinadores_tab, text="Atualizar Treinador",
                                       command=atualizar_treinador_na_interface)
atualizar_treinador_button.pack()

excluir_treinador_button = tk.Button(treinadores_tab, text="Excluir Treinador", command=excluir_treinador_na_interface)
excluir_treinador_button.pack()

# Botão para pesquisar treinadores
pesquisar_treinadores_button = tk.Button(treinadores_tab, text="Pesquisar Treinadores",
                                         command=pesquisar_treinadores_na_interface)
pesquisar_treinadores_button.pack()

# Evento para chamar a função de pesquisa de treinadores ao pressionar a tecla "Enter" nos campos de pesquisa
nome_treinador_entry.bind('<Return>', lambda event: pesquisar_treinadores_na_interface())
especializacao_entry.bind('<Return>', lambda event: pesquisar_treinadores_na_interface())
experiencia_entry.bind('<Return>', lambda event: pesquisar_treinadores_na_interface())
numero_registro_entry.bind('<Return>', lambda event: pesquisar_treinadores_na_interface())

listar_clientes_na_interface()
listar_treinadores_na_interface()

root.mainloop()