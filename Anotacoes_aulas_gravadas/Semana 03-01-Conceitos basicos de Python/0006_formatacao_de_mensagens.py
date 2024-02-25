# ====================================================================
# ! FORMATAÇÃO DE MENSAGENS:

# FORMAT -> f
# CHAVES -> a variável precisa estar dentro de CHAVES
# Podemos formatar mais de uma variável dentro de textos.

# ====================================================================
# ! FORMATANDO TEXTOS E VARIÁVEIS:

print("SOMA")
soma_numero1 = int(input("Digite o numero 01: "))
soma_numero2 = int(input("Digite o numero 02: "))
soma = soma_numero1 + soma_numero2
print(soma)
print(f'A soma dos números digitados é {soma}.')
print(f"A soma do primeiro número que é o {soma_numero1} com o segundo número que é o {soma_numero2}, resulta em {soma}.")


# ====================================================================
# ! IMPRESSO NO TERMINAL:

'''
SOMA
Digite o numero 01: 3
Digite o numero 02: 6
9
A soma dos números digitados é 9.
A soma do primeiro número que é o 3 com o segundo número que é o 6, resulta em 9.

'''

# ====================================================================
# ! STR.FORMAT( ): 
'''
s t r . f o r m a t ( )
'''

# Por padrão, sairá no Console apenas uma casa decimal após a vírgula/ponto
valor_1 = 45.00
print(valor_1)
# R: 45.0

# ==========================

# Força sair no Console, duas casas decimais após a virgula/ponto
valor_2 = 45.00
print(f'{valor_2:.2f}')
# R: 45.00


# ==========================

# Força sair no Console, duas casas decimais após a virgula/ponto mesmo havendo vários números após
valor_2 = 45.34566556
print(f'{valor_2:.2f}')
# R: 45.35


# ==========================
# Podemos fazer as marcações onde ficarão as variáveis e só definir de fato o conteúdo no final da frase

print('Olá {}, como vai?' .format('Isadora'))

# É obedecida a ordem de preenchimento nas marcações
print('Olá {}, como vai? Você tem {} anos.' .format('Isadora', 26))


