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
# ! EXERCÍCIO 03:
'''
 3. Escreva um script que pergunta ao usuário se ele deseja converter
 uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
 cada opção, crie uma função.
 Plus: Crie uma terceira, que é um menu para o usuário escolher a opção
 desejada, onde esse menu chama a função de conversão correta.
'''
# ? RESPOSTA:
print("\nResposta do Exercício 03: \n")

print(" - CONVERSOR DE TEMPERATURA - \n")

def conversor_temperatura():
    celsius = "C"
    fahrenheit = "F"

    if tipo_origem == "C":
        converte_cel_para_fah = temperatura_origem * 1.8 + 32
        print(f"Você informou {temperatura_origem} graus º{tipo_origem}!")
        print(f"Essa temperatura convertida para Fahrenheit é: {converte_cel_para_fah:.1f} graus.")
        #Se temperatura_origem for ºC
        # converte_cel_para_fah = (temperatura_origem * 1,8) + 32
        #Multiplicamos a temperatura em ºC por 1,8 e somamos 32 ao resultado.

    else:
        converte_fah_para_cel = (temperatura_origem - 32) / 1.8
        print(f"\nVocê informou {temperatura_origem} graus º{tipo_origem}!")
        print(f"\nEssa temperatura convertida para Celsius é: {converte_fah_para_cel:.1f} graus.")
        #Se temperatura_origem for ºF
        # converte_fah_para_cel = (temperatura_origem - 32) / 1,8
        #Subtraímos a temperatura em ºF por 32 e dividimos o resultado por 1,8.

# INPUT DO USUÁRIO
temperatura_origem = int(input("Informe a temperatura em graus (apenas números): \n"))
tipo_origem = str(input("A temperatura informada está em 'C' (ºC-Celsius) ou 'F' (ºF-Fahrenheit)? \n"))

# CHAMADA DA FUNÇÃO
conversor_temperatura()

'''
#? RESPOSTA NO TERMINAL:
=========================================================================
# Teste: 40 F

Resposta do Exercício 03:

- CONVERSOR DE TEMPERATURA -

Informe a temperatura em graus (apenas números):
40
A temperatura informada está em 'C' (ºC-Celsius) ou 'F' (ºF-Fahrenheit)?
F

Você informou 40 graus ºF!

Essa temperatura convertida para Celsius é: 4.4 graus.


=========================================================================
# Teste: 15 C

Resposta do Exercício 03:

- CONVERSOR DE TEMPERATURA -

Informe a temperatura em graus (apenas números):
15
A temperatura informada está em 'C' (ºC-Celsius) ou 'F' (ºF-Fahrenheit)?
C

Você informou 15 graus ºC!

Essa temperatura convertida para Fahrenheit é: 59.0 graus.

=========================================================================

'''

print("\n=========================================================================")
# ================================================================================