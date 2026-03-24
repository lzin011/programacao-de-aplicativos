pendentes = ["Relatorio.pdf", "Foto.png", "Planilha.xlsx"]
concluidos = []

# Remove o primeiro item de 'pendentes'
arquivo = pendentes.pop(0)

# Adiciona esse item em 'concluidos'
concluidos.append(arquivo)

# Exibe as listas
print("Pendentes:", pendentes)
print("Concluídos:", concluidos)