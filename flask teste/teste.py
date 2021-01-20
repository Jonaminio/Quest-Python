from flask import Flask

app = Flask('teste')


@app.route("/")


def home():
    return "olá <h1>Criando Páginas com Flask</h1>"

app.run()
