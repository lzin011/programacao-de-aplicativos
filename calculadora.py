peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))

imc = peso / (altura ** 2)

print("Seu IMC é:", imc)

if imc > 25:
    print("Você está com sobrepeso ")
else:
    print("Você não está com sobrepeso ")