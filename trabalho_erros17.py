import sqlite3

def inserir_professor(nome, materia, cpf):
    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        # existe um erro de digitaçao no comando sql (inserto)
        # por que o programa mostra "CPF ja cadastrando" em vez de avisar sobre o erro de sintexe?
        cursor.execute(" INSERTO INTO professores (nome, materia, cpf) VALUES (?,?,?)", (nome, materia, cpf))
        conexao.commit()
    except slite3.Error:
        print("Erro: este CPF ja esta cadastrando no sistema! ")
        finally:
            conexao.close()