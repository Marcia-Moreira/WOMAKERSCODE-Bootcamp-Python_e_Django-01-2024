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

def contar_vogais():
    vogais_minusculas = ['a', 'e', 'i', 'o', 'u' ]
    vogais_maiusculas = ['A', 'E', 'I', 'O', 'U' ]
    print("Na sua frase, tem x vogais.")
    frase_usuario = []
    vogais_na_frase = 0

    while True:
        try:
            if frase_usuario >= 0:
                break

            if frase_usuario == vogais_maiusculas or vogais_minusculas:
                vogais_na_frase += 1

            else:
                print(f"Na sua frase tem {vogais_na_frase} vogais.")


        except ValueError:
            print("Por favor, insira uma frase válida sem acentuação!")
            print("Não existem vogais na sua frase!")




# INPUT DO USUÁRIO:
frase_usuario = str(input("Escreva uma frase: "))
#Na sua frase, temos x vogais

# CHAMADA DA FUNÇÃO:
contar_vogais()


# letras maiusculas / Minusculas / acentos? 
# como contar 
# lista? array
# condicionais com incremento
# if e else +1
# como contar vogais na frase / array

'''
# CRIAR UMA LISTA EM PYTHON:
frutas = ['Maçã', 'Banana', 'Uva'] #Declaração de uma lista
for fruta in frutas:  #para cada
    print(fruta)
# Leia-se: Para cada fruta em Lista Frutas, imprima fruta.
'''


# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:
'''
#? RESPOSTA NO TERMINAL:

'''