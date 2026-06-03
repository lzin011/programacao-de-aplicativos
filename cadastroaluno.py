import json
import os

sistema_matrícula = 'sistema.json'

def cadastrar_aluno():
    print("\n--- Novo Cadastro ---")

    if os.path.exists(sistema_matrícula):
        with open(sistema_matrícula, "r", encoding='utf'-8) as n:
            sistema = json.load(n)

    else:
        sistemas = []

        novo_cadastro = {
        "id" : int(input("Id: ")),
        "nome_completo" : input("Nome_completo: "),
        "cpf" : input("CPF: "),
        "idade" : int(input("Idade: ")),
        "telefone" : input("Telefone: "),
        "turma" : input("Turma: ")
        }
    
    alunos.append(cadastro_novo)
    with open(sistema_matrícula, "w", encoding='utf'-8) as n:
        print("Aluno cadastrado com sucesso!")

def listar_aluno():
    print("\n--- Lista de Alunos ---")

    if os.path.exists(sistema_matrícula):
        with open(sistema_matrícula, "r", encoding='utf'-8) as n:
            sistema = json.load(n)

    else:
        sistemas = []

    if not sistemas:
        print("Erro: Este ID já está em uso!")
        return

    for sistema in sistemas:
        print(f"Nome: {aluno['nome']} | CPF: {aluno['cpf']} | Turma: {aluno['turma']} | Tel: {aluno['telefone']}")


# def atualizar_aluno():
#     print("\n--- Atualizar Aluno ---")

#     if not os.path.exists(sistema_matrícula):
#         print("Nenhum aluno cadastrado no sistema.")
#         return
    
#         with open(sistema_matrícula, "r", encoding='utf'-8) as n:
#             sistema = json.load(n)

#         id_busca = int(input("Digite o ID do aluno que deseja mudar?: "))

#         for sistema in sistemas: 

            
listar_aluno()


def atualizar_aluno(alunos):
    id_aluno = int(input("Digite o ID do aluno: "))

    for aluno in alunos:
        if aluno["id"] == id_aluno:
            print("Aluno encontrado!")

            aluno["nome"] = input(f"Novo nome ({aluno['nome']}): ")
            aluno["telefone"] = input(f"Novo telefone ({aluno['telefone']}): ")

            salvar_json(alunos)

            print("Dados atualizados com sucesso!")
            return

    print("Aluno não encontrado.")