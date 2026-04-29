def verificar_aprovacao(nota_teste, anos_xp, possui_certificacao):
    if (nota_teste > 80 and anos_xp > 2) or possui_certificacao:
        return True
    return Falsenota = float(input("Nota do teste: "))
xp = int(input("Anos de experiência: "))
cert = input("Possui certificação? (s/n): ").lower() == 's'

if verificar_aprovacao(nota, xp, cert):
    print("Contratar")
else:
    print("Descartar")