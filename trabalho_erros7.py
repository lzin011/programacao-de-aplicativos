import sqlite3

def cadastrar_turma (nome, id_serie, id_prof):
    try:
        conexao = sqlite3.connect('sistema_escola.db')
        cursor = conexao.cursor()
        cursor.execute("PRAGMA foreign_keys = ON;")
        # se o id_prof não existir, ocorre em IntegrityError.
        # se o erro acontecer, o que ocorre com a linha conexao.close()?
        # Se não houver erro, conexao.close() é executada normalmente.
        # Se houver erro antes dela e você não tratar a exceção, conexao.close() não é executada.
        # por isso que é bom fazer um bloco conexao.close dentro do finally porque garante o fechamento de seu codigo mesmo dando erro.
        cursor.execute("INSERT INTO turma (nome_turma, id_serie, id_professor) VALUES (?,?,?)",(nome, id_serie, id_prof))
         conexao.commit()
    except sqlite3.IntegrityError as e:
        print("Erro:", e)

    finally:
        conexao.close()
        
        