def eh_par(numero):
    return numero % 2 == 0

assert eh_par(4) is True          
assert eh_par(5) is False        
assert eh_par(0) is True          
assert eh_par(-4) is True       
assert eh_par(-5) is False

#----------------------------------------

def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    elif media >= 4:
        return "Recuperação"
    return "Reprovado"


assert situacao_aluno(8) == "Aprovado"       
assert situacao_aluno(6) == "Aprovado"       
assert situacao_aluno(4) == "Recuperação"    
assert situacao_aluno(3) == "Reprovado"      
assert situacao_aluno(5.9) == "Recuperação" 

#----------------------------------------

def calcular_desconto(preco, percentual):

    preco = float(preco)
    percentual = float(percentual)

    return round(preco - (preco * percentual / 100), 2)

assert calcular_desconto(100, 0.0) == 100      
assert calcular_desconto(100, 10.0) == 90     
assert calcular_desconto(100, 50.0) == 50       
assert calcular_desconto(100, 100.0) == 0       
assert calcular_desconto(99.90, 10.0) == 89.91

def teste_pode_entrar():
    if pode_entrar(20, False) == True:
        print("Teste 1 passou")

    if pode_entrar(17, True) == True:
        print("Teste 2 passou")

    if pode_entrar(17, False) == False:
        print("Teste 3 passou")

    if pode_entrar(18, False) == True:
        print("Teste 4 passou")

    if pode_entrar(17, True) == True:
        print("Teste 5 passou")

#---------------------------------------------

def teste_calcular_frete():
    if calcular_frete(50) == 20:
        print("Teste 1 passou")

    if calcular_frete(100) == 10:
        print("Teste 2 passou")

    if calcular_frete(150) == 10:
        print("Teste 3 passou")

    if calcular_frete(200) == 0:
        print("Teste 4 passou")

    if calcular_frete(250) == 0:
        print("Teste 5 passou")



















