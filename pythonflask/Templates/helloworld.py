from flask import Flask, render_template,redirect, url_for, request

app = Flask(__name__)

#@app.route("/")
# def home():
#     return "olá <h1>Criando Páginas com Flask</h1>"
#
# if __name__ == "__main__":
#     app.run()

@app.route("/")
def home():
     return render_template("index.html")

# @app.route("/<name>")
# def name(name)
@app.route("/login", methods=["POST","GET"])
def login():
    if request.method == "POST":
        user = request.form["nome"]
        print(user)
        return redirect(url_for('name', usr=user))
    else:
        return render_template("login.html")
'''
@app.route("/<usr>")
def name(usr):
    return f"<h1>{usr}</h1>"
'''
@app.route("/<name>")
def name2(name):
    return render_template("index3.html", content=name, parametro=["ai","ei","ou"])

if __name__ == "__main__":
    app.run(debug=True)
