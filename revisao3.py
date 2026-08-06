import sqlite3 

def criar():
    try:
        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()

        
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cinemas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome_unidade TEXT,
            bairro TEXT
        )
        """)

        nome = input("Nome do bairro: ")
        academia = input("Nome da academia: ")

        cursor.execute(
            "INSERT INTO bairro(nome_unidade, bairro) VALUES (?, ?)",
            (nome, bairro)
        )
        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro:", erro)

def criar2():
    try:
        conexao = sqlite3.connect("cinema.db")
        cursor = conexao.cursor()
        
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS salas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome INTEGER,
            mensalidade INTEGER,
            id_academia INTEGER,
            FOREIGN KEY(id_academia) REFERENCES academia(id)
        )
        ''') 

        nome = input("Nome: ")
        academia = input("mensalidade: ")
        id_academia = int(input("Nome do id: "))

        cursor.execute(
            "INSERT INTO alunos(nome, mensalidade, id_academia) VALUES (?, ?, ?)",
            (nome, mensalidade, id_academia)
        )
        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro:", erro)




