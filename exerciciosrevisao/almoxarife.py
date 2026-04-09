lista = []
rodando = True

while rodando:
    opcao = input("Digite (a)dicionar, (l)istar ou (s)air: ")

    if opcao == "a":
        item = input("Item: ")
        lista.append(item)

    elif opcao == "l":
        print(lista)

    elif opcao == "s":
        rodando = False