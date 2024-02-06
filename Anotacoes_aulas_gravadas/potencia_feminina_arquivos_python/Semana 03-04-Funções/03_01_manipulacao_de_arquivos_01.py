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
    file = 'arquivo.txt' #crie efetivamente o arquivo na mesma pasta do código py
    
    #? FASE ABRIR ARQUIVO (abrir, criar para salvar)
    #? OPEN somente para Leitura "r"
    arquivo_leitura = open(file, "r") #Pode ser o nome do arquivo ou nome da variavel, "r" de reading.
    
    #? OPEN para escrita "w"
    arquivo_escrita = open(file, "w")
        #? FASE ESCREVER ARQUIVO (escrever dentro de arquivos)
    arquivo_escrita.write("Texto a ser escrito")

    #? OPEN de arquivos binários "wb"
    arquivo_binario = open(file, "wb")

    # print(f'O resultado da multiplicação é {multiplicacao}')
multiplicacao_funcao()

'''

ACIMA NÃO FUNCIONA PARA EXECUÇÃO - DEIXEI COMO MODELO

file = "Caminho/Para/Seu/Diretorio/arquivo.txt"
arquivo_leitura = open(file, "r")


mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024 (main)
$ C:/Users/mmnol/AppData/Local/Programs/Python/Python312/python.exe "c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/Anotacoes_aulas_gravadas/potencia_feminina_arquivos_python/Semana 03-04-Funções/0002_manipulacao_de_arquivos.py"
=========================================================================
Traceback (most recent call last):
  File "c:\Projetos_MM\WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024\Anotacoes_aulas_gravadas\potencia_feminina_arquivos_python\Semana 03-04-Funções\0002_manipulacao_de_arquivos.py", line 30, in <module>
    multiplicacao_funcao()
  File "c:\Projetos_MM\WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024\Anotacoes_aulas_gravadas\potencia_feminina_arquivos_python\Semana 03-04-Funções\0002_manipulacao_de_arquivos.py", line 19, in multiplicacao_funcao
    arquivo_leitura = open(file, "r") #Pode ser o nome do arquivo ou nome da variavel, "r" de reading.
                      ^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'arquivo.txt'

mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024 (main)
'''