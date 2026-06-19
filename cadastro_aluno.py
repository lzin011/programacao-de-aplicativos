import sqlite3 # Importa a biblioteca

conexao = sqlite3.connect ('escola.db') # Cria uma conexão com o banco de dados chamado escola.db.
cursor = conexao.cursor() # O cursor é responsável por executar comandos SQL no banco de dados.
cursor.execute ('''CREATE TABLE IF NOT EXISTS alunos ( 
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    telefone TEXT,             
                    turma TEXT,
                    idade INTEGER,
                    cidade TEXT,
                    endereco TEXT,
                    estado TEXT,
                    cpf TEXT UNIQUE NOT NULL 
                    )''') # cria atabela # CPF é unico e é obrigatorio, nao pode ficar vazio. E o nome também 

# recebendo os dados do usuario 
nome_aluno = input("NOME: ") # pede o nome do aluno 
telefone_aluno = input("TELEFONE: ") # pede o telefone 
turma_aluno = input("TURMA: ") # pede a turma do aluno 
idade_aluno = int(input("IDADE: ")) #pede a idade do aluno 
CPF_aluno = input("CPF: ") # pede o cpf do aluno 
cidade_aluno = input("CIDADE: ") # pede a cidade 
endereco_aluno = input("ENDERECO: ") # pede o endereço
estado_aluno = input("ESTADO: ") # pede o estado 

comando_inserir = (f''' 
                    INSERT into alunos (nome, telefone, turma, idade,cpf)
                    VALUES('{nome_aluno}','{telefone_aluno}','{turma_aluno}',{idade_aluno},'{CPF_aluno}','{cidade_aluno}','{endereco_aluno}','{estado_aluno}')''') # monta o comando 
                        
cursor.execute(comando_inserir) # executa o comando 
conexao.commit() # grava definitivamente os dados no banco 
conexao.close () # fecha a conexão 

def listar():

    cursor.execute("SELECT * FROM alunos") 
    professores = cursor.fetchall()

    for aluno in alunos: 
        print(f"ID: {aluno[0]}")
        print(f"Nome: {aluno[1]}")
        print(f"Telefone: {aluno[2]}")
        print(f"Turma: {aluno[3]}")
        print(f"Idade: {aluno[4]}")
        print(f"CPF: {aluno[5]}")
        print(f"salario: {aluno[6]}")
        print(f"escola: {aluno[7]}")
        print(f"cidade: {aluno[8]}")
        print(f"endereco: {aluno[9]}")
        print(f"estado: {aluno[10]}")
        print("-" * 30)



def alterar():
    id_aluno = int(input("Qual é o teu ID: "))

    cursor.execute(f'''SELECT * FROM alunos WHERE id = {id_aluno}''')
    alunos = cursor.fetchone()

    if not id_aluno:
        print("Não encontrado!")
    else:
        novo_nome = input("qual o novo nome: ")
        novo_telefone = input("qual o novo telefone: ")
        novo_materia = input("qual a nova materia: ")
        novo_idade = int(input("qual a nova idade: "))
        novo_cpf = input("qual o novo cpf: ")
        novo_salario = float(input("qual o novo salario: "))
        novo_nome_de_escola = input("qual o novo nome: ")
        novo_cidade = input("qual a nova cidade: ")
        novo_endereco = input("qual o novo endereço: ")
        novo_estado = input("qual o novo estado: ")

        comando = f'''UPDATE professores SET nome = '{novo_nome}',telefone = '{novo_telefone}',materia = '{novo_materia}',idade = {novo_idade},cpf = '{novo_cpf}',salario = '{novo_salario}',escola = '{novo_escola}','''
        
        conexao.commit()
        print(" Dados alterados ")


def deletar():

    conexao = sqlite3.connect("escola_demonstracao.db")
    cursor = conexao.cursor()

    listar()

    id_professor = int(input(" Qual ID deseja deletar: " ))

    cursor.execute(f'''DELETE FROM professor WHERE Id = {id_professor}''')

    conexao.commit()
    print("professor deletado")

    conexao.close()



def menu():
      
    while True:
        print("\n--- TABELA PROFESSORES ---")
        print("\n=== SISTEMA ESCOLAR ===")  
        print("1. Cadastrar professor") 
        print("2. Listar professor") 
        print("3. Atualizar professor") 
        print("4. Excluir professor") 
        print("5. Sair")
            
        opcao = input("Escolha uma opção: ")

        if opcao == '1': criar()
        elif opcao == '2': listar() 
        elif opcao == '3': alterar() 
        elif opcao == '4': deletar() 
        elif opcao == '5': break
        else: print("Opção inválida!")

menu()


    

  

     
     
