nome_usuario = input("digite o nome de usuario ")
senha = int(input("digite sua senha "))

if nome_usuario == "admin" and senha == 12345:
    print("acesso permitido ")
else:
    print("acesso negado ")
