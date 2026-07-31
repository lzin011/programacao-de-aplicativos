def menu():
    while True:
        print("1. cadastrar aluno")
        print("2. sair")
        opcao = input("escolha: ")
         
        if opcao == "1":
            print("cadastrando...")
        elif opcao == "2":
            print("saindo do programa.")
            break
            # por que o programa continua rodando e mostrando o menu mesmo digitando 2?
            # O pass não faz nada. Ele apenas serve como um espaço reservado. O while continua executando e o menu aparece novamente.
            