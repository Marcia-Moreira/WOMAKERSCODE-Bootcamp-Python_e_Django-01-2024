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