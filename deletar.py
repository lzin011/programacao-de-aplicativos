def deletar():


    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    id_aluno = int(input(" Qual ID deseja deletar: " ))

    # Verifica se o aluno existe
    cursor.execute(f'''SELECT id FROM Alunos WHERE Id = {id_aluno}''')
    aluno = cursor.fetchone()

    if not aluno:
        print ("Aluno não encontrado ")
    else:
        cursor.execute(f'''DELETE FROM Alunos WHERE Id = {id_aluno}''')
        conexao.commit()
        print("aluno deletado")

        conexao.close()

alterar()