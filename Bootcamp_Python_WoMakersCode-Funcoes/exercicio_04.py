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