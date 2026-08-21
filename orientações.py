def dobrar(numero):
    return numero * 2

assert dobrar(3) == 6
assert dobrar(0) == 1
assert dobrar(-2) == -4
#----------------------------------------
def situacao_aluno(media):
    if media >= 6:
        return "Aprovado"
    return "Reprovado"

assert situacao_aluno(8) == "Aprovado"
assert situacao_aluno(6) == "Aprovado"
assert situacao_aluno(5.9) == "Reprovado"
assert situacao_aluno(0) == "Reprovado"
assert situacao_aluno(10) == "Aprovado"

assert situacao_aluno(5) == "Reprovado"
#----------------------------------------
def calcular_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 20) == 160
assert calcular_desconto(50, 10) == 45
#---------------------------------------
def eh_par(numero):
    return numero % 2 == 0

assert eh_par(3) is False
#---------------------------------------
def frete_gratis(valor):
    return valor >= 200

def pode_votar(idade):
    return idade >= 16

def senha_valida(senha):
    return len(senha) >= 8

assert frete_gratis(199.99) is False
assert frete_gratis(200) is True
assert frete_gratis(200.01) is True

assert pode_votar(15) is False
assert pode_votar(16) is True
assert pode_votar(17) is True

assert senha_valida("1234567") is False
assert senha_valida("12345678") is True
assert senha_valida("123456789") is True
#---------------------------------------
def situacao_faltas(faltas):
    if faltas <= 4:
        return "Regular"
    elif faltas <= 10:
        return "Atenção"
    else:
        return "Reprovado por falta"

assert situacao_faltas(0) == "Regular"
assert situacao_faltas(4) == "Regular"
assert situacao_faltas(5) == "Atenção"
assert situacao_faltas(10) == "Atenção"
assert situacao_faltas(11) == "Reprovado por falta"
#-----------------------------------------------------
def calcular_desconto_original(preco, percentual):
    return preco - percentual

def calcular_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto

assert calcular_desconto(100, 10) == 90
assert calcular_desconto(200, 25) == 150
assert calcular_desconto(50, 20) == 40
#-----------------------------------------------------
def pode_votar(idade):
    return idade >= 16

assert pode_votar(15) is False
assert pode_votar(16) is True
assert pode_votar(17) is True

assert pode_votar(10) is False
#----------------------------------------------------
def buscar_nome(lista, nome):
    return nome in lista

def tem_senha_valida(senha):
    return len(senha) >= 8

assert buscar_nome([], "Ana") is False
assert buscar_nome(["Ana", "João", "Maria"], "Ana") is True
assert buscar_nome(["Ana", "João", "Maria"], "Carlos") is False

assert tem_senha_valida("1234567") is False
assert tem_senha_valida("12345678") is True
assert tem_senha_valida("123456789") is True
#----------------------------------------------------------------
def classificar_temperatura(temperatura):
    if temperatura < 15:
        return "Frio"
    elif temperatura <= 25:
        return "Agradável"
    else:
        return "Quente"

assert classificar_temperatura(10) == "Frio"
assert classificar_temperatura(14.99) == "Frio"
assert classificar_temperatura(15) == "Agradável"
assert classificar_temperatura(20) == "Agradável"
assert classificar_temperatura(25) == "Agradável"
assert classificar_temperatura(25.01) == "Quente"
assert classificar_temperatura(30) == "Quente"