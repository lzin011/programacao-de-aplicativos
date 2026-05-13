def criar_arquivo():
    open('alunos.txt','w').close()

def criar():
    lugar = input("destino: ")
    with open('alunos.txt','a') as f:
        f.write(lugar + '\n')
    print("destino adicionado à lista!")
criar()