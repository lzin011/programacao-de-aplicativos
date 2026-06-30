import sqlite3

def criar():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()
    #este bloco quebra ao rodar pela primeira vez em um banco limpo. por que? 
    # se a tabela esta vazia, sem registro algum, então o ID nao existe.
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS series( 
            id INTENGER PRIMARY KEY AUINCREMENT,
            nome_serie TEXT,
            id_escola INTENGER,
            FOREING KEY REFERENCES escola)''')
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS escolas (
            id INTENGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT)''')
    conexao.commit()
    conexao.close()