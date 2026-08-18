import sqlite3 

def conectar_banco():
    try:
        conexao = sqlite3.connect("lavanderia.db")
        conexao.execute("PRAGMA foreign_keys = ON") 
        return conexao
    except Exception as erro:
        print("Erro:", erro)

def criar_tabelas():
    try:
        conexao = conectar_banco()
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS franquias_lavanderia (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_comercial TEXT,
                site TEXT
            )
        """)
        conexao.execute("""                                            
            CREATE TABLE IF NOT EXISTS unidades_operacionais (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                bairro_central TEXT,
                id_franquia INTEGER,
                FOREIGN KEY (id_franquia) REFERENCES franquias_lavanderia(id)
            )
        """)                     
        conexao.commit()
        conexao.close()
    except Exception as erro:
        print("Erro:", erro)


def cadastrar_franquia():
    try:
        conexao = conectar_banco()
        nome_comercial = input("Nome comercial: ")
        site = input("Site: ")
        conexao.execute(
            "INSERT INTO franquias_lavanderia (nome_comercial, site) VALUES (?, ?)",
            (nome_comercial, site)
        )
        conexao.commit()
        conexao.close()
        print("Franquia cadastrada!")
    except Exception as erro:
        print("Erro:", erro)


def cadastrar_unidade():
    try:
        conexao = conectar_banco()
        bairro_central = input("Bairro central: ")
        id_franquia = int(input("ID da franquia: "))

        franquia = conexao.execute(
            "SELECT id FROM franquias_lavanderia WHERE id = ?",
            (id_franquia,)
        ).fetchone()
                           
        if franquia is None:
            print("Franquia não existe!")
            conexao.close()
            return

        conexao.execute(
            "INSERT INTO unidades_operacionais (bairro_central, id_franquia) VALUES (?, ?)",     
            (bairro_central, id_franquia)
        )
        conexao.commit()
        conexao.close()
        print("Unidade cadastrada!")
    except Exception as erro:
        print("Erro:", erro)


def listar_unidades():
    try:
        conexao = conectar_banco()
        unidades = conexao.execute(
            "SELECT * FROM unidades_operacionais"
        ).fetchall()                              
        for unidade in unidades:
            print(unidade)

        conexao.close()
    except Exception as erro:
        print("Erro:", erro)


def atualizar_unidade():
    try:
        conexao = conectar_banco()
        id_unidade = int(input("ID da unidade: "))
        bairro_central = input("Novo bairro: ")
        id_franquia = int(input("Novo ID da franquia: "))

        franquia = conexao.execute(
            "SELECT id FROM franquias_lavanderia WHERE id = ?",  
                                                
            (id_franquia,)
        ).fetchone()

        if franquia is None:
            print("Franquia não existe!")
            conexao.close()
            return

        conexao.execute(
            "UPDATE unidades_operacionais SET bairro_central = ?, id_franquia = ? WHERE id = ?",
            (bairro_central, id_franquia, id_unidade)
        )
        conexao.commit()
        conexao.close()
        print("Unidade atualizada!")
    except Exception as erro:
        print("Erro:", erro)


def excluir_unidade():
    try:
        conexao = conectar_banco()
        id_unidade = int(input("ID da unidade: "))

        conexao.execute(
            "DELETE FROM unidades_operacionais WHERE id = ?", 
                                          
            (id_unidade,)
        )
        conexao.commit()
        conexao.close()
        print("Unidade excluída!")
    except Exception as erro:
        print("Erro:", erro)


def menu():
    try:
        criar_tabelas()

        while True:
            print("\n===== LAVANDERIA INDUSTRIAL =====") 
            print("1 - Cadastrar franquia")
            print("2 - Listar franquias")
            print("3 - Atualizar franquia")
            print("4 - Excluir franquia")
            print("5 - Cadastrar unidade")
            print("6 - Listar unidades")
            print("7 - Atualizar unidade")
            print("8 - Excluir unidade")
            print("0 - Sair")

            opcao = input("Escolha: ")

            if opcao == "1":
                cadastrar_franquia()
            elif opcao == "2":
                listar_franquias()
            elif opcao == "3":
                atualizar_franquia()
            elif opcao == "4":
                excluir_franquia()
            elif opcao == "5":
                cadastrar_unidade()
            elif opcao == "6":
                listar_unidades()
            elif opcao == "7":
                atualizar_unidade()
            elif opcao == "8":
                excluir_unidade()
            elif opcao == "0":
                break
            else:
                print("Opção inválida!")

    except Exception as erro:
        print("Erro:", erro)

menu()