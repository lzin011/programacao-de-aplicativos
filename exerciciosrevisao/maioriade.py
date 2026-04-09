from datetime import datetime

ano_nascimento = int(input("Digite seu ano de nascimento: "))

ano_atual = datetime.now().year

idade = ano_atual - ano_nascimento

if idade >= 18:
    print(f"Você tem {idade} anos e já é maior de idade.")
else:
    print(f"Você tem {idade} anos e ainda não é maior de idade.")