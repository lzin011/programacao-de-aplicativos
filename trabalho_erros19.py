import sqlite3 

def buscar_dados_dinamicos(nomes_tabela, id_registros):
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    #o sqlite joga um erro de sintaxe operacional indicando que não aceita o caractere '?'
    #não podemos parametrizar nomes de tabela? como resolver mantendo a segurança?
    #nome de colunas ou tabelas nao pode ser parametrizados. Eu teria que usar um outro codigo

    cursor.execute("SELECT * FROM ? WHERE id = ?", (nomes_tabela, id_registro ))

    print(cursor.fetchone())
    conexao.close()