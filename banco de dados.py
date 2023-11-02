import sqlite3


# Função para criar a tabela de clientes no banco de dados com tratamento de exceções
def criar_tabela_clientes():
    try:
        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                idade INTEGER,
                sexo TEXT,
                endereco TEXT,
                telefone TEXT
            )
        ''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela de clientes: {e}")

# Função para criar a tabela de treinadores no banco de dados com tratamento de exceções
def criar_tabela_treinadores():
    try:
        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS treinadores (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT,
                especializacao TEXT,
                experiencia INTEGER,
                numero_registro TEXT
            )
        ''')
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        print(f"Erro ao criar tabela de treinadores: {e}")

# Função para inserir um cliente no banco de dados com tratamento de exceções
def inserir_cliente(nome, idade, sexo, endereco, telefone):
    try:
        if not isinstance(idade, int) or idade < 0:
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
        if not isinstance(experiencia, int) or experiencia < 0:
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
def atualizar_cliente(id, nome, idade, sexo, endereco, telefone):
    try:
        if not isinstance(id, int) or id < 1:
            raise ValueError("ID do cliente inválido.")
        if not isinstance(idade, int) or idade < 0:
            raise ValueError("A idade deve ser um número inteiro não negativo.")
        if not isinstance(sexo, str) or len(sexo) != 1:
            raise ValueError("O sexo deve ser uma única letra.")
        if not isinstance(endereco, str):
            raise ValueError("O endereço deve ser uma string.")
        if not isinstance(telefone, str) or len(telefone) < 8:
            raise ValueError("O telefone deve ser uma string com pelo menos 8 caracteres.")

        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE clientes SET nome=?, idade=?, sexo=?, endereco=?, telefone=? WHERE id=?',
                       (nome, idade, sexo, endereco, telefone, id))
        conn.commit()
        conn.close()
        print("Cliente atualizado com sucesso!")
    except (sqlite3.Error, ValueError) as e:
        print(f"Erro ao atualizar cliente: {e}")

# Função para atualizar informações de um treinador com tratamento de exceções
def atualizar_treinador(id, nome, especializacao, experiencia, numero_registro):
    try:
        if not isinstance(id, int) or id < 1:
            raise ValueError("ID do treinador inválido.")
        if not isinstance(experiencia, int) or experiencia < 0:
            raise ValueError("A experiência deve ser um número inteiro não negativo.")
        if not isinstance(numero_registro, str) or len(numero_registro) < 6:
            raise ValueError("O número de registro deve ter pelo menos 6 caracteres.")

        conn = sqlite3.connect('academia.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE treinadores SET nome=?, especializacao=?, experiencia=?, numero_registro=? WHERE id=?',
                       (nome, especializacao, experiencia, numero_registro, id))
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

# Função principal com tratamento de exceções
def menu_principal():
    try:
        criar_tabela_clientes()
        criar_tabela_treinadores()

        while True:
            print("\nSistema de Gestão de Academias")
            print("1. Cadastrar Cliente")
            print("2. Cadastrar Treinador")
            print("3. Listar Clientes")
            print("4. Listar Treinadores")
            print("5. Atualizar Cliente")
            print("6. Atualizar Treinador")
            print("7. Excluir Cliente")
            print("8. Excluir Treinador")
            print("0. Sair")

            opcao = input("Escolha uma opção: ")

            if opcao == '1':
                nome = input("Nome do Cliente: ")
                idade = int(input("Idade: "))
                sexo = input("Sexo (M/F): ")
                endereco = input("Endereço: ")
                telefone = input("Telefone: ")
                inserir_cliente(nome, idade, sexo, endereco, telefone)

            elif opcao == '2':
                nome = input("Nome do Treinador: ")
                especializacao = input("Especialização: ")
                experiencia = int(input("Experiência: "))
                numero_registro = input("Número de Registro: ")
                inserir_treinador(nome, especializacao, experiencia, numero_registro)

            elif opcao == '3':
                print("\nClientes Cadastrados:")
                listar_clientes()

            elif opcao == '4':
                print("\nTreinadores Cadastrados:")
                listar_treinadores()

            elif opcao == '5':
                listar_clientes()
                id_cliente = int(input("Selecione o ID do Cliente que deseja atualizar: "))
                nome = input("Novo nome: ")
                idade = int(input("Nova idade: "))
                sexo = input("Novo sexo (M/F): ")
                endereco = input("Novo endereço: ")
                telefone = input("Novo telefone: ")
                atualizar_cliente(id_cliente, nome, idade, sexo, endereco, telefone)

            elif opcao == '6':
                listar_treinadores()
                id_treinador = int(input("Selecione o ID do Treinador que deseja atualizar: "))
                nome = input("Novo nome: ")
                especializacao = input("Nova especialização: ")
                experiencia = int(input("Nova experiência: "))
                numero_registro = input("Novo número de Registro: ")
                atualizar_treinador(id_treinador, nome, especializacao, experiencia, numero_registro)

            elif opcao == '7':
                listar_clientes()
                id_cliente = int(input("Selecione o ID do Cliente que deseja excluir: "))
                excluir_cliente(id_cliente)

            elif opcao == '8':
                listar_treinadores()
                id_treinador = int(input("Selecione o ID do Treinador que deseja excluir: "))
                excluir_treinador(id_treinador)

            elif opcao == '0':
                break

    except sqlite3.Error as e:
        print(f"Erro no banco de dados: {e}")

    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")



if __name__ == "__main__":
    menu_principal()

