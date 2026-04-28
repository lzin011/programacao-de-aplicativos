def aplicar_promocao(precos):
    nova_lista = []
    for preco in precos:
        if preco > 100:
            preco *= 0.85  # 15% de desconto
        nova_lista.append(preco)
    return nova_lista

compras = [150.0, 80.0, 200.0, 50.0]
print("Lista com desconto:", aplicar_promocao(compras))
