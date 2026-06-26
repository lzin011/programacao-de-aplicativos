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