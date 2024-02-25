from flask import Flask

#classe app
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h1>Olá, WoMakers!</h1>'


# PARA RODAR NO TERMINAL PWSL:
# => .\.venv\Scripts\activate
# => python manage.py runserver
# => flask --app app_01 run
