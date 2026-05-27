from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def questao1():
    return render_template("questao1.html", name = "Ayller")

@app.route("/questao2")
def questao2():
    dados = [{"nome" : "Ayller", "idade": 18}]
    return render_template("questao2.html", alunos = dados)

@app.route("/questao3")
def questao3():
    dados = [{"nome" : "Ana", "email": "ana@email.com"}]
    return render_template("questao3.html", nomail = dados)

if __name__ == "__main__":
    app.run(debug=True)