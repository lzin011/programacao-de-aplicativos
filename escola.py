import sqlite3
from banco import conectar


def cadastrar():
    nome = input("Nome da escola: ")
    cidade = input("Cidade: ")

    try:
        assert nome != "", "O nome não pode ficar vazio."
        assert cidade != "", "A cidade não pode ficar vazia."

        banco = conectar()
        banco.execute(
            "INSERT INTO escolas (nome, cidade) VALUES (?, ?)",
            (nome, cidade)
        )
        banco.commit()
        banco.close()

        print("Escola cadastrada!")

    except AssertionError as erro:
        print(erro)

    except sqlite3.Error as erro:
        print("Erro no banco:", erro)


def listar():
    try:
        banco = conectar()
        escolas = banco.execute("SELECT * FROM escolas").fetchall()

        print("\n--- ESCOLAS ---")

        for escola in escolas:
            print(escola)

        banco.close()

    except sqlite3.Error as erro:
        print("Erro:", erro)


def alterar():
    try:
        id_escola = int(input("ID da escola: "))
        nome = input("Novo nome: ")
        cidade = input("Nova cidade: ")

        assert nome != "", "O nome não pode ficar vazio."
        assert cidade != "", "A cidade não pode ficar vazia."

        banco = conectar()
        banco.execute(
            "UPDATE escolas SET nome = ?, cidade = ? WHERE id = ?",
            (nome, cidade, id_escola)
        )
        banco.commit()
        banco.close()

        print("Escola alterada!")

    except ValueError:
        print("O ID deve ser um número.")

    except AssertionError as erro:
        print(erro)

    except sqlite3.Error as erro:
        print("Erro:", erro)


def excluir():
    try:
        id_escola = int(input("ID da escola: "))

        banco = conectar()
        banco.execute(
            "DELETE FROM escolas WHERE id = ?",
            (id_escola,)
        )
        banco.commit()
        banco.close()

        print("Escola excluída!")

    except ValueError:
        print("O ID deve ser um número.")

    except sqlite3.Error as erro:
        print("Não foi possível excluir. Existem turmas vinculadas?")
        print(erro)