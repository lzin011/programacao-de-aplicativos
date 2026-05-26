import json
import os

ARQUIVO = "alunos.json"


def carregar_alunos():
    if not os.path.exists(ARQUIVO):
        return

    with open(ARQUIVO, "r", encoding="utf-8") as arquivo:
        return json.load(arquivo)


def salvar_alunos(alunos):
    with open(ARQUIVO, "w", encoding="utf-8") as arquivo:
        json.dump(alunos, arquivo, indent=4, ensure_ascii=False)


def criar_aluno():
    alunos = carregar_alunos()

    novo_aluno = {
        "id": gerar_id(alunos),
        "nome_completo": input("Nome completo: "),
        "telefone": input("Telefone: "),
        "turma": input("Turma: "),
        "idade": int(input("Idade: ")),
        "cpf": input("CPF: ")
    }

    alunos.append(novo_aluno)
    salvar_alunos(alunos)

    print("\nAluno cadastrado com sucesso!")


def listar_alunos():
    alunos = carregar_alunos()

    if len(alunos) == 0:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in alunos:
        print("\nID:", aluno["id"])
        print("Nome:", aluno["nome_completo"])
        print("Telefone:", aluno["telefone"])
        print("Turma:", aluno["turma"])
        print("Idade:", aluno["idade"])
        print("CPF:", aluno["cpf"])



def atualizar_aluno():
    alunos = carregar_alunos()

    id_aluno = int(input("Digite o ID: "))

    for aluno in alunos:

        if aluno["id"] == id_aluno:

            aluno["nome_completo"] = input("Novo nome: ")
            aluno["telefone"] = input("Novo telefone: ")
            aluno["turma"] = input("Nova turma: ")
            aluno["idade"] = int(input("Nova idade: "))
            aluno["cpf"] = input("Novo CPF: ")

            salvar_alunos(alunos)

            print("Aluno atualizado!")
            return

    print("Aluno não encontrado.")



def deletar_aluno():
    alunos = carregar_alunos()

    id_aluno = int(input("Digite o ID: "))

    for aluno in alunos:

        if aluno["id"] == id_aluno:

            alunos.remove(aluno)

            salvar_alunos(alunos)

            print("Aluno removido!")
            return

    print("Aluno não encontrado.")



