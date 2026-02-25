valor_total = float(input("digite o valor total da compra "))
cupom = input("digite o nome do cupom ")
 
if cupom == "DEV10":
    valor_com_desconto = valor_total - (0.10 * valor_total)
    print("o valor a ser pago e ", valor_com_desconto)
else:
    print("dados invalidos ")
