livros_disponiveis = ["Python Pro", "Banco de Dados", "Redes", "IA", "hardware"]
livros_emprestados = []
tarefas = input("digite o nome do livro que deseja: ")

if tarefas in livros_disponiveis:
    livros_disponiveis.remove(tarefas)
    livros_emprestados.append(tarefas)
else:
    print("desculpa, esse livro nao esta no acervo")

tarefas = input("digite o nome do livro que esta devolvendo")
if tarefas in livros_emprestados:
    livros_emprestados.remove(tarefas2)
    livros_disponiveis.append(tarefas2)
else:
    print("este livro nao consta como emprestado")

del livros_disponiveis[0:2]

print(f"estado final das duas listas. {livros_disponiveis} e {livros_emprestados}.")