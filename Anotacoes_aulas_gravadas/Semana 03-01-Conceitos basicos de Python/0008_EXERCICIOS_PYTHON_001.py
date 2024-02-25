
#! EXERCÍCIOS PYTHON 001:

# INSTRUÇÕES DE ENTREGA:

'''
BootcampBack-End Python e Django 
Orientações entrega do sExercícios

Obs.:Não aceita formatação!
1.Osprojetosdevemserpublicadasemumrepositóriodogithubcomtodososexercíciosresolvidoseseparadosempastasparaquepossaficarfácildeidentificar;

Abranchdeveseguirestepadrão:
Ex: ExerciciosPython_SquadBerthaLutz
[NomeDesafio]_[NomedaSquad] 

2.CriemumreadMecomonomedetodasasintegrantesdaequipeecomoseorganizaramparafazeraresoluçãodosdesafios;3.Todasdeverãocontribuirnesserepositóriocriado;4.Paraavançarparaaspróximasliçõesdocurso,énecessárioinformarolinkdorepositóriodoprojetonaplataforma.Pedimosquetodasdogrupoinformemomesmolinkcomoread.medetalhadocomocitadoacima;5.Compartilhemconhecimentoenãotenhammedodeperguntar!

'''

#! 001 - EXERCÍCIOS CONCEITOS BÁSICO DE PYTHON

# ====================================================================
# ! EXERCÍCIO 01:
'''
Faça um Programa que peça dois números, realize as principais
operações soma, subtração, multiplicação, divisão

'''
print("Resposta do Exercício 01: ")

# Imput de Dados pelo usuário:
numero_1= int(input('Digite um número inteiro: '))
numero_2 = int(input("Digite outro número inteiro: "))

# Operações:
soma = numero_1 + numero_2
subtracao = numero_1 - numero_2
multiplicacao = numero_1 * numero_2
divisao = numero_1 / numero_2
divisao_inteira = numero_1 // numero_2

# Imprimir no Terminal:
print(soma)
print(f"O Resultado da soma é {soma}.")
print(subtracao)
print(f'O Resultado da subtração é {subtracao}.')
print(multiplicacao)
print(f"O Resultado da multiplicação é {multiplicacao}.")
print(divisao)
print(f'O resultado da divisão é {divisao:.2f}.')
print(divisao_inteira)
print(f"O resultado da Divisão Inteira é {divisao_inteira}.")

'''
# RESPOSTA NO TERMINAL:
Resposta do Exercício 01: 
Digite um número inteiro: 6
Digite outro número inteiro: 4
10
O Resultado da soma é 10.
2
O Resultado da subtração é 2.
24
O Resultado da multiplicação é 24.
1.5
O resultado da divisão é 1.50.
1
O resultado da Divisão Inteira é 1.
'''

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


# ====================================================================
# ! EXERCÍCIO 05:
'''
 Escreva um programa que calcule o salário líquido. Lembrando de
declarar o salário bruto e o percentual de desconto do Imposto de
Renda.
● Renda até R$ 1.903,98: isento de imposto de renda;
● Renda entre R$ 1.903,99 e R$ 2.826,65: alíquota de 7,5%;
● Renda entre R$ 2.826,66 e R$ 3.751,05: alíquota de 15%;
● Renda entre R$ 3.751,06 e R$ 4.664,68: alíquota de 22,5%;
● Renda acima de R$ 4.664,68: alíquota máxima de 27,5%.
'''

# ? RESPOSTA:
print("Resposta do Exercício 05: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 06:
'''
Escreva um programa que calcule o tempo de uma viagem. Faça um
comparativo do mesmo percurso de avião, carro e ônibus.
Levando em consideração:
● avião = 600 km/h
● carro = 100 km/h
● ônibus = 80 km/h
'''
# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 07:
'''
Solicite ao usuário o peso em kg e a altura em metros. Calcule e
imprima o Índice de Massa Corporal (IMC) usando a fórmula:
IMC = peso / (altura x altura).

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 08:
'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.Calcule e mostre o total do seu salário no referido mês.
'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

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

# ====================================================================
# ! EXERCÍCIO 10:
'''
Faça um Programa que utilize 4 variáveis como preferir e no final print uma mensagem amigável utilizando as variáveis criadas. Exemplos de variáveis: nome, idade, lugar, profissão.... Exemplo de retorno: Olá Maria,prazer te conhecer. Sou de São Paulo também eestou migrando de área.Lembrando que para o retorno vamos usar print com as variáveis criadas e este texto é somente um exemplo, utilizem a criatividade.
'''

# ? RESPOSTA:
print("Resposta do Exercício 10: ")
# Imput de Dados pelo usuário:

# Seu nome / de onde é? / o que está estudando? / está procurando emprego?
nome_01 = input("Qual é o seu nome? ")
natural = input("De onde você é? ")
estuda = input("O que está estudando? ")
emprego = int(input("Quantos anos você tem? "))

# Operações:
# concatenação de frases e variáveis

# Imprimir no Terminal:
print (f'Oi {nome_01}, prazer! Vejo aqui que você é do {natural}, estuda {estuda} e tem {emprego} anos nesse momento!')

# RESPOSTA NO TERMINAL:
'''
Resposta do Exercício 10: 
Qual é o seu nome? Marcia
De onde você é? Rio de Janeiro
O que está estudando? Programação
Quantos anos você tem? 42
Oi Marcia, prazer! Vejo aqui que você é do Rio de Janeiro, estuda Programação e tem 42 anos nesse momento!
'''

# ====================================================================
# ! EXERCÍCIO 11:
'''
'''
# ? RESPOSTA:
print("Resposta do Exercício 10: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL: