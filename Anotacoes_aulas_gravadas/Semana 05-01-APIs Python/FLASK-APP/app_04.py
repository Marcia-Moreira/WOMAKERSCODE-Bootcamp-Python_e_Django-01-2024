from flask import Flask, render_template
# Classes e Bibliotecas:
import urllib.request, json

app = Flask(__name__)

# ROTA 01:
@app.route("/")
def get_list_characters_page():
    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    data = response.read()
    dict = json.loads(data)

    return render_template("characters_01.html", characters=dict["results"])

# --------------------------------------------------------------
# ROTA 02: Todos Personagens
# Lista todos os personagens da API Rick and Morth:
@app.route("/lista")
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


# Arquivo Correto app_04.py
# Roda Lista com Arquivo characters_01.html

# PARA RODAR NO TERMINAL PWSL:
# => .\.venv\Scripts\activate
# => flask --app app_4 run