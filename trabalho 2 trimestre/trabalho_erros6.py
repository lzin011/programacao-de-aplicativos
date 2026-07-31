import sqlite3

def buscar(id_prof):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #o python reclama de "Incorrect number of bindings"
    #estamos passando a variavel, por que ocorre o erro?
    #O erro ocorre porque o método cursor.execute() espera que os valores correspondentes aos ? da consulta SQL sejam passados em uma sequência, como uma tupla ou uma lista.

    cursor.execute("SELECT  nome FROM professores WHERE id = ?", (id_prof,)) # virgula obrigatoria (com base na resposta acima).
    resultado = cursor.fetchall()
    print(resultado)
    conexao.close()