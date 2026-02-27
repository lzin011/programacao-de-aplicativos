nivel =int (input("fale teu nivel atual: "))
esferas =int (input("fale as quantidades de esferas coletadas: "))

if nivel >= 20 and esferas >= 50:
    print("habilidade super salto desbloqueada!")

elif nivel < 20 and esferas < 50: 
    print("requisitos insuficientes para nova habilidade")
