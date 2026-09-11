numeros = list(range(1, 101))

def busca_sequencial(lista, alvo):
    comparacoes = 0

    for numero in lista:
        comparacoes += 1
        if numero == alvo:
            print("Sequencial:", comparacoes, "comparações")
            return

def busca_binaria(lista, alvo):
    inicio = 0
    fim = len(lista) - 1
    comparacoes = 0

    while inicio <= fim:
        meio = (inicio + fim) // 2
        comparacoes += 1

        if lista[meio] == alvo:
            print("Binária:", comparacoes, "comparações")
            return
        elif lista[meio] < alvo:
            inicio = meio + 1
        else:
            fim = meio - 1

busca_sequencial(numeros, 95)
busca_binaria(numeros, 95)