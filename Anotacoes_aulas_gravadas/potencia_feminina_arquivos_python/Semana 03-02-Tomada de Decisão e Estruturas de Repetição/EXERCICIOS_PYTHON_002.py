
# ====================================================================
# ! EXERCÍCIO 01:
'''
FaçaumProgramaquepeçadoisnúmeroseimprimaomaiordeles.
'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 02:
'''
FaçaumProgramaquepergunteemqueturnovocêestuda.PeçaparadigitarM-matutinoouV-VespertinoouN-Noturno.Imprimaamensagem"BomDia!","BoaTarde!"ou"BoaNoite!"ou"ValorInválido!",conformeocaso
'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 03:
'''
Façaumprogramaquepeçaumanota,entrezeroedez.Mostreumamensagemcasoovalorsejainválidoecontinuepedindoatéqueousuárioinformeumvalorválido
'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 04:
'''
Implementeumprogramaqueclassifiqueumalunocombaseemsuapontuaçãoemumexame.Oprogramadeverásolicitarumanotade0a10.Seapontuaçãoformaiorouiguala7,oalunoéaprovado;casocontrário,éreprovado
'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 05:
'''
Desenvolvaumprogramaquesoliciteaousuáriooscomprimentosdostrêsladosdeumtriânguloeclassifique-ocomoequilátero,isóscelesouescaleno.equilátero:todososladoscomomesmovalorisósceles:doisladoscomomesmovalorescaleno:todososladoscommedidasdistintas
'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 06:
'''
Crieumprogramaquesoliciteaousuárioumlogineumasenha.Oprogramadevepermitiroacessoapenasseousuáriofor"admin"easenhafor"admin123",casocontrárioimprimaumamensagemdeerro

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 07:
'''
Desenvolverumprogramaquesoliciteaidadedousuárioeidentifiqueseeleéumacriança,umadolescente,adultoouidoso
'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 08:
'''
CriarumprogramaemPythonquesolicitetrêsnúmerosaousuário,utilizeestruturascondicionaisparadeterminaromaiorentreeleseapresenteoresultado
'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 09: MINHA RESPONSABILIDADE
'''
O programa deve calcular e apresentar a quantidade de números pares e ímpares inseridos.O processo de leitura deve ser encerrado quando o usuário informar o valor zero.

Certifique-se de incluir validações para garantir que apenas números positivos sejam considerados na contagem e cálculos.
'''

# ? RESPOSTA POSSÍVEL:
print("Resposta do Exercício 09: ")

# Declaração de variaveis:
numero_par = 0
numero_impar = 0

# Operações:
# Enquanto Verdade
while True:
    # try-except - lidar com erros
    try:
        # Imput de Dados pelo usuário:
        numero_digitado = int(input('Digite um número positivo ("ou 0 para sair"): '))
        # Para parar se digitado o zero
        if numero_digitado == 0:
            break
        # Para verificar se o número é positivo ou negativo
        if numero_digitado > 0:
            # Se positivo, olhar se é par ou impar e somar +1
            if numero_digitado % 2 == 0:
                numero_par += 1
            else:
                numero_impar += 1
        else:
            # Caso usuário digite numero negativo
            print("Insira apenas números positivos!")
    # Caso o usuário já insira numero negativo imediatamente 
    except ValueError:
        print("Insira apenas números positivos!")

# Imprimir no Terminal:
print(f"Total de números pares inseridos: {numero_par}.")
print(f"Total de números impares inseridos: {numero_impar}.")
        
'''
# RESPOSTA NO TERMINAL:

TESTE 01:
Resposta do Exercício 09: 
Digite um número positivo ("ou 0 para sair"): 5
Digite um número positivo ("ou 0 para sair"): 6
Digite um número positivo ("ou 0 para sair"): 7
Digite um número positivo ("ou 0 para sair"): 4
Digite um número positivo ("ou 0 para sair"): 6
Digite um número positivo ("ou 0 para sair"): 0
Total de números pares inseridos: 3.
Total de números impares inseridos: 2.

# TESTE 02:
Resposta do Exercício 09: 
Digite um número positivo ("ou 0 para sair"): -5
Insira apenas números positivos!
Digite um número positivo ("ou 0 para sair"): 6
Digite um número positivo ("ou 0 para sair"): -3
Insira apenas números positivos!
Digite um número positivo ("ou 0 para sair"): 5
Digite um número positivo ("ou 0 para sair"): 6
Digite um número positivo ("ou 0 para sair"): 3
Digite um número positivo ("ou 0 para sair"): 0
Total de números pares inseridos: 2.
Total de números impares inseridos: 2.

'''

# informe um número Diferente de Zero 
# Calcular quantidade Par e Imp
# IF for Positivo = continua ELSE Negativo = Cancela
# Enquanto não for zero WILE

# ====================================================================
# ! EXERCÍCIO 10: MINHA RESPONSABILIDADE
'''
10.Faça um programa que lê três números inteiros e os mostra em ordem crescente.
'''

# ? RESPOSTA:
print("Resposta do Exercício 10: ")

# Imput de Dados pelo usuário:
primeiro_num = int(input("Digite um número: "))
segundo_num = int(input("Digite mais um número: "))
terceiro_num = int(input("Agora, digite o último número: "))

# Para criar uma lista com os 3 números:
todos_numeros = [primeiro_num, segundo_num, terceiro_num]

#  Ordenar a Lista (ordem crescente)
ordem_crescente = sorted(todos_numeros)

# Imprimir no Terminal:
print(f"Os números escolhidos, em ordem crescente, são {ordem_crescente}.")

'''
# RESPOSTA NO TERMINAL:

TESTE 01:
Resposta do Exercício 10: 
Digite um número: 4  
Digite mais um número: 2
Agora, digite o último número: 7
Os números escolhidos, em ordem crescente, são [2, 4, 7].

TESTE 02:
Resposta do Exercício 10: 
Digite um número: 54
Digite mais um número: 32
Agora, digite o último número: 6
Os números escolhidos, em ordem crescente, são [6, 32, 54].

TESTE 03:
Resposta do Exercício 10: 
Digite um número: -14
Digite mais um número: 4
Agora, digite o último número: 0
Os números escolhidos, em ordem crescente, são [-14, 0, 4].

'''
# fim
# ====================================================================


# ====================================================================
# ! EXERCÍCIO 00:
'''

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''
9.Oprogramadevecalculareapresentaraquantidadedenúmerospareseímparesinseridos.Oprocessodeleituradeveserencerradoquandoousuárioinformarovalorzero.Certifique-sedeincluirvalidaçõesparagarantirqueapenasnúmerospositivossejamconsideradosnacontagemecálculos.10.Façaumprogramaquelêtrêsnúmerosinteiroseosmostraemordemcrescente.

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''
9.Oprogramadevecalculareapresentaraquantidadedenúmerospareseímparesinseridos.Oprocessodeleituradeveserencerradoquandoousuárioinformarovalorzero.Certifique-sedeincluirvalidaçõesparagarantirqueapenasnúmerospositivossejamconsideradosnacontagemecálculos.10.Façaumprogramaquelêtrêsnúmerosinteiroseosmostraemordemcrescente.

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL:

# ====================================================================
# ! EXERCÍCIO 00:
'''
9.Oprogramadevecalculareapresentaraquantidadedenúmerospareseímparesinseridos.Oprocessodeleituradeveserencerradoquandoousuárioinformarovalorzero.Certifique-sedeincluirvalidaçõesparagarantirqueapenasnúmerospositivossejamconsideradosnacontagemecálculos.10.Façaumprogramaquelêtrêsnúmerosinteiroseosmostraemordemcrescente.

'''

# ? RESPOSTA:
# print("Resposta do Exercício 00: ")
# Imput de Dados pelo usuário:
# Operações:
# Imprimir no Terminal:
# RESPOSTA NO TERMINAL: