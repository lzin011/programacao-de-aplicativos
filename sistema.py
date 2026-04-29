def calcular_preco_final(valor_base, imposto_percentual, cupom_desconto):
    valor_com_imposto = valor_base + (valor_base * imposto_percentual / 100)
    preco_final = valor_com_imposto - cupom_desconto
    
    return max(preco_final, 0)
 
