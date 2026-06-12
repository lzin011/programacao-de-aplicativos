import sqlite3

conexao = sqlite3.connect("esclo_demonstração.db")
cursor = conexao.cursor()
cursor.execute(''' select * from alunos ''')
alunos = cursor.fetchall()
if not alunos:
    print("nenhum alunos cadastrado")
else: 
    for aluno in alunos: 
        print(f"nome = {alunos[0]}, idade = {aluno[1]}")
conexao.close()
