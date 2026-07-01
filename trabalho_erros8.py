import sqlite3

def cadstrar_professores(nome, cpf):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #o sistema aceita cadastrar dois professores com o mesmo cpf.
    #como restringir isso direito na estrutura da tabela abaixo?
    # nao tem como, por que, cpf é unico.

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS professores (
            id INTENGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            cpf )''')