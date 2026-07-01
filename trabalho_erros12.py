import sqlite3 

# o aluno criou a conexao fora das funçoes para "facilitar".
# por que isso quebra o sistema quando o sistema quando usamos multiplos arquivos (módulos)?
# esta tudo fora das DEF.

conexao = sqlite3.connect('sistema_escola.db')
cursor = conexao.cursor()

def inserir_escola(nome):
    cursor.execute("INSERT INTO escolas (nome) VALUES (?)", (nome,))
    conexao.commit()