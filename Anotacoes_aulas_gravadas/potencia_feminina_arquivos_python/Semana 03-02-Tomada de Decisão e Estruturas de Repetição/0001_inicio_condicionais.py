# ====================================================================
# ! ESTRUTURAS CONDICIONAIS: IF E ELSE

# SE e SENÃO = IF e else
# If idade > 17: a condição será executada
# ELSE: a condição será executada se anterior for falsa
# Usado para descobrir se uma instrução é verdadeira ou falsa!

# ENQUANTO = WILE  (Enquanto algo acontecer... execute xyz)
# WHILE idade >17 (enquanto a condição for verdadeira, esta condição será executada)

# PARA CADA = FOR  (Para cada Item ele toma uma condição)
# for maçã in frutas -> Para cada maçã na lista de frutas, será executada essa condição.

# ====================================================================
#? IF e ELSE

numero_if_else = int(input('Digite seu número: '))

if numero_if_else > 0:
    print('Número é positivo!')
else:
    print('Número é negativo!')

# ! IMPRESSO NO TERMINAL:
'''
Digite seu número: 5
Número é positivo!

'''

# ====================================================================
#? WILE -> Enquanto a condição for verdadeira, esta condição será executada.

# Neste Código, caso usuário, fique digitando número negativo, ficará dando erro em loopíng, até que seja digitado um número positivo.

numero_while = -1
while numero_while < 0:
    numero_while = int(input('Digite seu número: '))
# Quando não satisfazer maiso While, cairá no próximo print:
print("Número positivo inserido com sucesso!")

# ! IMPRESSO NO TERMINAL:
'''
Digite seu número: -6
Digite seu número: -8
Digite seu número: -2
Digite seu número: -4
Digite seu número: -6
Digite seu número: 8
Número positivo inserido com sucesso!
'''
# ====================================================================
#? FOR -> # PARA CADA 
# FOR  (Para cada Item ele toma uma condição)
# for maçã in frutas -> Para cada maçã na lista de frutas, será executada essa condição.

# CRIAR UMA LISTA EM PYTHON:
frutas = ['Maçã', 'Banana', 'Uva'] #Declaração de uma lista
for fruta in frutas:  #para cada
    print(fruta)
# Leia-se: Para cada fruta em Lista Frutas, imprima fruta.

# ! IMPRESSO NO TERMINAL:
'''
Maçã
Banana
Uva
'''

# ====================================================================
#  -> 



# ====================================================================
#  -> 





# ====================================================================
# ! IMPRESSO NO TERMINAL:

'''

'''