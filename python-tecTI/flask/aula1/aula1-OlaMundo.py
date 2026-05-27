from flask import Flask

app = Flask(__name__)  # inicio o flask


@app.route(
    "/"
)  # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return "Olá, Mundo!"  # Isso é o que será retornado quando a rota '/' for acessada


@app.route(
    "/hello"
)  # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def hello():
    return "Hello, World!"  # Isso é o que será retornado quando a rota '/hello' for acessada


@app.route("/decorator")
def decorator():
    return """
    <h1>O que é um Decorator em Python?</h1>

    <h2>O que é?</h2>
    <p>
        Um <strong>decorator</strong> é uma função que recebe outra função como argumento
        e retorna uma nova função com comportamento modificado ou estendido,
        sem alterar o código original da função decorada.
        Em Python, é representado pelo símbolo <code>@</code> antes do nome da função.
    </p>

    <h2>Para que ele serve?</h2>
    <p>
        Serve para adicionar funcionalidades extras a uma função de forma simples e reutilizável.
        Exemplos de uso: autenticação, logging, controle de acesso, medição de tempo de execução, etc.
    </p>

    <h2>Como ele é utilizado no Flask?</h2>
    <p>
        No Flask, o decorator <code>@app.route()</code> é usado para mapear uma URL
        a uma função Python. Quando o usuário acessa aquela URL no navegador,
        o Flask chama automaticamente a função associada.
    </p>
    <p>Exemplo:</p>
    <pre>
@app.route('/decorator')
def decorator():
    return 'Esta função foi mapeada para a rota /decorator'
    </pre>
    """


if __name__ == "__main__":
    app.run(debug=True)
