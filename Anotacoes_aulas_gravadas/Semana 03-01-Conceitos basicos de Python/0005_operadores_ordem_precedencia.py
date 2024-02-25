
#! PRECEDÊNCIA E OPERADORES RELACIONAIS 



# ====================================================================
# ! ORDEM DE PRECEDÊNCIA: (Parentese/Multiplicação e Divisão/Soma e Subtração)

# -> a MULTIPLICAÇÂO e a DIVISÂO, são realizadas primeiro!!!

# -> depois é que fazemos a soma e a subtração

# -> Tem prioridade onde colocamos parênteses ( ) 
'''
calculo = 2 + 5 * 5  (logo: 5 * 5 + 2 = 27)

calculo_prioridade = (2 + 5) * 5 (logo: 2 + 5 * 5 = 35)
'''
print("calculo = 2 + 5 * 5  (logo: 5 * 5 + 2 = 27)")
calculo = 2+5*5
print(calculo)

print("calculo_prioridade = (2 + 5) * 5 (logo: 2 + 5 * 5 = 35)")
calculo_prioridade = (2 + 5) * 5
print(calculo_prioridade)

#? rever
print("calculo_com_parenteses_1 = (2+5)*5+4*3 (logo: 2+5, 4*3, *5)")
calculo_com_parenteses_1 = (2+5)*5+4*3
print(calculo_com_parenteses_1)

#? rever
print("calculo_com_parenteses_2 = (2+5)*((5+4)*3) (logo: 2+5, 5+4, 5+4*3, 2+5*5+4*3)")
calculo_com_parenteses_2 = (2+5)*((5+4)*3)
print(calculo_com_parenteses_2)


# ====================================================================
# ! IMPRESSO NO TERMINAL: 

'''
calculo = 2 + 5 * 5  (logo: 5 * 5 + 2 = 27)
27
calculo_prioridade = (2 + 5) * 5 (logo: 2 + 5 * 5 = 35)
35
calculo_com_parenteses_1 = (2+5)*5+4*3 (logo: 2+5, 4*3, *5)
47
calculo_com_parenteses_2 = (2+5)*((5+4)*3) (logo: 2+5, 5+4, 5+4*3, 2+5*5+4*3)
189

'''


# ====================================================================
# ! OPERADORES RELACIONAIS:

'''
== : igual
> : maior
>= : maior ou igual
< : menor 
<= : menor ou igual 
!= : diferente

'''

# Para abrir o Interpretador do Python no Terminal (direto), digite => python

# ! Vamos fazer testes direto no interpretador python:

'''
mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/WOMAKERSCODE-Python_e_Django-01-2024
$ python
Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> 5==5
True
>>> 5>5
False
>>> 5>=5
True
>>> 5<5
False
>>> 5<=5
True
>>>
KeyboardInterrupt
>>>
>>> 5!=5
False
>>> 5!=2
True
>>>

 '''


