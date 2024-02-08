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
# ! EXERCÍCIO 04:
'''
 4. Crie um programa que leia quanto dinheiro uma pessoa tem na
 carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
 Considere a tabela de conversão abaixo:
 Dólar Americano: R$ 4,91
 Peso Argentino: R$ 0,02
 Dólar Australiano: R$ 3,18
 Dólar Canadense: R$ 3,64
 Franco Suiço: R$ 0,42
 Euro: R$ 5,36
 Libra Esterlina: R$ 6,21
'''
# ? RESPOSTA:
print("\nResposta do Exercício 04: \n")

print(" - CONVERSOR DE MOEDAS - \n")

def conversor_moedas():
    dolar_americano = quanto_tem_na_carteira / 4.91
    dolar_australiano = quanto_tem_na_carteira / 3.18
    dolar_canadense = quanto_tem_na_carteira / 3.64
    peso_argentino = quanto_tem_na_carteira / 0.02
    franco_suico = quanto_tem_na_carteira / 0.42
    euro = quanto_tem_na_carteira / 5.36
    libra_esterlina = quanto_tem_na_carteira / 6.21
    print("\nHoje, você pode comprar:\n")
    print(f"- {dolar_americano:.0f} Dólar(es) Americano.")
    print(f"- {dolar_australiano:.0f} Dólar(es) Australiano.")
    print(f"- {dolar_canadense:.0f} Dólar(es) Canadense.")
    print(f"- {peso_argentino:.0f} Peso(s) Argentino.")
    print(f"- {franco_suico:.0f} Franco(s) Suiço.")
    print(f"- {euro:.0f} Euro(s).")
    print(f"- {libra_esterlina:.0f} Libra(s) Esterlina.")
    
# INPUT DO USUÁRIO:
quanto_tem_na_carteira = float(input("Quanto você tem na carteira, em Real? R$ "))

# CHAMADA DA FUNÇÃO:
conversor_moedas()
'''
#? RESPOSTA NO TERMINAL:
=========================================================================

Resposta do Exercício 04:

- CONVERSOR DE MOEDAS - 

Quanto você tem na carteira, em Real? R$ 1000.00

Hoje, você pode comprar:

- 204 Dólar(es) Americano.
- 314 Dólar(es) Australiano.
- 275 Dólar(es) Canadense.
- 50000 Peso(s) Argentino.
- 2381 Franco(s) Suiço.
- 187 Euro(s).
- 161 Libra(s) Esterlina.

=========================================================================

Resposta do Exercício 04: 

- CONVERSOR DE MOEDAS - 

Quanto você tem na carteira, em Real? R$ 2.00

Hoje, você pode comprar:

- 0 Dólar(es) Americano.
- 1 Dólar(es) Australiano.
- 1 Dólar(es) Canadense.
- 100 Peso(s) Argentino.
- 5 Franco(s) Suiço.
- 0 Euro(s).
- 0 Libra(s) Esterlina.

=========================================================================
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
# ! EXERCÍCIO 06:
'''
 6. Vamos construir um jogo de forca. O programa escolherá
 aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
 secreta será representada por espaços em branco, um para cada letra
 da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
 tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
 na palavra secreta, ela será revelada nas posições correspondentes. Se
 a letra não estiver na palavra, uma mensagem de erro deverá ser
 informada. Após um número máximo de erros, o jogador perde. O jogo
 continua até que o jogador adivinhe a palavra ou exceda o número
 máximo de tentativas.
 Dica: Você precisará importar uma biblioteca para resolver esse
 exercício.
'''
#? RESPOSTA:
print("\nResposta do Exercício 06: \n")

# Biblioteca Importada:
import random

# Lista de palavras secretas predefinidas
palavras_secretas = ['python', 'programacao', 'computador', 'desenvolvimento', 'aleatoria', 'inteligencia']
#! Depois pensar em forma do usuário colocar as palavras antes para outra pessoa jogar! 

def escolher_palavra_secreta():
    #biblioteca random (para sortear)
    return random.choice(palavras_secretas)

def jogo_forca():
    palavra_secreta = escolher_palavra_secreta()
    # função len - retorna o comprimento:
    letras_reveladas = ['_'] * len(palavra_secreta)
    # contador de tentativas
    tentativas_restantes = 6

    print("Bem-vindo(a) ao \U0001F968 JOGO DE FORCA \U0001F968 !\n")
    # função join - concatenação e separadores
    print(" ".join(letras_reveladas))

    # para imprimir o total de letras da palavra sorteada
    total_letras = len(letras_reveladas)
    print(f"A palavra tem {total_letras} letras.")

    while tentativas_restantes > 0:
        letra = input("\nDigite uma letra: ")

        # Para converter maiúsculas digitadas em minúsculas:
        letra = letra.lower()

        if letra in palavra_secreta:
            # função enumerate - retorna um objeto enumerado
            for i_contador, cada_letra in enumerate(palavra_secreta):
                if cada_letra == letra:
                    letras_reveladas[i_contador] = letra
            # função join - concatenação e separadores
            print(" ".join(letras_reveladas))
            # se acabar os separadores, print ganhou.
            if '_' not in letras_reveladas:
                print("\n \U0001F389 Parabéns! Você ganhou! \U0001F389 \n")
                break
        else:
            # decremento das 6 tentativas
            tentativas_restantes -= 1
            print(f"\nLetra não encontrada. Tentativas restantes: {tentativas_restantes}.")
    
    if tentativas_restantes == 0:
        # se a tentativa for igual a zero, print:
        print(f"\n Que pena! Você excedeu o número máximo de 6 erros. A palavra secreta era: {palavra_secreta}.\n")

# CHAMADA DA FUNÇÃO:
jogo_forca()

'''
#? RESPOSTA NO TERMINAL:
=========================================================================

Resposta do Exercício 06: 

Bem-vindo(a) ao 🥨 JOGO DE FORCA 🥨 !

_ _ _ _ _ _ _ _ _ _ _ _ _ _ _
(A palavra tem 15 letras)

Digite uma letra: a

Letra não encontrada. Tentativas restantes: 5.

Digite uma letra: e
_ e _ e _ _ _ _ _ _ _ e _ _ _

Digite uma letra: I
_ e _ e _ _ _ _ _ i _ e _ _ _

Digite uma letra: T
_ e _ e _ _ _ _ _ i _ e _ t _

Digite uma letra: o
_ e _ e _ _ o _ _ i _ e _ t o

Digite uma letra: m
_ e _ e _ _ o _ _ i m e _ t o

Digite uma letra: p

Letra não encontrada. Tentativas restantes: 4.

Digite uma letra: n
_ e _ e n _ o _ _ i m e n t o

Digite uma letra: l
_ e _ e n _ o l _ i m e n t o

Digite uma letra: d
d e _ e n _ o l _ i m e n t o

Digite uma letra: s
d e s e n _ o l _ i m e n t o

Digite uma letra: v
d e s e n v o l v i m e n t o

 🎉 Parabéns! Você ganhou! 🎉

======================================================================FIM
'''
print("\n======================================================================FIM")
# =============================================================================FIM

'''
PDF DA ATIVIDADE COMPLETA:

Bootcamp Back-End Python e
 Django
 Exercícios Extras de Python

 Exercícios Funções e Extras de Python
 1. Faça um programa, com uma função que necessite de três
 argumentos, e que forneça a soma desses três argumentos.

 2. Reverso do número. Faça uma função que retorne o reverso de um
 número inteiro informado. Por exemplo: 127-> 721.

 3. Escreva um script que pergunta ao usuário se ele deseja converter
 uma temperatura de grau Celsius para Fahrenheit ou vice-versa. Para
 cada opção, crie uma função.
 Plus: Crie uma terceira, que é um menu para o usuário escolher a opção
 desejada, onde esse menu chama a função de conversão correta.

 4. Crie um programa que leia quanto dinheiro uma pessoa tem na
 carteira, e calcule quanto poderia comprar de cada moeda estrangeira.
 Considere a tabela de conversão abaixo:
 Dólar Americano: R$ 4,91
 Peso Argentino: R$ 0,02
 Dólar Australiano: R$ 3,18
 Dólar Canadense: R$ 3,64
 Franco Suiço: R$ 0,42
 Euro: R$ 5,36
 Libra esterlina: R$ 6,21

 5. Crie uma função chamada contar_vogais que recebe uma string
 como parâmetro. Implemente a lógica para contar o número de vogais
 na string e retorne o total de vogais. Solicite ao usuário para inserir uma
 frase e utilize a função para contar as vogais.

 6. Vamos construir um jogo de forca. O programa escolherá
 aleatoriamente uma palavra secreta de uma lista predefinida. A palavra
 secreta será representada por espaços em branco, um para cada letra
 da palavra. O jogador terá um número limitado de 6 tentativas. Em cada
 tentativa, o jogador pode fornecer uma letra. Se a letra estiver presente
 na palavra secreta, ela será revelada nas posições correspondentes. Se
 a letra não estiver na palavra, uma mensagem de erro deverá ser
 informada. Após um número máximo de erros, o jogador perde. O jogo
 continua até que o jogador adivinhe a palavra ou exceda o número
 máximo de tentativas.
 Dica: Você precisará importar uma biblioteca para resolver esse
 exercício.

 '''
print("\n=========================================================================")
# ================================================================================