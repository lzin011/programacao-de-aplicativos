def calcular_area(largura, comprimento):
    return largura * comprimento

for i in range(3):
    largura = float(input(f"Terreno {i+1} - largura: "))
    comprimento = float(input(f"Terreno {i+1} - comprimento: "))
    print("Área:", calcular_area(largura, comprimento))
