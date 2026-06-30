import sqlite3 

def inicializar():
    conexao = sqlite3.connect ('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute('''
    CREAT TABLE IF NOT EXISTS escolas(
        id INTENGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL)''')

# o banco não esta salvando as alterações. por que? 
# por que nao tinha o commit.

    conexao.commit()
    conexao.close()


