# Aula Python WoMakersCode 
# ====================================================================
# ! FUNÇÕES -> DEF 

'''
SINTAXE:

São grupos de instruções relacionadas, que executam uma tarefa

Declaração da Função:

def nome_da_funcao():

Chamada da função: 

mostrar_mensagem()

*variaveis não podem ter o mesmo nome da função

'''
print("=========================================================================")
# 1ª FUNÇÃO:
# Declaração da Nossa Função:
def soma_funcao(): #definição da função soma
    calculo = 10+2
    print(f'O resultado da soma é: {calculo}')
# Chamada da função:
soma_funcao() #Invocação da Função
# Resposta Console: 12

# 2ª FUNÇÃO:
def subtracao_funcao():
    subtracao = 10-2
    print(f'O resultado da subtração é {subtracao}')
    # multiplicacao_funcao() 
    soma_funcao() #! Uma função pode ser chamada dentro da outra desde que já tenha sido DECLARADA e exista qualquer outra chamada abaixo no lugar padrão!!
# Chamada da função:
soma_funcao()  #vai chamar o resultado da soma e ignorar da subtração
subtracao_funcao()
# Resposta Console: 12
# Resposta Console: 12
# Resposta Console: 08
# Resposta Console: 12

# 3ª FUNÇÃO:
def multiplicacao_funcao():
    multiplicacao = 10*2
    print(f'O resultado da multiplicação é {multiplicacao}')
# Chamada da função:
multiplicacao_funcao()
# Resposta Console: 20

#Uma função pode ser chamada dentro da outra!!



