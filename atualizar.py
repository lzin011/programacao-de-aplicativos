def atualizar_produto(indice, novo_nome):
    """
    Atualiza o nome de um produto existente.

    Parâmetros:
    indice (int): Posição do produto na lista.
    novo_nome (str): Novo nome a ser atribuído.
    """
    if 0 <= indice < len(estoque):
        produto_antigo = estoque[indice]
        estoque[indice] = novo_nome
        print(f"Produto '{produto_antigo}' atualizado para '{novo_nome}'.")
    else:
        print("Erro: índice inválido.")
