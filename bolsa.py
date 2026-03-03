media = float(input("qual sua media "))
renda = float(input("qual a renda da sua familia "))
escola = input("voce veio da escola publica? (s/n)")

if media >= 8.0 and renda >= 2.000 or escola == "s":
    print("voce passou ")
elif media < 8.0 and renda < 2.000 or escola == "n":
    print("voce nao passou ")