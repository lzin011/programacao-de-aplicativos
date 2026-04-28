def somar_carrinho(precos):
    total = sum(precos)
    if total > 500:
        total *= 0.9  # 10% de desconto
    return total

lista_compras = [200, 150, 180]
print("Total a pagar:", somar_carrinho(lista_compras))
