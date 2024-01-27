
# ====================================================================
# ! OPERADORES RESTO (%), INCREMENTO (+=) E DECREMENTO (-=)

# Resto % => Resto da Divisão
# Incremento += => Soma algum valor ao que já existe
# Decremento -= => Diminui algum valor ao que já existe

# ====================================================================
# ! RESTO
# Resto de uma Divisão

'''
10/2=5
10/3=3 -> %1 (Resta 1)
'''
print("Resto da Divisão: % ")
valor_1 = 10
valor_2 = 3
resta = valor_1 % valor_2
print(resta)

# ====================================================================
# ! INCREMENTO (soma)
# Veja a diferença: # temos uma valor e precisamos acrescentar algo)

print("Soma Normal: + ")
valor_soma = 5
valor_soma + 1
print(valor_soma)

print("Soma Incremento: += ")
valor_incremento = 5
valor_incremento += 1
print(valor_incremento)


# ====================================================================
# ! DECREMENTO (subtração)
# Veja a diferença: # temos uma valor e precisamos diminuir algo)

print("Subtração Normal: - ")
valor_subtração = 5
valor_subtração - 1
print(valor_subtração)

print("Subtração Incremento: -= ")
valor_decremento = 5
valor_decremento -= 1
print(valor_decremento)


# ====================================================================
# ! IMPRESSO NO TERMINAL:

'''
Resto da Divisão: % 
1
Soma Normal: +
5
Soma Incremento: +=
6
Subtração Normal: -
5
Subtração Incremento: -=
4
'''


