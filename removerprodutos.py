def remover_produto(indice):
    """
    Remove um produto do estoque com base no índice.

    Parâmetro:
    indice (int): Posição do produto na lista.
    """
    if 0 <= indice < len(estoque):
        produto_removido = estoque.pop(indice)
        print(f"Produto '{produto_removido}' removido com sucesso.")
    else:
        print("Erro: índice inválido.")

