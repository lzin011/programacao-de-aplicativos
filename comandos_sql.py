import sqlite3
conexao = sqlite.connect('escola_demonstracao.db')
cursor = conexao.cursor()

def criar():


    cursor.execute ('''CREATE TABLE IF NOT EXISTS alunos ( 
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            telefone TEXT,             
                            idade INTEGER,
                            turma TEXT,
                            id_professor INTEGER
                            FOREING KEY (id_professor)reference professor(id))''')


        nome_professor = input("qual o nome do professor: ")
        telefone = input("qual o telefone do professor: ")
        idade = int(input("qual sua idade: ") )
        turma = input("digite a turma: ")
        
        comando_inserir = (f''' 
                        INSERT into professores (nome, telefone, materia, idade, cpf, salario, escola)
                        VALUES('{nome_professor}','{telefone}','{idade}','{turma}')''') 
                            
        cursor.execute(comando_inserir)

        conexao.commit()

        print("cadastro realizado!")


def listar()

                