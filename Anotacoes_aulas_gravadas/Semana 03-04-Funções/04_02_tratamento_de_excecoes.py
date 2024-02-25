print("=========================================================================")
# ==============================================================================
#! TRATAMENTO DE ERROS: Try (tente) x Except (exceção) E "AS E:"
#
def divisao(a,b):
    try:
        resultado = a/b 
        print(resultado)

    # Erro se o usuário tentar dividir números por zero:
    except ZeroDivisionError:
        print("Erro: Impossível dividir um valor por zero")
    # Erro se o usuário tentar dividir número por texto:
    except TypeError as e:
        print(f'Erro: O tipo do dado informado está incorreto. \n Detalhes: {e}')
    # Conclui caso a divisão seja possível e não prevista nas tratativas acima
    else:
        print('Sem exceções de erro!') 

# divisao(10,0)     #Não dá pra dividir 10 por zero!
# divisao(10, 2)    #Funciona
divisao(10, 'womarkercode')     #TypeError - Não dá pra dividir por TIPO palavras    

'''
RESULTADO NO CONSOLE:
=========================================================================
Erro: O tipo do dado informado está incorreto.
 Detalhes: unsupported operand type(s) for /: 'int' and 'str'
=========================================================================
'''

'''
#! DICAS E ANOTAÇÕES:
"As E:" permite darmos mais informações de detalhes do erro {e}
A professora menciona lista de principais Tratativas de Erro
'''

print("=========================================================================")
# ==============================================================================



