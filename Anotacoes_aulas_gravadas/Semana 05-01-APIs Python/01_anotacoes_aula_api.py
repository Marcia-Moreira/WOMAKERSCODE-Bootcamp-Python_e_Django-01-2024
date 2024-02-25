# Anotações Aulas API:

# Vícios de Linguagem = ãããh , neh,  e basicamente neh, ali neh, digamos assim neh, 

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Introdução aos protocolos web (http e https)

'''
Protocolo HTTP -> cliente solicita uma informação, ele entrega a informação. Ex: eu num restaurante, o garçon, que leva meu pedido até a cozinha.

Comunicação web:
1-Cliente
2-Internet
3-Servidor 

HTTP -> HyperText Transfer Protocol (projetado para enviar conteúdo)

Proxy -> É um representante que leva e traz informações, público ou privado. Também validam os logins para saber se podemos acessar uma aula.

Gatway -> Intermediário

HTTPS -> HyperText Transfer Protocol Secure

Cache -> Histórico temporário até que sejam carregadas novas informações.

Ex: Proxy ajudou a guardar endereço of-line em cache.

Balanceamento de carga através de um proxy -> manejo de fluxo para reduzir tráfego nos servidores e datacenter...

'''
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Métodos de Requisição HTTP

'''
Principais Métodos de Requisição são 5:

1-> GET = Faz uma CONSULTA a um registro ou a uma coleção de registro do servidor

2-> POST = Envia dados para CRIAR um 'novo registro' no servidor

3-> PUT = Envia dados para ATUALIZAR um 'registro existente' no servidor.

4-> DELETE = EXCLUIR registros do servidor.

5-> PATCH = Envia dados para atualizar parcialmente um registro existente do servidor. (Não entendi direito isso)

=================================================

Os 4 principais elementos das etapas de comunicação do protocolo http:

- Connect = atribui conexão remota dentro do servidor (endpoit - ponto de extremidade)

- Options = descreve as opções de comunicação para um recurso especifico.

- Trace = projetado para fins de diagnóstico durante o desenvolvimento

- Head = recupera os cabeçalhos do recurso para o próprio recurso.


'''
'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: HTTP.cat

'''
================================================

Todo Pedido tem uma resposta: HTTP Cats API

httpcats/http.cat

https://http.cat/

USAGE API:
https://http.cat/[status_code]


'''
'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: HTTPS

'''
HTTPS -> HyperText Transfer Protocol Secure

Insere uma camada de segurança nos processos. Seja criptografando dados sensíveis, por exemplo. Evitando a leitura em mensagens abordadas no meio do caminho, por estarem criptografadas.

Certificados de Segurança SSL


'''
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: O que são APIs?

'''
Introdução à APIs:

API = Application Programming Interface / Interface de Programação de Aplicativos

APIs são interfaces que permitem a comunicação e a integração entre diferentes aplicações de software (sites, aplicativos e dispositivos).

Podem ser criadas para uso próprio ou de terceiros (google maps)

Cliente -> Requeste e/ou Response <- API <-> API Server

CICLO: Postman (Ajuda a testar as APIs)

Cliente -> Request -> API -> API Server -> API -> Response -> Cliente

=============================================

Dois principais modelos de destribuição de APIs:

REST vs. SOAP 

SOAP -> é tipo um envelope de carta (sobrecarga, mais largura de banda, mais trabalho em ambas as extremidades)

REST -> é tipo um cartão postal (Mais leve, mais rápito, pode ser armazenado em cache e mais fácil de atualizar)

==============================================

As APIs são o ponto de conexão com os Dados!

Métodos de requisição HTTP: CRUD

CREATE / CRIAR -> POST

READ / LER -> GET

UPDATE / ATULALIZAR -> PUT ou PATCH

DELETE / APAGAR -> DELETE

'''
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Explorando uma API com Postman
'''
Link: postman.com e https://rickandmortyapi.com/

Postman é uma plataforma API para construir e usar APIs. O Postman simplifica cada etapa do ciclo de vida da API e agiliza a colaboração para que você possa criar APIs melhores e mais rapidamente.

Postman - Login Google mm.no.linkedin@gmail.com


https://rickandmortyapi.com/

GET https://rickandmortyapi.com/api/character/2

GET https://rickandmortyapi.com/api/episode/10,28

copie o http da busca que vc escolher.


cole no site do Postman:

login -> My Workspace -> New -> HTTP -> Selecione o metodo (get, post?) -> colo a url que pegou do site da api desejada -> Send -> 

Para visualizar os http das APIs! 

'''


'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Estrutura de uma REST API com JSON

'''
Estrutura de uma REST API:

REST -> Representational State Transfer

Rest Cliente x Rest Transfer

Rest Request x Rest Response:

- Request -> GET/POST/PUT/DELETE method
- Response -> XML/JSON format

Endpoint -> destino de acesso

headers ->

body ->

response ->


O JSON traz um dicionário de dados!

Estudar um pouco de JSON!

Flask -> é uma biblioteca python.

'''

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: APIs (QUIZ)
'''




'''

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Introdução ao Flask

'''

Link: https://json-schema.org/


"Flask Web development, one drop at a time"

Flask é um micro framework que utiliza a linguagem Python para criar aplicativos web.

Já consegue integrar com a Web

WSGI - estabelece interface comum entre os servidores...

REQUEST -> Ajuda o fluxo de comunicação

Dinja -> rever

Carregar = Listar o perfil de personagens

O Arquivo do HTML será um Template para mostrar os dados.



'''

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Instalação do Flask
'''
Obs: Testes realizados na pasta FLASK-APP

VSCode -> Abrir o VSCode

- Pasta FLASK-APP
- Arquivo app.py

Abrir um Terminal PowerShell, dentro da pasta FLASK-APP:

Criar um Ambiente Virtual: (py -3 -m venv .venv)
=> py -3 -m venv .venv

Ativar o Ambiente Virtual:
=> .\.venv\Scripts\activate

Instalação do FLASK no ambiente virtual:
=> pip install Flask

Se precisar atualizar o pip, pode fazer conforme a msg.:
=> python.exe -m pip install --upgrade pip

PRONTO - Podemos começar a criar as primeiras Rotas do Projeto!

'''

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: "Olá, WoMakers" com Flask
'''
ROTAS em Flask:
Com o VENV ativado!

Para Ativar o Servidor no Flask:  "Levantar um Servidor Local"

=> flask --app app_01 run

(segundo app é o nome do arquivo app_01.py)
(Vai gerar um link do LocalHost)


Atenção: Como a Live Reeload não está ativada, caso algo seja mudado no arquivo app.py, deve ser interrompido o servidor com ctrl+c , rode com ...run novamente e então será recarregada a atualização.


'''
'''
# Arquivo - app_01.py

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Olá, WoMakers!'

    # PARA RODAR NO TERMINAL PWSL => flask --app app_01 run


'''

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Criando um JSON de resultados

'''
================================
lISTAR OS ELEMENTOS DA API RICK E MARTH - 

# Arquivo - app_02.py

from flask import Flask
# Classes e Bibliotecas:
import urllib.request, json

app = Flask(__name__)

@app.route("/")
def get_list_characters():

    # URL retirada da API publica - Vai listar todos os personagens cadastrados
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]
        } 

        characters.append(character)

    return {"characters": characters}


# PARA RODAR NO TERMINAL PWSL => flask --app app_02 run


'''

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Criando um template
'''

parei aqui e nao entendi nada. digitar o codigo e pedir ajuda ao chat gpt




'''

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Customizando o template
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Detalhe de um personagem - Parte 1
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Detalhe de um personagem - Parte 2
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Detalhe de um personagem - Parte 3
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Detalhe de um personagem - Parte 4
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Introdução ao FastAPI
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Métodos Síncronos e Assíncronos
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Instalação do FastAPI
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Trabalhando com parâmetros simples
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: User Model
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: HTTP GET Request
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: HTTP POST Requests
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: HTTP DELETE Requests
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: HTTP Exceptions
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Documentação da API
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Flask e Fast (QUIZ)
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Introdução ao Codespaces e GitHub Copilot (Opcional)
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================

# ! MATERIA: Criar e gerenciar projetos no Python (QUIZ)
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA: Avalie seu desempenho e o conteúdo do mês.
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA:
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA:
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA:
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA:
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA:
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================
# ! MATERIA:
#
#

'''
RESULTADO NO CONSOLE:

'''

'''
#? DICAS E ANOTAÇÕES:

'''

print("=========================================================================")
# ==============================================================================