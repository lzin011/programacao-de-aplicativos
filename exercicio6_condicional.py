media = float(input("digite a media: "))
presenca = int(input("digite sua porcentagem de presenca: "))

if media >= 7.0 and presenca >= 75: 
    print("parabens, vc passou! ")

elif media < 7.0 and presenca < 75: 
    print("reprovado, verifique sua nota ou presenca ")