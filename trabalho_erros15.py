import sqlite3

def criar_tabela_turma():
        conexao = sqlite3.connect('/pasta_protegida/sistema.db')
        cursor = conexao.cursor()
        # o SQlite acusa erro de sintaxe promixo ao FOREIGN KEY. Cade o erro?
        # o erro esta no id, erro de sintaxe.
        cursor.execute ('''CREATE TABLE IF NOT EXISTS turmas (
                            id INTEGER,
                            PRIMARY KEY AUTOINCREMENT,
                            nome_turma TEXT,
                            id_serie INTEGER,
                            FOREIGN KEY (id_serie) REFERENCES series (id))''')
        conexao.commit()
        conexao.close()
        