def converter_km_para_ms(velocidade):
    return velocidade / 3.6

vel = float(input("Digite a velocidade em km/h: "))
if vel > 80:
    print("Velocidade em m/s:", converter_km_para_ms(vel))
    print("Reduza a velocidade!")

