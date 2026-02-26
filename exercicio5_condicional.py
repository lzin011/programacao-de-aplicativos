idade = int(input("digite sua idade ")) 
dinheiro = float(input("digite o saldo que tem em sua carteira "))

if idade >= 18 and dinheiro >= 50:
     
    print("acesso altorizado, bem vindo ao evento! ")

elif idade < 18 and dinheiro < 50:
    print("infelizmente voce não cumpre os requisitos de entrada ")
