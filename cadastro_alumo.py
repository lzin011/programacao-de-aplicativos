import sqlite3
conexão = sqlite3.connect ('escola.db')
sursor = conexão.cursor()
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
                    INSERT into alunos (nome, telefone, idade,cpf)
                    VALUES('{nome_aluno}','{telefone_aluno}','{turma_aluno}',{idade_aluno},'{CPF_aluno}')''')
                        
cursor.execute(comando_inserir)
conexão.commit()
conexão.close 
