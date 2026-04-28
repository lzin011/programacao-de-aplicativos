def sofrer_dano(vida, dano):
    return vida - dano

vida = 100

while vida > 0:
    dano = int(input("Quanto dano o monstro causou? "))
    vida = sofrer_dano(vida, dano)
    print("Vida atual:", vida)

print("Game Over!")