#
#! ESte é o arquivo de Conexão que funciona pois está com acminho mais curto! Só funciona junto com o arquivo de .db

#!NÃO FUNCIONA EM CAMINHOS LONGOS DE PASTA - TIVE QUE TIRAR NA PASTA DA MATERIA DB E POR MAIS PRA FORA OS DOIS ARQUIVOS: conexao_py_db_banco_de_dados.py E db_banco_de_dados.db

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

#? Para renomear Coluna:
#cursor.execute('ALTER TABLE tb_usuario RENAME COLUMN telefoni TO telefone')

#? Para excluir uma tabela inteira com todos usuarios: DROP TABLE (para excluir apenas 1 usuario=delete from)
#cursor.execute('DROP TABLE tb_mercadoria')

#? Para inserir dados na tabela:
#cursor.execute('INSERT INTO tb_usuario(id, nome, endereco, email, telefone) VALUES(1, "Isadora Moreira", "França", "isa@gmail.com", 123456 )')

#cursor.execute('INSERT INTO tb_usuario(id, nome, endereco, email, telefone) VALUES(2, "Maria Silva", "Caxias", "maria@gmail.com", 12345 )')

#cursor.execute('INSERT INTO tb_usuario(id, nome, endereco, email, telefone) VALUES(3, "Alexandre Guaraldo", "Las Vegas", "ale@gmail.com", 1234567 )')

#cursor.execute('INSERT INTO tb_usuario(id, nome, endereco, email, telefone) VALUES(4, "Marcia Moreira", "Miami", "mm@gmail.com", 12345678 )')

#? Para excluir apenas um dado específico dentro de uma tabela:
# delete da tabela x quando id for...
#cursor.execute('DELETE FROM tb_usuario where id=2')

"""
#? Para Visualizar as informações - select todos :
# selecione * tudo da tabela x , mas temos que associar ao python com a variável 'dados'.
dados = cursor.execute('SELECT * FROM tb_usuario')
for tb_usuario in dados:
    print(tb_usuario) 

"""
'''
(1, 'Isadora Moreira', 'França', 'isa@gmail.com', 123456)
(3, 'Alexandre Guaraldo', 'Las Vegas', 'ale@gmail.com', 1234567)
(4, 'Marcia Moreira', 'Miami', 'mm@gmail.com', 12345678)
(2, 'Maria Silva', 'Caxias', 'maria@gmail.com', 12345)
'''


'''
#? Para Visualizar as informações - select coluna x:
# selecione coluna nome da tabela x , mas temos que associar ao python com a variável 'dados'.
dados = cursor.execute('SELECT nome FROM tb_usuario')
for tb_usuario in dados:
    print(tb_usuario) 
'''
'''
('Isadora Moreira',)
('Alexandre Guaraldo',)
('Marcia Moreira',)
('Maria Silva',)
'''

'''
#? Para Visualizar as informações - select coluna x e y:
# selecione coluna nome da tabela x , mas temos que associar ao python com a variável 'dados'.
dados = cursor.execute('SELECT nome,telefone FROM tb_usuario')
for tb_usuario in dados:
    print(tb_usuario)

'''
'''
('Isadora Moreira', 123456)
('Alexandre Guaraldo', 1234567)
('Marcia Moreira', 12345678)
('Maria Silva', 12345)
'''

#? Para Visualizar as informações - select coluna x e y com condição de filtro:
# selecione coluna nome da tabela x , mas temos que associar ao python com a variável 'dados'.
dados = cursor.execute('SELECT nome,telefone FROM tb_usuario WHERE id>3')
for tb_usuario in dados:
    print(tb_usuario) 

'''
('Marcia Moreira', 12345678)
'''

#? Para Atualizar informações - UPDate:
cursor.execute('')

# ==========================================================
#? 04 - COMANDOS PARA ENVIO E ENCERRAMENTO DOS COMANDOS DB:
# para envio das informações nesse comando:
conexao.commit()
# Para interromper a execução e disponibilizar sistema logo que concluído:
conexao.close()

# ==========================================================
#? 

'''
Anotações:


mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024 (main)
$ c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/womakercode/Scripts/python.exe c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/conexao_py_db_banco_de_dados.py

mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024 (main)
$ c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/womakercode/Scripts/python.exe c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/conexao_py_db_banco_de_dados.py

mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024 (main)
$ c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/womakercode/Scripts/python.exe c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/conexao_py_db_banco_de_dados.py

mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024 (main)
$ c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/womakercode/Scripts/python.exe c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/conexao_py_db_banco_de_dados.py

mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024 (main)
$ c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/womakercode/Scripts/python.exe c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/conexao_py_db_banco_de_dados.py

mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024 (main)
$ c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/womakercode/Scripts/python.exe c:/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024/conexao_py_db_banco_de_dados.py

mmnol@Galaxy-Book-MM-13062023 MINGW64 /c/Projetos_MM/WOMAKERSCODE-Bootcamp-Python_e_Django-01-2024 (main)
$


'''