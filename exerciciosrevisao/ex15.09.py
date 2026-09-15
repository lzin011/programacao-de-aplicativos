def busca_sequencial_indice(vetor, valor):
  for i in range(len(vetor)):
    if vetor[i] == valor:
      return i  
  return -1  


vetor = [12, 45, 7, 23, 56, 89, 34, 2, 90, 15]
valor_procurado = 23
indice = busca_sequencial_indice(vetor, valor_procurado)
print(f"Exercício 1: O valor {valor_procurado} está no índice {indice}.")

def conta_ocorrencias(lista, valor):
  contador = 0
  for item in lista:
    if item == valor:
      contador += 1
  return contador



lista = [4, 2, 7, 2, 9, 2, 5, 8, 2, 1]
valor_procurado = 2
qtd = conta_ocorrencias(lista, valor_procurado)
print(
    f"Exercício 2: O valor {valor_procurado} aparece {qtd} vezes na lista."
)

def buscar_aluno(lista_alunos, nome):
    for i, aluno in enumerate(lista_alunos):
        if aluno.lower() == nome.lower():
            return f"'{nome}' encontrado na posição {i}."
    return f"'{nome}' não foi encontrado na lista."


alunos = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
print(buscar_aluno(alunos, "Carlos"))
print(buscar_aluno(alunos, "Fernanda"))

def primeira_e_ultima_posicao(vetor, numero):
    primeira = -1
    ultima = -1
    for i in range(len(vetor)):
        if vetor[i] == numero:
            if primeira == -1:
                primeira = i
            ultima = i
    return primeira, ultima


numeros = [1, 3, 5, 5, 5, 7, 9]
p, u = primeira_e_ultima_posicao(numeros, 5)
print(f"Primeira posição: {p}, Última posição: {u}")

def busca_binaria(vetor, alvo):
    esquerda, direita = 0, len(vetor) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if vetor[meio] == alvo:
            return meio
        elif vetor[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1


vetor_ordenado = [10, 20, 30, 40, 50, 60]
print("Índice do 40:", busca_binaria(vetor_ordenado, 40))
print("Índice do 25:", busca_binaria(vetor_ordenado, 25))

def busca_palavra(lista_palavras, palavra):
    esquerda, direita = 0, len(lista_palavras) - 1

    while esquerda <= direita:
        meio = (esquerda + direita) // 2
        if lista_palavras[meio] == palavra:
            return True
        elif lista_palavras[meio] < palavra:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return False


dicionario = ["abelha", "bola", "casa", "dado", "elefante"]
print("Contém 'casa'?", busca_palavra(dicionario, "casa"))
print("Contém 'gato'?", busca_palavra(dicionario, "gato"))

def busca_binaria_com_contagem(vetor, alvo):
    esquerda, direita = 0, len(vetor) - 1
    comparacoes = 0

    while esquerda <= direita:
        comparacoes += 1
        meio = (esquerda + direita) // 2

        if vetor[meio] == alvo:
            return meio, comparacoes
        elif vetor[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio - 1

    return -1, comparacoes



indice, comps = busca_binaria_com_contagem([2, 4, 6, 8, 10, 12, 14], 10)
print(f"Índice: {indice}, Comparações: {comps}")

def posicao_insercao(vetor, alvo):
    esquerda, direita = 0, len(vetor)

    while esquerda < direita:
        meio = (esquerda + direita) // 2
        if vetor[meio] < alvo:
            esquerda = meio + 1
        else:
            direita = meio

    return esquerda


vetor = [10, 20, 30, 40, 50]
novo_valor = 25
pos = posicao_insercao(vetor, novo_valor)
print(f"O valor {novo_valor} deve ser inserido na posição: {pos}")

def busca_sequencial_comparacoes(vetor, alvo):
    comparacoes = 0
    for i, val in enumerate(vetor):
        comparacoes += 1
        if val == alvo:
            return i, comparacoes
    return -1, comparacoes


vetor_100 = list(range(1, 101))  
valores_teste = [12, 75, 150]  

print("--- Comparação de Desempenho (100 elementos) ---")
for val in valores_teste:
    _, comp_seq = busca_sequencial_comparacoes(vetor_100, val)
    _, comp_bin = busca_binaria_com_contagem(vetor_100, val)
    print(
        f"Alvo: {val:3} -> Sequencial: {comp_seq:3} comparações | Binária: {comp_bin} comparações"
    )