def gerar_relatorio_saude(nome, peso, altura, idade):
    imc = peso / (altura ** 2)
    
    if imc < 18.5:
        categoria = "Baixo peso"
    elif imc < 25:
        categoria = "Normal"
    elif imc < 30:
        categoria = "Sobrepeso"
    else:
        categoria = "Obesidade"
    
    return f"{nome}, {idade} anos, tem IMC {imc:.2f} e está na categoria: {categoria}"

nome = input("Nome: ")
peso = float(input("Peso (kg): "))
altura = float(input("Altura (m): "))
idade = int(input("Idade: "))

print(gerar_relatorio_saude(nome, peso, altura, idade))