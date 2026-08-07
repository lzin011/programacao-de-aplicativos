import sqlite3

def criar():
    try:
        conexao = sqlite3.connect("hotelaria.db")
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS cinemas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cidade TEXT
        )
        """)
        nome_do_hotel = input("Nome do hotel: ")
        cidade = input("Nome da cidade: ")

        cursor.execute(
            "INSERT INTO nome(nome, cidade) VALUES (?, ?)",
            (nome, cidade)
        )
        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro:", erro)

def criar2():
    try:
        conexao = sqlite3.connect("hotelaria.db")
        cursor = conexao.cursor()

        cursor.execute("PRAGMA foreign_keys = ON")

        cursor.execute('''
        CREATE TABLE IF NOT EXISTS salas(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            numero INTEGER,
            preco_diaria INTEGER,
            id_hotel INTEGER,
            FOREIGN KEY(id_hotel) REFERENCES hotel(id)
        )
        ''')

        numero = input("Numero do hotel: ")
        preco_diaria = input("Preço da diaria: ")

         cursor.execute(
            "INSERT INTO nome(numero, preco_diaria) VALUES (?, ?)",
            (numero, preco_diaria, )
        )
        conexao.commit()

    except sqlite3.Error as erro:
        print("Erro:", erro)

def cadastrar():
    try:
        numero = int(input("Número do quarto: "))
        tipo = input("Tipo do quarto: ")
        capacidade = int(input("Capacidade: "))
        diaria = float(input("Valor da diária: "))

        if cursor.fetchall():
            cursor.execute('''
                    INSERT INTO salas(numero_sala, tipo, capacidade, diaria)
                    VALUES (?, ?, ?, ?)
                ''', (numero, tipo, capacidade, diaria))

            conexao.commit()
            print("hotel todo cadastar: ")

            cursor.execute("SELECT * FROM hotel")
            hotel = cursor.fetchall()

            for hotel in hoteis:
                print(hotel)

                else:
            print("hotel não encontrado: ")

    except ValueError:
        print("Digite apenas números nos campos numéricos.")

    except sqlite3.Error as erro:
        print("Erro:", erro)

    finally:
        conexao.close()




