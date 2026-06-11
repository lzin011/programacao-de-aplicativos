import sqlite3
conexao = sqlite3.connect ('escola.db')
cursor = conexao.cursor()
cursor.execute ('''CREATE TABLE IF NOT EXISTS alunos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,
                    turma TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL
                    )''')


nome_aluno = input("NOME: ")
telefone_aluno = input("TELEFONE: ")
turma_aluno = input("TURMA: ")
idade_aluno = int(input("IDADE: "))
CPF_aluno = input("CPF: ")

comando_inserir = (f'''
                    INSERT into alunos (nome, telefone, turma, idade,cpf)
                    VALUES('{nome_aluno}','{telefone_aluno}','{turma_aluno}',{idade_aluno},'{CPF_aluno}')''')
                        
cursor.execute(comando_inserir)
conexao.commit()
conexao.close 
