curso = input("voce concluiu o curso de segurança? (s/n) ")

if curso == "n":
    print: ("acesso negado")
elif curso == "s": 
     instrutor = input("o instrutor esta presente? (s/n)")
     if instrutor == "s":
        print("acesso liberado")
        elif instrutor == "n":
        print("aguarde o instrutor") 