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
# ! EXERCÍCIO 02:
'''
 2. Reverso do número. Faça uma função que retorne o reverso de um
 número inteiro informado. Por exemplo: 127-> 721.
'''
# ? RESPOSTA:
print("\nResposta do Exercício 02: \n")

print(" - NÚMERO REVERSO - \n")

def invertido():
    digite_numero = int(input("Digite qualquer número inteiro, a partir do número 100(cem): "))

    # preciso converter o int em string para fatiar e inverter:
    converte_numero_string = str(digite_numero)[::-1]

    inverte_numero = int(converte_numero_string)

    print("\nO número reverso é: ", inverte_numero)

    print("\nAperte 'play/run' para reiniciar!\n")

invertido()

'''
#? RESPOSTA NO TERMINAL:
=========================================================================
# Teste: 102

Resposta do Exercício 02:

 - NÚMERO REVERSO -

Digite qualquer número inteiro, a partir do número 100(cem): 102

O número reverso é:  201

Aperte 'play/run' para reiniciar!

=========================================================================
'''

print("\n=========================================================================")
# ================================================================================