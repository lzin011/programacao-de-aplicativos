import sqlite3 # Importa a biblioteca

conexao = sqlite3.connect ('escola.db') # Cria uma conexão com o banco de dados chamado escola.db.
cursor = conexao.cursor() # O cursor é responsável por executar comandos SQL no banco de dados.
cursor.execute ('''CREATE TABLE IF NOT EXISTS alunos ( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,             
                    turma TEXT,
                    idade INTEGER,
                    cpf TEXT UNIQUE NOT NULL 
                    )''') # cria atabela # CPF é unico e é obrigatorio, nao pode ficar vazio. E o nome também 

# recebendo os dados do usuario 
nome_aluno = input("NOME: ") # pede o nome do aluno 
telefone_aluno = input("TELEFONE: ") # pede o telefone 
turma_aluno = input("TURMA: ") # pede a turma do aluno 
idade_aluno = int(input("IDADE: ")) #pede a idade do aluno 
CPF_aluno = input("CPF: ") # pede o cpf do aluno 

comando_inserir = (f''' 
                    INSERT into alunos (nome, telefone, turma, idade,cpf)
                    VALUES('{nome_aluno}','{telefone_aluno}','{turma_aluno}',{idade_aluno},'{CPF_aluno}')''') # monta o comando 
                        
cursor.execute(comando_inserir) # executa o comando 
conexao.commit() # grava definitivamente os dados no banco 
conexao.close () # fecha a conexão 
