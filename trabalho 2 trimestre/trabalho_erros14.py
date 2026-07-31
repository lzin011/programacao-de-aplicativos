import sqlite3

def cadastrar_serie_seguro(nome, id_escola):
    conexao = None
    try:
        # se a linha abaixo falhar por falta d epermissao na pasta,
        # o bloco finally vai tentar fechar algo que nao abriu. como corrigir?
        # criar conexao = None antes do try e verificar se ela existe antes de chamar close().
        conexao = sqlite3.connect('/pasta_protegida/sistema.db')
        cursor = conexao.cursor()
        cursor.execute ("INSERT INTO series (nome_serie, id_escola) VALUES (?,?)",(nome, id_escola))
        conexao.commit()
    except sqlite3.Error as e:
        print("Error tecnico:", e)
    finally:
        if conexao:
            conexao.close()