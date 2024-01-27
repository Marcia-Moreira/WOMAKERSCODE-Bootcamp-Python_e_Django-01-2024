# ====================================================================
# ! EXERCÍCIO 09:
'''
Solicite ao usuário o número de horas de exercício físico por semana. Calcule o total de calorias queimadas e mum mês,considerando uma média de 5 calorias por minuto de exercício.
'''
# ? RESPOSTA:
print("Resposta do Exercício 09: ")

# Imput de Dados pelo usuário:
horas_treino_semana = int(input("Informe o total de horas de treino por semana: "))

# Operações:
total_minutos_mes = (horas_treino_semana * 60) * 4
total_calorias_mes = total_minutos_mes * 5 

# Imprimir no Terminal:
print(f'O seu total de calorias queimadas no mês é de {total_calorias_mes}.')

'''
# RESPOSTA NO TERMINAL:
Resposta do Exercício 09: 
Informe o total de horas de treino por semana: 6
O seu total de calorias queimadas no mês é de 7200.
'''
