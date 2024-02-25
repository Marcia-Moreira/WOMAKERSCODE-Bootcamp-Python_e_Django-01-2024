
# ====================================================================
# ! OPERAÇÕES MATEMÁTICAS:

# soma = +
# Subtração = -
# Multiplicação = *
# Divisão = /  (retorna sempre decimal com ponto/virgula)
# Divisão INTEIRA = //  # ? (Não deixa retornar resultado com ponto/virgula)

# CLEAR no terminal, limpa ele.

# ====================================================================
# SOMA
print("SOMA")
soma_numero1 = int(input("Digite o numero 01: "))
soma_numero2 = int(input("Digite o numero 02: "))
soma = soma_numero1 + soma_numero2
print(soma)
# Obs: se não escrevermos INT ele iria concatenar os números

# ====================================================================
# SUBTRAÇÃO
print("SUBTRAÇÃO")
subtracao_numero_1 = int(input('Digite o número 01: '))
subtracao_numero_2 = int(input("Digite o numero 02: "))
subtração = subtracao_numero_1 - subtracao_numero_2
print(subtração)


# ====================================================================
# MULTIPLICAÇÃO
print("MULTIPLICAÇÃO")
multiplicacao_numero_1 = int(input('Digite o número 01: '))
multiplicacao_numero_2 = int(input("Digite o numero 02: "))
multiplicacao = multiplicacao_numero_1 * multiplicacao_numero_2
# ou
# multiplicacao = multiplicacao_numero_1*3
print(multiplicacao)


# ====================================================================
# DIVISÃO (retorna sempre decimal com ponto/virgula)
print("DIVISÃO")
divisao_numero_1 = int(input('Digite o número 01: '))
divisao_numero_2 = int(input("Digite o numero 02: "))
divisao = divisao_numero_1 / divisao_numero_2
print(divisao)

# ====================================================================
# DIVISÃO INTEIRA  (Não deixa retornar resultado com ponto/virgula)
print("DIVISÃO INTEIRA")
divisao_inteira_numero_1 = int(input('Digite o número 01: '))
divisao_inteira_numero_2 = int(input("Digite o numero 02: "))
divisao_inteira = divisao_inteira_numero_1 // divisao_inteira_numero_2
print(divisao_inteira)


# ====================================================================
# ! IMPRESSO NO TERMINAL:

'''
SOMA
Digite o numero 01: 5
Digite o numero 02: 2
7
SUBTRAÇÃO
Digite o número 01: 7
Digite o numero 02: 3
4
MULTIPLICAÇÃO
Digite o número 01: 5
Digite o numero 02: 3
15
DIVISÃO
Digite o número 01: 8
Digite o numero 02: 3
2.6666666666666665
DIVISÃO INTEIRA
Digite o número 01: 8
Digite o numero 02: 3
2
'''

