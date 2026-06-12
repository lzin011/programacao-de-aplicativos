conexao = sqlite3.connect("escola_demonstracao.db")
cursor = conexao.cursor()

id_aluno = 1

cursor.execute("SELECT * FROM Alunos WHERE id = ?", (id_aluno,))
print("\nantes da alteração:")
print(cursor.fetchone())


cursor.execute('''
    UPDATE Alunos
    SET nome = ?, cpf = ?
    WHERE id = ?
''', (novo_nome, novo_cpf, id_aluno))
novo_nome = "João Pedro da Silva"
novo_cpf = "123.456.789-00"
conexao.commit()

cursor.execute("SELECT * FROM Alunos WHERE id = ?", (id_aluno,))
print("\ndepois da alteração:")
print(cursor.fetchone())

conexao.close()