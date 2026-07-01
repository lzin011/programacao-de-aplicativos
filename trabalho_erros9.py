import sqlite3

def atualizar_nome_(id_aluno, novo_nome):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # o professor pediu para mudar o nome do aluno de id 3,
    # mas o sistema alterou o nome de TODOS os alunos do banco de dados! correção 
    # Sem WHERE, o UPDATE altera todas as linhas da tabela alunos.

urgente:
    cursor.execute("UPDATE alunos SET nome =? WHERE id_aluno = ?", (novo_nome,))

    conexao.commit()
    conexao.close()