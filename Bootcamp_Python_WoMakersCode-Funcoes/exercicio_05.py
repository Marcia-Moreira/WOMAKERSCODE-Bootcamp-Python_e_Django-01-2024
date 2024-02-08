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
# ! EXERCÍCIO 05:
'''
 5. Crie uma função chamada contar_vogais que recebe uma string
 como parâmetro. Implemente a lógica para contar o número de vogais
 na string e retorne o total de vogais. Solicite ao usuário para inserir uma
 frase e utilize a função para contar as vogais.
'''
# ? RESPOSTA:
print("\nResposta do Exercício 05: \n")

print(" - CONTADOR DE VOGAIS - ")
print('(Não utilize acentos ou cedilhas)\n')

#Precisamos Importar Biblioteca:
# from unidecode import unidecode (ERRO para instalar Unidecode)
#Ativar ambiente virtual Venv e Flask (ERRO persistênte)

def contar_vogais(frase):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A','E', 'I', 'O', 'U']
    vogais_na_frase = 0

    #Para remover acentos:
    # frase_para_contagem = unidecode(frase) #ERRO para instalar Unidecode

    #Para converter minúsculas:
    # frase_para_contagem = frase_para_contagem.lower()

    # for letra in frase_para_contagem:
            # if letra in vogais:
                # vogais_na_frase += 1

    for letra in frase:
        # função lower - para converter maiúsculas em minúsculas
        if letra.lower() in vogais:
            vogais_na_frase += 1

    print(f"\nA sua frase, tem {vogais_na_frase} vogais.\n")

    if vogais_na_frase == 0:
        print("Digite uma frase válida com vogais sem acentuação!\n")

    else:
        print("Perfeito! Aperte 'play/run' para reiniciar!\n")


# INPUT DO USUÁRIO:
frase_do_usuario = str(input("Escreva uma frase: "))

# CHAMADA DA FUNÇÃO:
contar_vogais(frase_do_usuario)

# letras maiusculas / Minusculas / acentos? 
# como contar 
# lista? array
# condicionais com incremento
# if e else +1 ou for
# como contar vogais na frase / array

'''
#? RESPOSTA NO TERMINAL:
=========================================================================

Resposta do Exercício 05: 

 - CONTADOR DE VOGAIS - 
(Não utilize acentos ou cedilhas)

Escreva uma frase: O amor e lindo demais

A sua frase, tem 9 vogais.

Perfeito! Aperte 'play/run' para reiniciar!

=========================================================================
'''
print("\n=========================================================================")
# ================================================================================