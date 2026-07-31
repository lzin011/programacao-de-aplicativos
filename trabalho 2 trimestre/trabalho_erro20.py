import sqlite3

def cadastrar_escola_manual():
    id_escola = int(input("Digite o ID para a nova escola: "))
    nome = input("Nome da escola: ")

    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    try:
        cursor.execute(
            "INSERT INTO escola (id, nome) VALUES (?, ?)",
            (id_escola, nome)
        )
        conexao.commit()
        print("Escola cadastrada com sucesso!")

    except sqlite3.IntegrityError:
        print("Erro: já existe uma escola com esse ID.")

    finally:
        conexao.close()

        #se rodar duas vezes com o id 1, o programa fecha abruptamente (crash) #aplique a blindagem protetora necessaria: 
        # A forma recomendada é usar try/except e garantir o fechamento da conexão com finally:
