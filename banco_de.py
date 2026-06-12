import sqlite3

conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

id_aluno = 1 

cursor.execute(
        "DELET FROM Alunos WHERE id = ?",
        (id_aluno,)
)

conexao.commit()

if cursor.execute 
