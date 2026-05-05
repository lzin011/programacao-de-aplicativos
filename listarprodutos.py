def listar_produtos():
    """
    Exibe todos os produtos armazenados no estoque,
    juntamente com seus respectivos índices.
    """
    if len(estoque) == 0:
        print("O estoque encontra-se vazio.")
    else:
        print("\nProdutos cadastrados:")
        for indice, produto in enumerate(estoque):
            print(f"Índice {indice}: {produto}")