import sqlite3
from banco import conectar

def cadastrar():
    try:
        nome = input("Nome do aluno: ")
        idade = int(input("Idade: "))
        id_turma = int(input("ID da turma: "))

        assert nome != "", "Nome não pode ficar vazio"
        assert idade >= 3, "Idade deve ser 3 ou mais"

        banco = conectar()
        banco.execute(
            "INSERT INTO alunos(nome,idade,id_turma) VALUES(?,?,?)",
            (nome, idade, id_turma)
        )
        banco.commit()
        banco.close()

        print("Aluno cadastrado!")

    except ValueError:
        print("Digite números válidos.")
    except AssertionError as e:
        print(e)
    except sqlite3.Error:
        print("Turma não encontrada.")


def listar():
    banco = conectar()

    for aluno in banco.execute("SELECT * FROM alunos"):
        print(aluno)

    banco.close()


def alterar():
    try:
        id = int(input("ID: "))
        nome = input("Novo nome: ")
        idade = int(input("Nova idade: "))
        id_turma = int(input("ID da turma: "))

        assert nome != "", "Nome não pode ficar vazio"
        assert idade >= 3, "Idade deve ser 3 ou mais"

        banco = conectar()
        banco.execute(
            """UPDATE alunos
            SET nome=?, idade=?, id_turma=?
            WHERE id=?""",
            (nome, idade, id_turma, id)
        )
        banco.commit()
        banco.close()

        print("Alterado!")

    except ValueError:
        print("Digite números válidos.")
    except AssertionError as e:
        print(e)
    except sqlite3.Error:
        print("Turma não encontrada.")


def excluir():
    try:
        id = int(input("ID: "))

        banco = conectar()
        banco.execute("DELETE FROM alunos WHERE id=?", (id,))
        banco.commit()
        banco.close()

        print("Excluído!")

    except ValueError:
        print("Digite um ID válido.")