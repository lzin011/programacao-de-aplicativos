idade = int(input("digite sua idade "))
ingresso = input("possui ingresso? (S/N) ")
lista = input("esta na lista? (S/N) ")

if idade >= 18 and ingresso == "s" or lista == "s":
    print("acesso permitido ")
elif idade < 18 and ingresso == "n" or lista =="n":
    print("acesso negado ")
