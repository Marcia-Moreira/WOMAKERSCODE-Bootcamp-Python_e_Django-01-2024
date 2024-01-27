# ====================================================================
# ! EXERCÍCIO 03:
'''
Faça um Programa que peça a quantidade de quilômetros, transforme
em metros, centímetros e milímetros.
'''

# ? RESPOSTA:
print("Resposta do Exercício 03: ")
print("Conversor de Medidas:")

# Imput de Dados pelo usuário:
quilometros = int(input('Informe o total de quilômetros: '))

# Operações:
conversao_metros = quilometros * 1000
conversao_centimetros = quilometros * 100000
conversao_milimetros = quilometros * 1000000

# Imprimir no Terminal:
print(f'{quilometros} quilômetros é equivalente à {conversao_metros} metros.')
print(f'{quilometros} quilômetros é equivalente à {conversao_centimetros} centímetros.')
print(f'{quilometros} quilômetros é equivalente à {conversao_milimetros} milimetros.')

'''
# RESPOSTA NO TERMINAL:
Resposta do Exercício 03:
Conversor de Medidas:
Informe o total de quilômetros: 20
20 quilômetros é equivalente à 20000 metros.
20 quilômetros é equivalente à 2000000 centímetros.
20 quilômetros é equivalente à 20000000 milimetros.
'''