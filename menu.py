import sqlite3

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
            criar()

        elif opcao == "2":
            alterar()

        elif opcao == "3":
            listar()

        elif opcao == "4":
            excluir()

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