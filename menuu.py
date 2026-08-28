import banco
import escola
import turma
import aluno


banco.criar_tabelas()


while True:

    print("\n===== GESTÃO ESCOLAR =====")
    print("1 - Cadastrar escola")
    print("2 - Listar escolas")
    print("3 - Alterar escola")
    print("4 - Excluir escola")

    print("5 - Cadastrar turma")
    print("6 - Listar turmas")
    print("7 - Alterar turma")
    print("8 - Excluir turma")

    print("9 - Cadastrar aluno")
    print("10 - Listar alunos")
    print("11 - Alterar aluno")
    print("12 - Excluir aluno")

    print("0 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        escola.cadastrar()

    elif opcao == "2":
        escola.listar()

    elif opcao == "3":
        escola.alterar()

    elif opcao == "4":
        escola.excluir()

    elif opcao == "5":
        turma.cadastrar()

    elif opcao == "6":
        turma.listar()

    elif opcao == "7":
        turma.alterar()

    elif opcao == "8":
        turma.excluir()

    elif opcao == "9":
        aluno.cadastrar()

    elif opcao == "10":
        aluno.listar()

    elif opcao == "11":
        aluno.alterar()

    elif opcao == "12":
        aluno.excluir()

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")