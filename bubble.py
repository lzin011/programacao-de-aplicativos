alunos = ["Pedro", "Ana", "Lucas", "Beatriz", "Carlos"]

for i in range(len(alunos)):
    for j in range(len(alunos) - i - 1):
        if alunos[j] > alunos[j + 1]:
            alunos[j], alunos[j + 1] = alunos[j + 1], alunos[j]
            print(alunos)

print(alunos)