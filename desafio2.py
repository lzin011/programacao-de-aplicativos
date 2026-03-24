autorizados = ["alice", "bob", "carlos"]
nome = input("digite o nome de um pesquisador: ")

# verificação de existencia 
if nome in autorizados:
    indice = autorizados.index(nome)
    print(f"acesso permitido! o pesquisador {nome} esta na posição {indice}")

    pergunta = input("deseja remover esse pesquiador da lista (s/n)? ")

    if pergunta == "s":
        autorizados.remove(nome)
        print(f"lista atualizada {autorizados}")

    else:
        print("encerrando programa!")

else:
    adicionar = input("deseja cadastrar esse novo pesquisador (s/n)? ")
    if adicionar == "s":
        autorizados.append(nome)
        print(f"lista atualizada {autorizados}")

