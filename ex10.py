vagas = ["ocupado", "livre", "ocupado", "livre"]
vaga = int(input("digite o numero de uma vaga (0 a 3): "))

if vaga %2 == 0 or vagas == "livres":
    print(f"vaga autorizada para estacionar.")
else:
    print(f"vaga{indice} indisponivel ou fora das regras.")