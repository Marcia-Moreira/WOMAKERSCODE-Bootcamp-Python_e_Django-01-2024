#NÃO FUNCIONA EM CAMINHOS LONGOS DE PASTA - TIVE QUE TIRAR NA PASTA DA MATERIA DB E POR MAIS PRA FORA OS DOIS ARQUIVOS: conexao_py_db_banco_de_dados.py E db_banco_de_dados.db

# ==========================================================
#? 01 - COMANDOS IMPORTAÇÃO DE BIBLIOTECA SQLITE3:
# imprtar Biblioteca sqlite3 que vem na instalação do Python:
import sqlite3

# ==========================================================
#? 02 - COMANDOS DE CONEXÃO .PY X .DB:
# conectar o arquivo .py com o arquivo .db:
conexao = sqlite3.connect('db_banco_de_dados.db')
# passar a conexão para uma nova variável a ser usada:
cursor = conexao.cursor()

# ==========================================================
#? 03 - COMANDOS DE EXECUÇÃO/CRIAÇÃO TABELAS E DADOS DO BANCO:
# Nesse espaço, devem ser escritos o COMANDO de SQL a serem executados no Banco de Dados:
# cursor.execute('')  #modelo

#? Para criar uma tabela com colunas vazias:
#cursor.execute('CREATE TABLE tb_usuarios(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(50));')

#teste para ser apagada com drop:
#cursor.execute('CREATE TABLE tb_mercadoria(id INT, nome VARCHAR(100), endereco VARCHAR(100), email VARCHAR(50));')

#? Para renomear uma tabela:
#cursor.execute('ALTER TABLE tb_usuarios RENAME TO tb_usuario')

#? Para incluir uma Coluna:
#cursor.execute('ALTER TABLE tb_usuario ADD COLUMN telefoni INT')

# Para renomear Coluna:
#cursor.execute('ALTER TABLE tb_usuario RENAME COLUMN telefoni TO telefone')

#? Para excluir uma tabela inteira:
#cursor.execute('DROP TABLE tb_mercadoria')


# ==========================================================
#? 01 - COMANDOS PARA ENVIO E ENCERRAMENTO DOS COMANDOS DB:
# para envio das informações nesse comando:
conexao.commit()
# Para interromper a execução e disponibilizar sistema logo que concluído:
conexao.close()

# ==========================================================
#? 

'''
Anotações:




'''