
# ! BOOTCAMP WoMakers Code - 01/2024
# =============================================================================================
# * Curso HTML5 e CSS3:
# Introdução à WEB

# A WEB foi criada em 1992 por Tim Berners-Lee, com objetivo de compartilhar documentos entre 
# centros de pesquisas. WWW significa Word Wide Web (Grande Rede Mundial).

# HTML e Navegadores -> Consórcio W3C padronizam o HTML e suas boas práticas.

# Suporte dos navegadores -> Verificar em https://caniuse.com/

# Configurando Ambiente Chrome e VSCode + Extenção Live Server

# Pasta -> Potencia Feminina

# Para acessar Porta no Navegador -> No Navegador digite: localhost:5500  (Exemplo do numero indicado)

# Acesse os links abaixo:

# Projeto do curso no Github
# https://github.com/WoMakersCode/html-css-womakerscode-irme

# Site W3C
# https://www.w3.org/

# Site Can I Use?
# https://caniuse.com/

# Google Chrome
# https://www.google.com/intl/pt-BR/chrome/

# Visual Studio Code
# https://code.visualstudio.com/?WT.mc_id=javascript-12143-gllemos

# Visual Studio Live Server
# http://bit.ly/2VqzdzT


# =============================================================================================
# * Aula 02: Estrutura

# Parei Aula 1 Introdução ao html 

# Tags:

# <p>conteúdo da tag</p>

# Aninhamento de elementos:

# <p>Exemplo de <em>aninhamento</em>.</p>


# =============================================================================================
# * Aula 03: Atributos declarados

# class="exemplo"

# <p class="exemplo">Exemplo de atributo.</p>
# Será explicado posteriormente

# =============================================================================================
# * Aula 04: Principais Tags

# <!DOCTYPE html>
# ?indica a versão htmp mais atualizada
# <html>
# ?contem as tags html da página inteira
#     <head>
# ?Informações de cabeçalho e especifidade de configurações (tipo de codificação por exemplo)
#         <meta charset="utf-8">
#         <title>Potência Feminina</title>
#         ? indica qual nome irá aparecer na aba da página e não é = ao h1 do body
#     </head>
#     <body>
#     ? todo conteúdo do site
#       <p>Este é um parágrafo</P>
#       ?Parágrafo
#       <h1>Título</h1>
#       ?Títulos
#     </body>
# </html>

# =============================================================================================
# * Aula 05: Principais Tags - Trabalhando com Meta Informações / Ajuda nos conteúdos de busca

# <!DOCTYPE html>
# <html lang="pt-br">
# ?Atributo Global Lang para indicar o idioma que foi escrito
#     <head>
#      ?Meta informações ou Meta Dados inseridos no Head
#         <meta charset="utf-8">
#         <meta name="author" content="Marcia Moreira">
#         ?Content quer dizer: conteúdo
#         <meta nome="description" content="Aula sobre metadados para o curso de HTML5">
#         ? Uma boa descrição ajuda no mecanismo de busca
#         <title>Potência Feminina</title>
#     </head>
#     <body>
#       <h1>Este é um elemento que vai no elemento body</h1>
#       <p>Este é um parágrafo</P>
#       <p lang="en">This is a paragraph in English</P>
#       ?Para indicar que conteúdo específico está em idioma diferente aos demais.
#     </body>
# </html>


# =============================================================================================
# * Aula 06: Principais Tags - Trabalhando com textos
# ?cada parágrafo deve estar dentro da tag p.

# Obedecer hierarquia na página dos h.

#? há seis elementos de título em html: h1 principal h2 subtítulo, h3 sub-subtítulos...
#?Obedecer a hierarquia de níveis de título
# <body>
# Elementos de título
# <h1> Isso é um parágrafo h1 </h1>
# <h2> Isso é um parágrafo h2 </h2>
# <h3> Isso é um parágrafo h3 </h3>
# <h4> Isso é um parágrafo h4 </h4>
# <h5> Isso é um parágrafo h5 </h5>
# <h6> Isso é um parágrafo h6 </h6>

#? boa prática usar no máximo 3 níveis de título

# <p>Isso é um parágrafo <em>com ênfase aqui<em>.</p>
#? em -> itálico

# <p>Isso é um parágrafo <strong>com importância<strong>bem aqui.</p>
#? strong -> marcação em destaque
# </body>

# # =============================================================================================
# * Aula 07: Principais Tags - Trabalhando com listas
# listas para organizar navegação

# <body>
# <h2>Lista Ordenada</h2>
#? É importante haver ordem nesta lista
# <ol>
#     <li>Primeiro ítem</li>
#     <li>Segundo Ítem</li>
# </ol>

# <h2>Lista Não Ordenada</h2>
#? A órdem dos ítens não importa
# <ul>
#     <li>Primeiro ítem</li>
#     <li>Segundo Ítem</li>
# </ul>
# </body>

# =============================================================================================
# * Aula 08: Principais Tags - Trabalhando com Links

# <body>
# <h2>Trabalhando com Links</h2>
# <p>Este é um link para o <a href="https://www.google.com.br/" title="O maior site de busca" target="_blank" rel=noreferrer noopener>site do Google</a></p>
# </body>
#? inserir no padrão arquivo html

# target -> para abrir o link em outra aba
# rel -> para segurança do site

# =============================================================================================
# * Aula 09: Principais Tags - Formulários

# Mais simples e direto/ usar rascunho do que deseja

# <!DOCTYPE html>
# <html lang="pt-br">
#     <head>
#         <meta charset="utf-8">
#         <meta name="author" content="Marcia Moreira">
#         <meta nome="description" content="Aula sobre metadados para o curso de HTML5"
#         <title>Potência Feminina</title>
#     </head>
#     <body>
#       <h1>Este é um elemento que vai no elemento body</h1>
#       <p>Este é um parágrafo</P>
#       <p lang="en">This is a paragraph in English</P>
#       <h2>Trabalhando com Links</h2>
#       <p>Este é um link para o <a href="https://www.google.com.br/" title="O maior site de busca" target="_blank" rel=noreferrer noopener>site do Google</a></p>
        # <h2>Trabalhando com Formulários</h2>
        # <form>
        #     <div>
        #         <label for="nome"Nome:></label>
        #         <input type="text" id="nome" placeholder="Digite seu nome">
        #     </div>
        #     <div>
        #         <label for="email">E-mail:</label>
        #         <input type="email" id="email" placeholder="Digite seu e-mail">
        #     </div>
        #     <div>
        #         <label for="mensagem">Mensagem:</label>
        #         <textarea id="mensagem" placeholder="Digite sua mensagem">Esse campo está preenchido</textarea>
        #     </div>
        #     <div>
        #         <button type="submit">Eviar mensagem e limpar formulário</button>
        #     </div>
        # </form>
#     </body>
# </html>

# Passamos ao for o mesmo nome do id da label!
# Placeholder -> trará uma orientação no formuário
# imput -> onde usuário pode escrever no site
#? descobrir como fazer com o que o botão enviar de uma página, realmente funcione.

# =============================================================================================
# * Aula 10: Principais Tags - Trabalhando com Multimídias (Imagens)

# <img src=imagnes/irme.png alt="logo do Instituto Rede Mulher Empreendedora" title="Logotipo IME">

#? o alt deve ser usado para caso a imagem não carrega, veremos pelo nome alt do que se trata!
#? title é pra termos legenda da foto quando passamos o mause sobre

# Se o conteúdo for irrelevante, deixe o alt vazio
# <img src=imagnes/irme.png alt=" ">

#? Figure:
# Quando precisamos usar imagem e legenda da imagem:
# <figure>
#     <img src=imagnes/irme.png alt="logo do Instituto Rede Mulher Empreendedora">
#     <figcaption>Logotipo IME</figcaption>
# </figure>

# Cuidado com as permissões de imágens (imágens de domínio público)
# =============================================================================================
# * Aula 11: Principais Tags - Trabalhando com Tabelas

# <h2>Trabalhando com Tabelas</h2>
# <table>
#     <caption>Datas de Aniversário</caption> #? É o título da nossa tabela centralizado
#     <tr> #? Criar Linhas - TR
#         <td>Nome</td> #? Criar Colunas - TD
#         <td>Idade</td>
#         <td>Aniversário</td>
#     </tr>
#     <tr>
#         <td>Larissa</td>
#         <td>26</td>
#         <td>07/07</td>
#     </tr>
#     <tr>
#         <td>Enzo</td>
#         <td>09</td>
#         <td>31/07o</td>
#     </tr>
# </table>


# Caption -> é o título da nossa tabela, centralizado

# =============================================================================================
# * Aula 12: Principais Tags - Outros

# <header>Cabeçalho do Site</header>

# <main>Conteudo principal da página</main>
# não pode estar dentro das tag: aside, footer, header, article ou nav

# <footer>Rodapé</footer
# Informações de autoria, contatos...

# nav -> Seção de navegação: links a determinadas páginas do nosso site. pode ter vários nav.

# <nav>
#     <ul>
#         <li><a href="#">Página Inicial</a></li>
#         <li><a href="#">Sobre</a></li>
#         <li><a href="#">Contato</a></li>
#     </ul>
# </nav>


# ASSIDE: não entendi direito. Pesquisar.
# <aside>
#     <p>Conteúdo relacionado ao main.</p>
# </aside>

# ARTICLE: pode representar artigos independentes. Trechos
# <article>
#     <h3>Um artigo do site</h3>
#     <p>Esse artigo é muito bom.</p>
# </article>

# SECTION: representa uma seção na página
# <section>
#     <h1>Esta é uma seção</h1> #Pode ter seções
#     <p>Essa seção é maneira.</p>
# </section>

# DIV: Tag genérica para agrupar e estilizar sem valor semântico
# <div>
#     <h1>Esta é uma DIV</h1>
#     <p>Essa DIV é maneira.</p>
# </div>

# SPAN: utilizamos como div só que em TEXTOS para estilizarmos uma parte específica.
# <p>Aqui temos um parágrafo <span>com um span</span>.</p>


# =============================================================================================
# * Aula 13: Recursos Adicionais

# Acesse os links abaixo:

# [ARTIGO] Elementos HTML
# https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element

# [ARTIGO] Atributos HTML
# https://developer.mozilla.org/pt-BR/docs/HTML/Attributes

# [ARTIGO] Meta Informações
# https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/meta

# [ARTIGO] Elementos HTML de conteúdo textual
# https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element#conte%C3%BAdo_textual

# [ARTIGO] Semânticas textuais inline
# https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element#sem%C3%A2nticas_textuais_inline

# [ARTIGO] Criando hyperlinks
# https://developer.mozilla.org/pt-BR/docs/Aprender/HTML/Introducao_ao_HTML/Criando_hyperlinks

# [ARTIGO] Formulários em HTML
# https://developer.mozilla.org/pt-BR/docs/Web/Guide/HTML/Forms

# [ARTIGO] Trabalhando com Botões
# https://developer.mozilla.org/pt-BR/docs/Web/HTML/Element/button

# [ARTIGO] Conteúdos Multimídia e Embutidos na página
# https://developer.mozilla.org/pt-BR/docs/Aprender/HTML/Multimedia_and_embedding

# [ARTIGO] Tabelas em HTML
# https://developer.mozilla.org/pt-BR/docs/Aprender/HTML/Tables

# MÓDULO HTML CONCLUÍDO 1833H 21-01-23

# =============================================================================================

# QUIZ Módulo 02

# =============================================================================================
# * Aula 01: Gerenciamento de foco (tecla TAB do teclado) com tabIndex=""

# O tabindex="", pode ser usado para mudar a ordem do foco ou retirar o foco 
# A ordem será as div com tabindex positivos diferentes de sero e depois se houver algum interativo nativo... quando acaba o tab sai da página

# Não é boa prática ter essas ordem de foco muito embaralhadas, ideal criar o formulário já na ordem natural!

'''
<body>
  <h2>Gerenciamento de Foco 'piscando para escrever'</h2>
  <label for="input">Segundo elemento focado</label>
  <input type="text" id=input>

  #Por padrão todos vem com TabIndex 0! então esse não altera a preioridade
  <div tabindex="0"> Terceiro elemento focado.</div>

  #Caso não queiramos focar essa div, usamos -1
   <label for="input" tabindex="-1">Segundo elemento focado</label>
   <input type="text" id=input>

  <div>Essa div não é naturalmente focada, a não ser que tenha tabindex definido</div>

  # Essa será a primeira a ser focada -> tabindex=1
  <div tabindex="1">Primeiro elemento focado</div>
</body>


'''


# =============================================================================================
# * Por que semântica é tão importante? :

'''
clara e objetiva
respeitar a ordem do leitor de tela
não utilizar linguagem inapropriada

'''


# =============================================================================================
# * Entendendo a semântica com WAI-ARIA  - Papéis:

'''
WAI-ARIA -> Accessible Rich Internet Applications

- Especificação do W3C para melhorar a acessibilidade
- Utilizamos para expandir a semântica nativa do nosso HTML

Regras Básicas -> Usar os elementos com propósito para qual foram criados. Serem descritivos e nunca descaracterizados. Os elementos precisam ser acessíveis por teclados.

PAPEIS/FUNÇÕES do ARIA roles -> usamos para indicar o que o elemento é ou faz. Evite usar caso o elemento já faça por padrão!!!

<form role="search"></form>

#! no slide tem um link com todos os wai-aria roles!


'''

# =============================================================================================
# * Entendendo a semântica com WAI-ARIA  - Estado e Propriedades:

'''
ARIA properties -> Propriedades
- adiciona semantica nos elementos que não tem por padrão
- declaramos utilizando atributos com prefixo "aria-" nos nossos elementos
Ex: <button aria-haspopup="true"></button>


ARIA states -> Estados
- informa a condição atual dos elementos dinâmicos
- declaramos utilizando atributos com prefixo "aria-" nos nossos elementos
Ex: <input type="checkbox" aria-selected="true">

'''
# =============================================================================================
# * Aprendendo um pouco mais sobre acessibilidade:

'''
Ferramentas de Teste de Acessibilidade:
- leitores de tela (VERSÕES GRATUITAS)
- Plugins para navegadores
- SITES QUE VERIFICAM A ACESSIBILIDADE DE OUTROS SITES (analisa e informa o que pode ser melhorado)

'''


#! INTRODUÇÃO AO CSS (25-01-2024)

# =============================================================================================
# * Formas de utilizar o CSS:

'''

1-> CSS INLINE:

<style>
  p{
  color: red;
  }
</style>
<body>
 <h2>Formas de utilizar o css</h2>
 <p>Essa é a forma - inline</p>


 2-> CSS Interno
# rever
<p style="color: red">Essa é a forma - interna</p>


 3-> CSS Externo


#!Parei aqui

'''

# =============================================================================================
# * Y:


# =============================================================================================
# * Y:


# =============================================================================================
# * Y:


# =============================================================================================
# * Y:


# =============================================================================================
# * Y:


# =============================================================================================
# * Y:


# =============================================================================================
# * Y:


# =============================================================================================
# * Y:


# =============================================================================================
# * Y:

# =============================================================================================
# * Y:


# =============================================================================================
# * Y:

# =============================================================================================
# * Y:


# =============================================================================================
# * Y:

# =============================================================================================
# * Y:


# =============================================================================================
# * Y: