def senha_valida(senha):
    return len(senha) >= 6

while True:
    senha = input("Digite uma senha: ")
    if senha_valida(senha):
        print("Senha cadastrada com sucesso!")
        break
    else:
        print("Senha muito curta, tente novamente.")
