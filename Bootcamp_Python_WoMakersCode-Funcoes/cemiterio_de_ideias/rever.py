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
ERRO:

Digite uma frase: o amor e lindo
A vogal a aparece 1 vezes na frase.
A vogal e aparece 1 vezes na frase.
A vogal i aparece 1 vezes na frase.
A vogal o aparece 3 vezes na frase.
A vogal u aparece 0 vezes na frase.
'''