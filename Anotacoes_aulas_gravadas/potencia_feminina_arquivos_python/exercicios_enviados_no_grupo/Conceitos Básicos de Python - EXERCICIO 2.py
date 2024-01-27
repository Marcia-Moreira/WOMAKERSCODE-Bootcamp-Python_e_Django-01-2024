# ====================================================================
# ! EXERCÍCIO 02:
'''
Peça ao usuário para informar o ano de nascimento. Em seguida,
calcule e imprima a idade atual.

'''
# ? RESPOSTA:
print("Resposta do Exercício 02: ")

# Imput de Dados pelo usuário:
ano_nascimento = int(input('Informe o ano do seu nascimento: '))
ano_atual = int(input('Informe o ano atual: '))

# Operações:
sua_idade = ano_atual - ano_nascimento

# Imprimir no Terminal:
print(sua_idade)
print(f'Sua idade é {sua_idade} anos.')

'''
# RESPOSTA NO TERMINAL:
Resposta do Exercício 02:
Informe o ano do seu nascimento: 1981
Informe o ano atual: 2024
43
Sua idade é 43 anos.
'''
