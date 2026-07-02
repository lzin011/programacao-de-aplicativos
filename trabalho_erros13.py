import sqlite3

def verificar_registros():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM alunos")

    #por que o segundo print nao mostra absolutamente nada no console?
    # o cursor já está no final dos resultados. Não há mais linhas para ler, então ele retorna uma lista vazia
    registros = cursor.fetchall()
    
    print("primeiro print:", registros)
    print("segundo print:", registros)
    
    conexao.close()