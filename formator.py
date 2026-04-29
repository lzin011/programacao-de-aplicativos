def gerar_etiqueta(rua, numero, bairro, cidade, cep, urgencia=False):
    prefixo = "URGENTE | " if urgencia else ""
    return f"{prefixo}RUA: {rua}, Nº: {numero} - {bairro} - {cidade} - CEP: {cep}"


print(gerar_etiqueta(
    input("Rua: "),
    input("Número: "),
    input("Bairro: "),
    input("Cidade: "),
    input("CEP: "),
    input("É urgente? (s/n): ").lower() == 's'
))