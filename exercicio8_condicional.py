nome = "admin"

codigo = int (input("digite seu codigo "))
usuario = input("digite seu usuario")
 
if usuario == "admin" and codigo == 999:
    print("acesso liberado")
else:
    print("falha")
