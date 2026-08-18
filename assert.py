def eh_par(numero):
    try:
        return numero % 2 == 0

assert eh_par(4) is True          
assert eh_par(5) is False        
assert eh_par(0) is True          
assert eh_par(-4) is True       
assert eh_par(-5) is False

    except Exception as erro:
        print("Erro:", erro)
    finally:
        print("codigo encerrado")



