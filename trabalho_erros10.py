import sqlite3 

def deletar_escola_antiga():
    id_escola = int(input("ID da escola remover"))
    conexao = sqlite3.connect('sistema_escola.db')
    cursor = conexao.cursor()

    # esse comando vai apagar o banco inteiro se o aluno não prestar atenção.
    # O código original está errado porque id_escola é interpretado como nome de uma coluna. A forma correta usa ? para excluir apenas a escola com o ID informado pelo usuário.
    
    cursor.execute(
        "DELETE FROM escola WHERE id = ?",
        (id_escola,)
    )


    conexao.commit()
    conexao.close()
    
    print("escola removida com sucesso")