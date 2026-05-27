from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "<h1>Página inicial</h1>"


@app.route("/<nome>")
def usuario(nome):
    return f"<h1>Bem-vindo, {nome}!</h1>"


if __name__ == "__main__":
    app.run(debug=True)
