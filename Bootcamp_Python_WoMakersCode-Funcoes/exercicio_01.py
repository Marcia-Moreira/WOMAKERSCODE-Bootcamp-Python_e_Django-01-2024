'''
*=========================================================================================
?   PROJETO ->> BOOTCAMP BACK END PYTHON E DJANGO 2024.1-WOMAKERSCODE(Mais Mulheres em Tech)
?   OBJETIVO ->> CHALLENGER O2 - FUNÇÕES EM PYTHON.
?   CRIAÇÃO E DESENVOLVIMENTO ->> Marcia Moreira
?   DATA DA CRIAÇÃO ->> 06/02/2024 a 07/02/2024.
?   MEU GITHUB ->> https://github.com/Marcia-Moreira
?   MEU LINK WAKATIME ->> https://wakatime.com/@Marcia_Moreira
?   MEU LINKEDIN ->> https://www.linkedin.com/in/marciamoreiramm
*========================================================================================
'''
print("\n=========================================================================")
# ================================================================================
# ! EXERCÍCIO 01:
'''
 1. Faça um programa, com uma função que necessite de três
 argumentos, e que forneça a soma desses três argumentos.
'''
# ? RESPOSTA:
print("\nResposta do Exercício 01: \n")

print(" - CALCULADORA DE SOMA - \n")

def soma_argumentos():
    # soma_3 = 1+2+3
    argumento_1 = int(input("Digite o primeiro número: "))
    argumento_2 = int(input("Digite o segundo número: "))
    argumento_3 = int(input("Digite o terceiro número: "))
    soma_numeros = argumento_1 + argumento_2 + argumento_3
    print(f"\nA soma dos 3 números é: {soma_numeros}.")

soma_argumentos() 
'''
#? RESPOSTA NO TERMINAL:
=========================================================================
# Teste: 1 2 3

Resposta do Exercício 01:

 - CALCULADORA DE SOMA -

Digite o primeiro número: 1
Digite o segundo número: 2
Digite o terceiro número: 3
A soma dos 3 números é: 6.

=========================================================================
'''
print("\n=========================================================================")
# ================================================================================