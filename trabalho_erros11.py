import sqlite3

def listar_alunos_e_turmas():
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # o relatorio roda, mas repete os dados erroneamnte em formato de matriz cruzada
    # porque falta definir a regra de colagem (vínculo). conserte o comando SQL:
    
    cursor.execute('''SELECT alunos.nome, turmas.nome_turma 
                    FROM alunos 
                    INNER JOIN turmas
                    ON aluno.id_turma = turma.id''')

    for linha in cursor.fetchall():
        print(f"Aluno: {linha[0]} | turma: {linha[1]}")
        
    conexao.close()