def eh_par(numero):
    
    return numero % 2 == 0


def calcular_desconto(preco, percentual):
    
   return preco - (preco * percentual / 100)


def pode_votar(idade):
   
    if idade < 16:
        return "Não pode votar"
    elif idade < 18 or idade >= 70:
        return "Voto facultativo"
    else:
        return "Voto obrigatório"

    assert pode_votar(15) == "Não pode votar"
    assert pode_votar(30) == "Voto obrigatório"
    assert pode_votar(70) == "Voto facultativo"

    assert calcular_desconto(100, 10) == 90
    assert calcular_desconto(250, 0) == 250
    assert calcular_desconto(80, 100) == 0

    assert eh_par(2) is True
    assert eh_par(7) is False
    assert eh_par(0) is True


print("Todos os testes foram executados com sucesso!")