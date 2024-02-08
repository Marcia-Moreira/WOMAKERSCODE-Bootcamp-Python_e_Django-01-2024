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

#Precisamos Importar Biblioteca:
# from unidecode import unidecode

#Ativar ambiente virtual Venv e Flask

def contar_vogais(frase):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A','E', 'I', 'O', 'U']
    vogais_na_frase = 0

    #Para remover acentos:
    # frase_para_contagem = unidecode(frase)  #!ERRO instalação Biblioteca!!!

    #Para converter minúsculas:
    frase_para_contagem = frase_para_contagem.lower()

    for letra in frase_para_contagem:
            if letra in vogais:
                vogais_na_frase += 1

    print(f"A sua frase, tem {vogais_na_frase} vogais.\n")

    if vogais_na_frase == 0:
        print("Digite uma frase válida com vogais!\n")

    else:
        print("Perfeito! Aperte 'play/run' para continuar!\n")


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

'''

print("\n=========================================================================")