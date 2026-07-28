import sqlite3 

def cadastrar_escola_manual():
    #o aluno resolveu gerar o id por conta propria 
    id_escola = int(input("digite o id para a nova escola: "))
    nome = input("nome da escola: ")
    
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #se rodar duas vezes com o id 1, o programa fecha abruptamente (crash)
    #aplique a blindagem protetora necessaria:
    # A forma recomendada é usar try/except e garantir o fechamento da conexão com finally:
    cursor.execute("INSERT INTO escola (id, nome) VALUES (?, ?)", (id_escola, nome))

    conexao.commit()
    conexao.close()