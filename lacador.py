def esta_na_lista(lista, nome):
    for item in lista:
        if item == nome:
            return "Encontrado!"
    return "Não disponível"

frutas = ["maçã", "banana", "laranja", "uva"]
busca = input("Digite uma fruta para buscar: ")
print(esta_na_lista(frutas, busca))
