import sqlite3 
def cadastrar():
    try:
        conexao = sqlite3.connect("hospital.db")
        conexao.execute("PRAGMA foreign_keys = ON")
        cursor = conexao.cursor()
    

        cursor.execute('''CREATE TABLE IF NOT EXISTS hospitais (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            cidade TEXT NOT NULL)''')


        cursor.execute('''
                CREATE TABLE IF NOT EXISTS medicos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                crm TEXT NOT NULL,
                id_hospital INTEGER NOT NULL,
                FOREIGN KEY (id_hospital) REFERENCES hospitais(id)
            )
        ''')
        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro ao criar o banco:", erro)

def inserir():
    try:
        nome = input("Nome do hospital: ")
        cidade = input("Cidade: ")
        cursor.execute("INSERT INTO hospitais(nome, cidade) VALUES (?, ?)", (nome, cidade))
        conexao.commit()

            
        nome = input("Nome do médico: ")
        registro_medico = input("registro: ")
        id_hospital = int(input("ID do hospital: "))


        cursor.execute("SELECT * FROM hospitais WHERE id = ?", (id_hospital,))

        if cursor.fetchone():
            cursor.execute(
                "INSERT INTO medicos(nome, registro_medico, id_hospital) VALUES (?, ?, ?)",
                (nome, registro_medico, id_hospital)
                )
            conexao.commit()
            print("Médico cadastrado!")
        else:
            print("Erro: Hospital não existe.")
    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()

