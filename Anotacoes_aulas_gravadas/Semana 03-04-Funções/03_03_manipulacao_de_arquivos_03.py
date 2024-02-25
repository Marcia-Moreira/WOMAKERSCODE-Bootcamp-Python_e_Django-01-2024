print("=========================================================================")
# ====================================================================
# ! MANIPULAÇÃO DE ARQUIVOS -> OPEN - WRITING - READING (abertura/escrita/leitura)
# 3 formas de abertura (leitura binária não sei o que é)
# Salvar resultados e informações

# Processo de Abertura de um Arquivo tem 3 processos:
# ABERTURA - OPEN
# ESCRITA - WRITING
# LEITURA - READING

# MULTIPLICAÇÃO
def multiplicacao_funcao():
    multiplicacao = 10*3
    file = 'arquivo.txt' #crie efetivamente o arquivo na mesma pasta do código py
    #! Não esta gravando nada no arquivo!!!
    
    #? Escrevendo:
    #? OPEN para escrita "w"
    # Primeiro abrimos como Escrita e depois escrevemos e por fim fechamos para rodar o próximo
    arquivo_escrita = open(file, "w") # "w" de writing
    arquivo_escrita.write(f'O resultado da multiplicação é {multiplicacao}')
    arquivo_escrita.close()

    #? Lendo:
    #? OPEN para leitura "r"
    # Primeiro abrimos como Leitura e depois Lemos
    #*Abrir o arquivo para Leitura
    arquivo_leitura = open(file, "r") # "r" de reading.
    #*Leitura do arquivo
    leitura = arquivo_leitura.read()
    #*Print o que será escrito no Arquivo (Deve conferir abrindo o arquivo.txt, não confiar só no Terminal)
    print(leitura)
    #*Fechar o Arquivo
    arquivo_leitura.close()


multiplicacao_funcao() # Chamada da Função

#! DICA - o nome do arquivo não pode ter varios zeros na frente senão ele não funciona e não deixa gravar a mensagem dentro do txt.

#! DICA - Não consigo gravar dentro do txt pastas divulgada no github??? fiz varios testes e não funcionou, apenas numa pasta não divulgada

'''
RESULTADO NO CONSOLE:

mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/MM_Estudo-Testes
$ C:/Users/mmnol/AppData/Local/Programs/Python/Python312/python.exe c:/Projetos_MM/MM_Estudo-Testes/03_manipulacao_de_arquivos.py        
=========================================================================
O resultado da multiplicação é 20

mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/MM_Estudo-Testes

'''