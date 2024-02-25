from flask import Flask, render_template
# Classes e Bibliotecas:
import urllib.request, json

app = Flask(__name__)

# --------------------------------------------------------------
# ROTA 05: HOME -> Projeto real (Rota Principal)
@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters.html", characters=dict["results"])

# --------------------------------------------------------------
# ROTA 04: Único Personagem ID -> Projeto real
@app.route("/profile/<id>")
def get_profile(id):
    url = "https://rickandmortyapi.com/api/character/" + id
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("profile.html", profile=dict)




# TESTES ANTERIORES:
# --------------------------------------------------------------
# ROTA 03: Lista com Foto (app_05.py com character_02.html = http://127.0.0.1:5000/foto)
@app.route("/foto")
def get_list_characters_page_foto():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters_02.html", characters=dict["results"])

# --------------------------------------------------------------
# ROTA 02: Lista (app_04.py com character_01.html)
@app.route("/lista")
def get_list_characters_page1():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters_01.html", characters=dict["results"])

# --------------------------------------------------------------
# ROTA 01: Todos Personagens
# Lista todos os personagens da API Rick and Morth:
@app.route("/todos")
def get_list_characters():

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


# Arquivo Correto app_05.py
# Roda Lista com Arquivo characters_02.html

# PARA RODAR NO TERMINAL PWSL:
# => .\.venv\Scripts\activate
# => flask --app app_5 run