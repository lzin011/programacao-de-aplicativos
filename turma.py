import sqlite3
from banco import conectar


def cadastrar():
    nome = input("Nome da turma: ")

    try:
        id_escola = int(input("ID da escola: "))

        assert nome != "", "O nome da turma não pode ficar vazio."
        assert id_escola > 0, "O ID da escola deve ser maior que zero."

        banco = conectar()
        banco.execute(
            "INSERT INTO turmas (nome_turma, id_escola) VALUES (?, ?)",
            (nome, id_escola)
        )
        banco.commit()
        banco.close()

        print("Turma cadastrada!")

    except ValueError:
        print("O ID deve ser um número.")

    except AssertionError as erro:
        print(erro)

    except sqlite3.Error as erro:
        print("A escola informada não existe.")
        print(erro)


def listar():
    try:
        banco = conectar()
        turmas = banco.execute("SELECT * FROM turmas").fetchall()

        print("\n--- TURMAS ---")

        for turma in turmas:
            print(turma)

        banco.close()

    except sqlite3.Error as erro:
        print("Erro:", erro)


def alterar():
    try:
        id_turma = int(input("ID da turma: "))
        nome = input("Novo nome: ")
        id_escola = int(input("Novo ID da escola: "))

        assert nome != "", "O nome não pode ficar vazio."
        assert id_escola > 0, "O ID da escola deve ser maior que zero."

        banco = conectar()
        banco.execute(
            """
            UPDATE turmas
            SET nome_turma = ?, id_escola = ?
            WHERE id = ?
            """,
            (nome, id_escola, id_turma)
        )
        banco.commit()
        banco.close()

        print("Turma alterada!")

    except ValueError:
        print("Os IDs devem ser números.")

    except AssertionError as erro:
        print(erro)

    except sqlite3.Error as erro:
        print("A escola informada não existe.")
        print(erro)


def excluir():
    try:
        id_turma = int(input("ID da turma: "))

        banco = conectar()
        banco.execute(
            "DELETE FROM turmas WHERE id = ?",
            (id_turma,)
        )
        banco.commit()
        banco.close()

        print("Turma excluída!")

    except ValueError:
        print("O ID deve ser um número.")

    except sqlite3.Error as erro:
        print("Não foi possível excluir. Existem alunos vinculados?")
        print(erro)

aluno.py
import sqlite3
from banco import conectar


def cadastrar():
    nome = input("Nome do aluno: ")

    try:
        idade = int(input("Idade: "))
        id_turma = int(input("ID da turma: "))

        assert nome != "", "O nome não pode ficar vazio."
        assert idade >= 3, "O aluno deve ter 3 anos ou mais."

        banco = conectar()
        banco.execute(
            """
            INSERT INTO alunos (nome, idade, id_turma)
            VALUES (?, ?, ?)
            """,
            (nome, idade, id_turma)
        )
        banco.commit()
        banco.close()

        print("Aluno cadastrado!")

    except ValueError:
        print("Idade e ID da turma devem ser números.")

    except AssertionError as erro:
        print(erro)

    except sqlite3.Error as erro:
        print("A turma informada não existe.")
        print(erro)


def listar():
    try:
        banco = conectar()
        alunos = banco.execute("SELECT * FROM alunos").fetchall()

        print("\n--- ALUNOS ---")

        for aluno in alunos:
            print(aluno)

        banco.close()

    except sqlite3.Error as erro:
        print("Erro:", erro)


def alterar():
    try:
        id_aluno = int(input("ID do aluno: "))
        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))
        id_turma = int(input("Novo ID da turma: "))

        assert nome != "", "O nome não pode ficar vazio."
        assert idade >= 3, "O aluno deve ter 3 anos ou mais."

        banco = conectar()
        banco.execute(
            """
            UPDATE alunos
            SET nome = ?, idade = ?, id_turma = ?
            WHERE id = ?
            """,
            (nome, idade, id_turma, id_aluno)
        )
        banco.commit()
        banco.close()

        print("Aluno alterado!")

    except ValueError:
        print("ID e idade devem ser números.")

    except AssertionError as erro:
        print(erro)

    except sqlite3.Error as erro:
        print("A turma informada não existe.")
        print(erro)


def excluir():
    try:
        id_aluno = int(input("ID do aluno: "))

        banco = conectar()
        banco.execute(
            "DELETE FROM alunos WHERE id = ?",
            (id_aluno,)
        )
        banco.commit()
        banco.close()

        print("Aluno excluído!")

    except ValueError:
        print("O ID deve ser um número.")

    except sqlite3.Error as erro:
        print("Erro:", erro)