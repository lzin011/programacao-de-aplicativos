import json

def cadastrar_aluno():
    cpf_aluno = int(input("digite seu cpf: "))
    nome_aluno = input("qual o seu nome: ")
    telefone_aluno = int(input("qual o seu telefone "))
    turma = input("qual a sua turma: ")
    idade_aluno = int(input("qual sua idade: "))

aluno = {"cpf":cpf_aluno
         "nome":nome_aluno
         "telefone":telefone_aluno
         "turma":turma
         "idade":idade_aluno }
with open (f"cadastro.json",'r')as arquivo:
    json.dump(aluno,cadastro.json, indent=4, ensure-ascii=false)



