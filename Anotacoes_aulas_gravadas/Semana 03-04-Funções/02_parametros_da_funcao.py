print("=========================================================================")
# ====================================================================
# ! PARÂMETROS DE FUNÇÕES:
# Passagens de valores paras diferentes funções aos mesmo tempo

# Declaração da Nossa Função:
def soma_funcao(): #definição da função soma
    # calculo = 10+2
    # Agora o usuário digitando:
    num1 = int(input('Digite o primeiro número: '))
    num2 = int(input('Digite o segundo número: '))
    calculo = num1 + num2
    print(f'O resultado da soma é: {calculo}')
# Chamada da função:
soma_funcao()

'''
Resultado no Console:
=========================================================================
Digite o primeiro número: 8
Digite o segundo número: 2
O resultado da soma é: 10
=========================================================================
'''


print("=========================================================================")
# ====================================================================
# ! PARÂMETROS DE FUNÇÕES: em várias funções

# Declaração da Função:

# SOMA
def soma_funcao(num1,num2):
    soma = num1 + num2
    print(f'O resultado da soma é: {soma}')

# SUBTRAÇÃO
def subtracao_funcao(num1,num2):
    # subtracao = 10-2
    subtracao = num1-num2
    print(f'O resultado da subtração é {subtracao}')

# MULTIPLICAÇÃO
def multiplicacao_funcao(num1,num2):
    # multiplicacao = 10*2
    multiplicacao = num1*num2
    print(f'O resultado da multiplicação é {multiplicacao}')

# Input (será a primeira linha lida no código) #Para não precisar pedir resposta do usuário várias vezes
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))

# Chamada da função:
soma_funcao(num1,num2)
subtracao_funcao(num1,num2)
multiplicacao_funcao(num1,num2)
# Sempre que passamos valores, precisamos receber na declaração
'''
Resultado no Console:
=========================================================================
Digite o primeiro número: 8
Digite o segundo número: 2
O resultado da soma é: 10
O resultado da subtração é 6
O resultado da multiplicação é 16
=========================================================================
'''

print("=========================================================================")









