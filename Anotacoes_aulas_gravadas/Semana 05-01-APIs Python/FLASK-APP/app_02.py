from flask import Flask
# Classes e Bibliotecas:
import urllib.request
import json

app = Flask(__name__)

@app.route("/")
def get_list_characters():

    url = "https://rickandmortyapi.com/api/character/"
    response = urllib.request.urlopen(url)
    characters = response.read()
    dict = json.loads(characters)

    characters = []

#Looping Laço de repetição
    for character in dict["results"]:
        character = {
            "name": character["name"],
            "status": character["status"]
        } 

        characters.append(character)

    return {"characters": characters}


# PARA RODAR NO TERMINAL PWSL:
# => .\.venv\Scripts\activate
# => flask --app app_02 run

# * No Navegador Bing, se colarmos o link do servidor, trará as informações organizadas tipo dicionário.
