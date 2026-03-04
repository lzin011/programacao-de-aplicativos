valor = float(input("qual o valor da compra? "))
ass = input("é assinante prime? (s/n) ")
frete = 50.00
if valor >= 500 or ass == "sim" and valor >= 100:
    frete = 0.00

valorfinal = valor + frete 
print("frete: ", frete )
print("total a pagar", valorfinal )