import sqlite3
conexao = sqlite3.connect('escola_demonstracao.db')
cursor = conexao.cursor()


def criar():
    try:

        cursor.execute ('''CREATE TABLE IF NOT EXISTS professores ( 
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            nome TEXT NOT NULL,
                            telefone TEXT,             
                            materia TEXT,
                            idade INTEGER,
                            cpf TEXT UNIQUE NOT NULL,
                            salario REAL,
                            nome da escola TEXT,
                        )''')
                            
                        
        nome_professor = input("qual o nome do professor: ")
        telefone = input("qual o telefone do professor: ")
        materia = input("qual a materia: ")
        idade = int(input("qual sua idade: ") )
        cpf_professor = input("digite o cpf: ")
        salario = int(input("digite seu salario: "))
        nome_da_escola = input("qual o nome da escola: ") 
        
        comando_inserir = (f''' 
                        INSERT into professores (nome, telefone, materia, idade, cpf, salario, escola)
                        VALUES('{nome_professor}','{telefone}','{materia}',{idade},'{cpf_professor}',{salario},'{nome_da_escola}',''') 
                            
        cursor.execute(comando_inserir)

        conexao.commit()
        except ValueError:
            print("erro de valor no cadastro tente novamente")
        except TypeError:
            print("erro de tipo de dados") 
        except NameError:
            print("erro de valor no cadastro tente novamente")	
        except IndexError:
            print("erro de indice fora dos limites")	
        except KeyError:
            print("erro de chave")	
        except AttributeError:
            print("erro de objeto")	
        except ZeroDivisionError:
            print("erro de tentativa de dividir")
        except FileNotFoundError:
            print("erro de arquivo nao encontrado")	
        except PermissionError:
            print("erro de permissao para acessar arquivo")	
        except ImportError:
            print("erro de importacao de um modulo")
        except ModuleNotFoundError:
            print("erro de modulo nao encontrado")	
        except RuntimeError:
            print("erro generico em tempo de execucao")	
        except OverflowError:
            print("erro de numero execedido ao limite")	
        except MemoryError:
            print("erro de memoria insuficiente")
        except KeyboardInterrupt:
            print("erro de usuario, interrompeu o programa")	
        except EOFError:
            print("erro de fim inesperado")
        except Exception:
            print("Classe base da maioria dos erros.")	
        finally:
            conexao.close

      
def listar():
    try:

        cursor.execute("SELECT * FROM professores") 
        professores = cursor.fetchall()

        for professor in professores: 
            print(f"ID: {professor[0]}")
            print(f"Nome: {professor[1]}")
            print(f"Telefone: {professor[2]}")
            print(f"materia: {professor[3]}")
            print(f"Idade: {professor[4]}")
            print(f"CPF: {professor[5]}")
            print(f"salario: {professor[6]}")
            print(f"escola: {professor[7]}")
        

def alterar():
    try: 

        id_professor = int(input("Qual é o teu ID: "))

        cursor.execute(f'''SELECT * FROM professores WHERE id = {id_professor}''')
        professores = cursor.fetchone()

        if not id_professor:
            print("Não encontrado!")
        else:
            novo_nome = input("qual o novo nome: ")
            novo_telefone = input("qual o novo telefone: ")
            novo_materia = input("qual a nova materia: ")
            novo_idade = int(input("qual a nova idade: "))
            novo_cpf = input("qual o novo cpf: ")
            novo_salario = float(input("qual o novo salario: "))
            novo_nome_de_escola = input("qual o novo nome: ")

            comando = f'''UPDATE professores SET nome = '{novo_nome}',telefone = '{novo_telefone}',materia = '{novo_materia}',idade = {novo_idade},cpf = '{novo_cpf}',salario = {novo_salario},escola = '{novo_escola}' WHERE id ={id_professor}'''
            
            conexao.commit()
            except ValueError:
                print("erro de valor no cadastro tente novamente")
            except TypeError:
                print("erro de tipo de dados") 
            except NameError:
                print("erro de valor no cadastro tente novamente")	
            except IndexError:
                print("erro de indice fora dos limites")	
            except KeyError:
                print("erro de chave")	
            except AttributeError:
                print("erro de objeto")	
            except ZeroDivisionError:
                print("erro de tentativa de dividir")
            except FileNotFoundError:
                print("erro de arquivo nao encontrado")	
            except PermissionError:
                print("erro de permissao para acessar arquivo")	
            except ImportError:
                print("erro de importacao de um modulo")
            except ModuleNotFoundError:
                print("erro de modulo nao encontrado")	
            except RuntimeError:
                print("erro generico em tempo de execucao")	
            except OverflowError:
                print("erro de numero execedido ao limite")	
            except MemoryError:
                print("erro de memoria insuficiente")
            except KeyboardInterrupt:
                print("erro de usuario, interrompeu o programa")	
            except EOFError:
                print("erro de fim inesperado")
            except Exception:
                print("Classe base da maioria dos erros.")	
            finally:
            print(" Dados alterados ")

def deletar():
    try:

        conexao = sqlite3.connect("escola_demonstracao.db")
        cursor = conexao.cursor()

        listar()

        id_professor = int(input(" Qual ID deseja deletar: " ))

        cursor.execute(f'''DELETE FROM professor WHERE Id = {id_professor}''')

        conexao.commit()
       
        except ValueError:
            print("erro de valor no cadastro tente novamente")
        except TypeError:
            print("erro de tipo de dados") 
        except NameError:
            print("erro de valor no cadastro tente novamente")	
        except IndexError:
            print("erro de indice fora dos limites")	
        except KeyError:
            print("erro de chave")	
        except AttributeError:
            print("erro de objeto")	
        except ZeroDivisionError:
            print("erro de tentativa de dividir")
        except FileNotFoundError:
            print("erro de arquivo nao encontrado")	
        except PermissionError:
            print("erro de permissao para acessar arquivo")	
        except ImportError:
            print("erro de importacao de um modulo")
        except ModuleNotFoundError:
            print("erro de modulo nao encontrado")	
        except RuntimeError:
            print("erro generico em tempo de execucao")	
        except OverflowError:
            print("erro de numero execedido ao limite")	
        except MemoryError:
            print("erro de memoria insuficiente")
        except KeyboardInterrupt:
            print("erro de usuario, interrompeu o programa")	
        except EOFError:
            print("erro de fim inesperado")
        except Exception:
            print("Classe base da maioria dos erros.")	
        finally:
            conexao.close



def menu():
    try:
      
        while True:
            print("\n--- TABELA PROFESSORES ---")
            print("\n=== SISTEMA ESCOLAR ===")  
            print("1. Cadastrar professor") 
            print("2. Listar professor") 
            print("3. Atualizar professor") 
            print("4. Excluir professor") 
            print("5. Sair")
                
            opcao = input("Escolha uma opção: ")

            if opcao == '1': criar()
            elif opcao == '2': listar() 
            elif opcao == '3': alterar() 
            elif opcao == '4': deletar() 
            elif opcao == '5': break
            else: print("Opção inválida!")

            except ValueError:
                print("erro de valor no cadastro tente novamente") 

    menu()


    

  

     
     