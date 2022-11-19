from flask import Flask, render_template, url_for

app = Flask("__name__")

@app.route("/") 
def home(): 
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")

@app.route("/experiencias")
def experiencias():
    return render_template("experiencias.html")

@app.route("/projetos")
def projetos():
    return render_template("projetos.html")

if __name__ == "__main__":
    app.run(debug=True)