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
    multiplicacao = 10*2
    file = 'arquivo.txt' #crie efetivamente o arquivo na mesma página do código py
    
    #? OPEN para escrita "w"
    arquivo_escrito = open(file, "w")
        #? FASE ESCREVER ARQUIVO (escrever dentro de arquivos)
    arquivo_escrito.write("Texto a ser escrito")

    # print(f'O resultado da multiplicação é {multiplicacao}')
multiplicacao_funcao()


'''
RESPOSTA NO CONSOLE:

mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024 (main)
$ C:/Users/mmnol/AppData/Local/Programs/Python/Python312/python.exe "c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/Anotacoes_aulas_gravadas/potencia_feminina_arquivos_python/Semana 03-04-Funções/teste.py"
=========================================================================
'''