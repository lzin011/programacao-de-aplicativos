cargo = input("insira o seu cargo ")
code = int(input("codigo de acesso "))
botao = input("botao de emergencia pressionado (s/n)")
epi = input("EPIcompleto? (s/n)")

if(cargo == "ENGENHEIRO" or "TECNICO") and (code == 2411 or botao == "s") and epi =="s":
    print("ACESSO LIBERADO")
else:
    print("ACESSO NEGADO")
