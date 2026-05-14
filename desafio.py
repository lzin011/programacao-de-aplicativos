def criar_arquivo():
    open('alunos.txt','w').close()

def criar():
    lugar = input("destino: ")
    with open('destino.txt','a') as f:
        f.write(lugar + '\n')
    print("destino adicionado à lista!")
criar()


def lista():
    with open('alunos.txt','r') as f:
        alunos = f.readlines()


def atualizar():
    ler()
    idx = int(input("digite o ID do destino que quer alterar: "))
    novo_nome = input ("novo destino: ")
    with open ('viagens.txt', 'r') as f:
        lugar = f.readlines()0
