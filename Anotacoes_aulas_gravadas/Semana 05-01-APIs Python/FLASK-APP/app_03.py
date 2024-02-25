from flask import Flask
# Classes e Bibliotecas:
import urllib.request, json

app = Flask(__name__)

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



# PARA RODAR NO TERMINAL PWSL:
# => .\.venv\Scripts\activate
# => python manage.py runserver
# => flask --app app_3 run