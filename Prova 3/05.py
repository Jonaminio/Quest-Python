from flask import Flask,render_template,redirect, url_for, request

app = Flask('teste')


@app.route("/")

def home():
    return "<h1>Período de Vacinação</h1>" \
           "<h2>Para saber, precisamos de alguns dados seus:</h2>" \
           "<h3>1- Nome:</h3>" \
           "<h3>2- Idade:</h3>" \
           "<h3>3- Possui Comorbidades? ( SIM ou NÃO)</h3>" \
           "<h3>4- É trabalhador da Saúde? (SIM ou NÃO)</h3>" \
           "<h3>É Professor, pertence as forças armadas, ou faz parte da população privada de liberdade? (SIM ou NÃO)</h3>" \
           ""
@app.route("/Primeirafase>")

def name():
    return "<h1> usr</h1>"
app.run()