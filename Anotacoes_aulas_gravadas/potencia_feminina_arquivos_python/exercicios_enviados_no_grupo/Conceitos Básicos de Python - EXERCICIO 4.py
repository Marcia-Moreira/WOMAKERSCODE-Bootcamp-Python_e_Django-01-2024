# ====================================================================
# ! EXERCÍCIO 04:
'''
Receba do usuário a quantidade de litros de combustível consumidos e
a distância percorrida. Calcule e imprima o consumo médio em km/l.
'''

# ? RESPOSTA:
print("Resposta do Exercício 04: ")

# Imput de Dados pelo usuário:
distancia_percorrida = int(input("Informe a distância total percorrida: "))
combustivel_consumido = int(input("Informe o total de combustível consumido: "))

# Operações:
consumo_medio = distancia_percorrida / combustivel_consumido

# Imprimir no Terminal:
print(f'O consumo médio é de {consumo_medio}.')

'''
# RESPOSTA NO TERMINAL:
Resposta do Exercício 04:
Informe a distância total percorrida: 20
Informe o total de combustível consumido: 10
O consumo médio é de 2.0.
'''