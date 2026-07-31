import sqlite3

def vincular():
    nome = input("nome do aluno: ")
    # se o usuario digitar "turma b" em vez do numero do id, o sistema quebra.
    # o try/execept abaixo falhou em capturar esse erro. qual o problema?
    # o problema era que não estava mostrando esse erro e iria continuar rodando sem aparace.
    try:
        id_turma = int(input("digite o id numerico da nossa turma: "))
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute ("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", (nome, id_turma))
        conexao.commit()
    except ( ValueError, sqlite3.Error) as e:
        print("Erro", e)
    finally:
        print("codigo encerrado")
            conexao.close