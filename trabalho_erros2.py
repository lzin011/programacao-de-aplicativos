import sqlite3

def cadastrar_serie(nome_serie, id_escola):
    conexao = sqlite3.connect ('sistemna_escola.db')
    cursor = conexao.cursor()
    cursor.execute("PRAGMA foreing_keys = ON")
    #o alunos tenta cadastrar uma serie com id_escola = 999 (que não existe).
    #o sqlite aceita o cadastro mesmo assim. o que esta faltando ativar?
    # tivemos que usar o PRAGMA, feito para alterar algumas configurações da conexão.
    try:
        cursor.execute("INSERT INTO series (nome_serie, id_escola) VALUES (?, ?)",(nome_serie, id_escola))
        conexao.commit()
    except sqlite3.integrityError:
        print("Erro: Escola inexistente!")
    finally:
        print("codigo encerrado")
        conexao.close()