print("=========================================================================")
# ====================================================================
# ! TRATAMENTO DE EXCEÇÕES:

def divisao(a,b):
    resultado = a/b 
    print(resultado)

divisao(10,2)

'''
RESULTADO NO CONSOLE:
=========================================================================
5.0
=========================================================================
'''

print("=========================================================================")
# ====================================================================
#VAMOS PENSAR NOS POSSÍVEIS ERROS:

#! TRATAMENTO DE ERROS: Try (tente) x Except (exceção)

def divisao(a,b):
    try:
        resultado = a/b 
        print(resultado)

    except ZeroDivisionError:
        print("Erro: Impossível dividir um valor por zero") 

divisao(10,0)  #Não dá pra dividir 10 por zero!

'''
RESULTADO NO CONSOLE:
=========================================================================
Erro: Impossível dividir um valor por zero
=========================================================================
'''

# Quando tentarmos executar e der erro no console, a frase estranha que aparece deverá ser incluída no exception, com uma frase mais amigável para o nosso usuário
# Erro completo que apareceu no console: ZeroDivisionError: division by zero (utilize apenas -> ZeroDivisionError:)

print("=========================================================================")

def divisao(a,b):
    try:
        resultado = a/b 
        print(resultado)

    except ZeroDivisionError:
        print("Erro: Impossível dividir um valor por zero") 

divisao(10,2)  #Teste com número possível usando try exception

'''
RESULTADO NO CONSOLE:
=========================================================================
5.0
=========================================================================
'''