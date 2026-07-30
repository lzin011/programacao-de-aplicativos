import sqlite3

def buscar_dados_dinamicos(nome_tabela, id_registro):
    tabelas_permitidas = {
        "alunos",
        "professores",
        "cursos"
    }

    if nome_tabela not in tabelas_permitidas:
        raise ValueError("Tabela inválida.")

    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    sql = f"SELECT * FROM {nome_tabela} WHERE id = ?"
    cursor.execute(sql, (id_registro,))

    print(cursor.fetchone())

    conexao.close()

    # o sqlite joga um erro de sistema operacional indicando que nao aceita o carectere "?"
    # nao podemos parametrizar nomes de tabela? como resolver mantendo a segurança? 
      # o caractere "?" nao pode ser usado para nomes de tabela ou coluna, ele serve so para valores.