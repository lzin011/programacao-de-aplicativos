def avaliar_desempenho(nota):
    if nota >= 9:
        return "Excelente"
    elif nota >= 7:
        return "Bom"
    elif nota > 5:
        return "Regular"
    else:
        return "Insuficiente"

nota = float(input("Digite a nota (0 a 10): "))
print("Desempenho:", avaliar_desempenho(nota))
