import sqlite3

def criar_cliente():
    print("Função criar cliente")

def alterar_cliente():
    print("Função alterar cliente")

def listar_cliente():
    print("Função listar clientes")

def excluir_cliente():
    print("Função excluir cliente")

def criar_produto():
    print("Função criar produto")

def alterar_produto():
    print("Função alterar produto")

def listar_produto():
    print("Função listar produtos")

def excluir_produto():
    print("Função excluir produto")


def Menu():
    while True:
        print("\n===== MENU =====")
        print("1 - Criar cliente")
        print("2 - Alterar cliente")
        print("3 - Listar clientes")
        print("4 - Excluir cliente")
        print("5 - Criar produto")
        print("6 - Alterar produto")
        print("7 - Listar produtos")
        print("8 - Excluir produto")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            criar_cliente()

        elif opcao == "2":
            alterar_cliente()

        elif opcao == "3":
            listar_cliente()

        elif opcao == "4":
            excluir_cliente()

        elif opcao == "5":
            criar_produto()

        elif opcao == "6":
            alterar_produto()

        elif opcao == "7":
            listar_produto()

        elif opcao == "8":
            excluir_produto()

        elif opcao == "0":
            print("Programa encerrado!")
            break

        else:
            print("Opção inválida!")


Menu()