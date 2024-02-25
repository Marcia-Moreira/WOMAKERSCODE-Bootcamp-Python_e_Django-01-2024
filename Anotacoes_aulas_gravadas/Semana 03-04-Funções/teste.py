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
from unidecode import unidecode

#Ativar ambiente virtual Venv e Flask

def contar_vogais(frase):
    vogais = ['a', 'e', 'i', 'o', 'u', 'A','E', 'I', 'O', 'U']
    vogais_na_frase = 0

    #Para remover acentos:
    frase_para_contagem = unidecode(frase)

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
#Na sua frase, temos x vogais

# CHAMADA DA FUNÇÃO:
contar_vogais(frase_do_usuario)


'''

teste= prgrtqp mn tdfs

def contar_vogais(frase):
    # Inicializa um contador para cada vogal
    contador = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

    # Converte a frase para minúsculas para garantir a contagem correta das vogais
    frase = frase.lower()

    # Percorre cada caractere da frase
    for letra in frase:
        # Verifica se o caractere é uma vogal
        if letra in contador:
            # Incrementa o contador da vogal correspondente
            contador[letra] += 1

    # Imprime o resultado
    for vogal, contagem in contador.items():
        print(f'A vogal {vogal} aparece {contagem} vezes na frase.')

# Solicita ao usuário para inserir a frase
frase_usuario = input('Digite uma frase: ')

# Chama a função para contar as vogais na frase fornecida pelo usuário
contar_vogais(frase_usuario)
'''


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