import sqlite3

try:
    conexao = sqlite3.connect("sistema_escola.db")
    cursor = conexao.cursor()

    cursor.execute(
        "INSERT INTO professores (nome, materia, cpf) VALUES (?, ?, ?)",
        (nome, materia, cpf)
    )

    conexao.commit()

except sqlite3.IntegrityError:
    print("Erro: este CPF já está cadastrado no sistema!")

except sqlite3.Error as erro:
    print("Erro no banco de dados:", erro)

finally:
    conexao.close()

    # existe um erro de digitaçao no comando sql (inserto) 
    # por que o programa mostra "CPF ja cadastrando" em vez de avisar sobre o erro de sintexe?
    # Se houver um erro de sintaxe no SQL (por exemplo, escrever INSERTO em vez de INSERT), será exibida a mensagem com o erro real, como "Erro no banco de dados: near 'INSERTO': syntax error".
    #Dessa forma, você consegue identificar corretamente a causa do problema em vez de mostrar sempre a mesma mensagem.