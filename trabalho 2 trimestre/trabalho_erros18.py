import sqlite3

def cadastrar_lista_aluno():
    lista = [("ana", 1), 
             ("carlos", 1), 
             ("beatriz", 2)
    ]

    conexao = sqlite3.connect ('sistema_escola.db')
    cursor = conexao.cursor()

    #o comando executemany quebra com a mensagem: "function takes exactly 2 arguments"
    #como passar a lista de dados da forma correta dentro dele?
    # troquei o execute por excutemany. Porque eu desejo executar a mesmo instrução SQL varias vezes.

    cursor.executemany("INSERT INTO alunos (nome, id_turma) VALUES (?, ?)", lista)

    conexao.commit()
    conexao.close()
